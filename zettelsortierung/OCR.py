import os
import numpy as np
import openvino as ov
import openvino.properties.hint as hints
from typing import Protocol
from dotenv import load_dotenv
from dataclasses import replace
from zettelsortierung.Transformation import Transformation, Composition, ResolveDPBatch
from zettelsortierung.DataTypes import DataPoint, DataPointBatch

load_dotenv()


class OCRModel(Protocol):
    def __call__(self, image: np.ndarray) -> str: ...


class PaddleOCR:
    def __init__(self):
        # Create OpenVINO Runtime Core
        self.core = ov.Core()
        self.core.set_property(
            "CPU",
            {hints.execution_mode: hints.ExecutionMode.PERFORMANCE},  # type: ignore
        )

        # Compile the Model
        model_path = os.getenv("PADDLE_OCR_ONNX_MODEL_PATH")
        assert model_path is not None
        config = {hints.performance_mode: hints.PerformanceMode.THROUGHPUT}  # type: ignore
        self.model = self.core.compile_model(model_path, "AUTO", config)

        # Gab Input Layer and Output Layer
        self.input_layer = self.model.input(0)
        self.output_layer = self.model.output(0)

        # Create an Inference Request
        self.infer_request = self.model.create_infer_request()

    def __call__(self, dp_batch: DataPointBatch) -> DataPointBatch:
        self.infer_request.set_input_tensor(dp_batch.feature_batch)
        self.infer_request.infer()  # synchronous
        preds = self.infer_request.get_output_tensor().data.copy()
        return replace(dp_batch, feature_batch=preds)


#####################################################################
# Low-Level OCR Transformations
#####################################################################


class OCRstack(Transformation):
    def transform(self, dp_batch: list[DataPoint]) -> DataPointBatch:
        scan_batch = [dp.scan for dp in dp_batch]
        feature_id_batch = [dp.feature_id for dp in dp_batch]
        feature_batch = []

        w_max = max(dp.feature.shape[1] for dp in dp_batch)
        for dp in dp_batch:
            h, w, c = dp.feature.shape
            padded_patch = np.pad(
                dp.feature,
                ((0, 0), (0, w_max - w), (0, 0)),
                mode="constant",
                constant_values=0,
            )
            feature_batch.append(padded_patch)

        stack = np.stack(feature_batch)
        return DataPointBatch(scan_batch, feature_id_batch, stack)


class OCRnormalize(Transformation):
    def transform(self, dp_batch: DataPointBatch) -> DataPointBatch:
        normalized = np.float32(dp_batch.feature_batch) / 255.0
        return replace(dp_batch, feature_batch=normalized)


class OCRtranspose(Transformation):
    def transform(self, dp_batch: DataPointBatch) -> DataPointBatch:
        # Permute dimensions from [B, H, W, D] to [B, D, H, W]
        transposition = np.transpose(dp_batch.feature_batch, (0, 3, 1, 2))
        return replace(dp_batch, feature_batch=transposition)


class OCRtensorize(Transformation):
    def transform(self, dp_batch: DataPointBatch) -> DataPointBatch:
        tensor = ov.Tensor(array=dp_batch.feature_batch, shared_memory=False)
        return replace(dp_batch, feature_batch=tensor)


class OCRinference(Transformation):
    def __init__(self, model: OCRModel):
        self.model = model

    def transform(self, dp_batch: DataPointBatch):
        return self.model(dp_batch)  # type: ignore


class CTCdecode(Transformation):
    BLANK = 0

    def __init__(self):
        self.characters = self.load_character_dict()

    def transform(self, dp_batch: DataPointBatch) -> DataPointBatch:
        labels = [self.ctc_decode(feature) for feature in dp_batch.feature_batch]
        return replace(dp_batch, feature_batch=labels)

    @classmethod
    def load_character_dict(cls) -> list[str]:
        char_dict_path = os.getenv("PADDLE_OCR_CHAR_DICT_PATH")
        assert char_dict_path is not None
        with open(char_dict_path, mode="r", encoding="utf-8") as f:
            chars = [line.strip("\n") for line in f]
        chars.insert(cls.BLANK, "")  # CTC blank at index 0
        chars.insert(len(chars), " ")  # Space at last index
        return chars

    def ctc_decode(self, preds: np.ndarray):
        """
        preds: numpy array [T, C], where
                T ^= number of predictions
                C ^= number of characters
        """
        pred_indices = np.argmax(preds, axis=1)

        change_mask = np.empty_like(pred_indices, dtype=bool)
        change_mask[0] = True
        change_mask[1:] = pred_indices[1:] != pred_indices[:-1]

        indices = pred_indices[change_mask]
        indices = indices[indices != self.BLANK]

        return "".join(np.take(self.characters, indices))


#####################################################################
# High-Level OCR Transformations
#####################################################################


class OCRpreprocessing(Transformation):
    def __init__(self):
        self.composition = Composition(OCRstack(), OCRnormalize(), OCRtranspose())

    def transform(self, dp_batch: list[DataPoint]) -> DataPointBatch:
        return self.composition(dp_batch)  # type: ignore


class OCR(Transformation):
    def __init__(self):
        self.model = PaddleOCR()
        self.composition = Composition(OCRtensorize(), OCRinference(self.model))  # type: ignore

    def transform(self, dp_batch: list[DataPoint]) -> DataPointBatch:
        return self.composition(dp_batch)  # type: ignore


class OCRpostprocessing(Transformation):
    def __init__(self):
        self.composition = Composition(CTCdecode(), ResolveDPBatch())

    def transform(self, dp_batch: list[DataPoint]) -> DataPointBatch:
        return self.composition(dp_batch)  # type: ignore
