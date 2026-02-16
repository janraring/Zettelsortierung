import os
import numpy as np
import openvino as ov
import openvino.properties.hint as hints
from typing import Protocol
from dotenv import load_dotenv

load_dotenv()


class OCRModel(Protocol):
    def __call__(self, image: np.ndarray) -> str:
        pass


# Instructions from https://docs.openvino.ai/2025/openvino-workflow/running-inference.html
class PaddleOCR:
    def __init__(self):
        # Create OpenVINO Runtime Core
        self.core = ov.Core()
        self.core.set_property(
            "CPU",
            {hints.execution_mode: hints.ExecutionMode.PERFORMANCE},
        )

        # Compile the Model
        model_path = os.getenv('PADDLE_OCR_ONNX_MODEL_PATH')
        config = {hints.performance_mode: hints.PerformanceMode.THROUGHPUT}
        self.compiled_model = self.core.compile_model(model_path, 'AUTO', config)

        # Gab Input Layer and Output Layer
        self.input_layer = self.compiled_model.input(0)
        self.output_layer = self.compiled_model.output(0)

        # Create an Inference Request
        self.infer_request = self.compiled_model.create_infer_request()

        # Create Decoding Dictionary
        char_dict_path = os.getenv('PADDLE_OCR_CHAR_DICT_PATH')
        self.characters = self.load_character_dict(char_dict_path)

    @staticmethod
    def load_character_dict(dict_path: str) -> list[str]:
        with open(dict_path, "r", encoding="utf-8") as f:
            chars = [line.strip("\n") for line in f]
        chars.insert(0, "")            # CTC blank at index 0
        chars.insert(len(chars), ' ')  # Space at last index
        return chars

    @staticmethod
    def ctc_decode(preds: np.ndarray, characters: list[str]) -> str:
        """
        preds: numpy array [1, T, C], where
            T ^= number of predictions
            C ^= number of characters
        characters: list of vocab characters (with blank at index 0)
        """
        pred_indices = np.argmax(preds, axis=1)

        # Compute mask for change detection
        change_mask = np.empty_like(pred_indices, dtype=bool)
        change_mask[0] = True
        change_mask[1:] = pred_indices[1:] != pred_indices[:-1]

        # Apply dedup + blank removal
        final_indices = pred_indices[change_mask]
        final_indices = final_indices[final_indices != 0]

        return "".join(np.take(characters, final_indices))

    def __call__(self, im_region_batch: list[np.array]) -> list[str]:
        '''
        Args:
            image_array (np.array): [B, H, W, D], where
                B ^= batch size
                H ^= height
                W ^= width
                D ^= depth
        Returns:
            list[str]: recognized text segments
        '''

        # Normalize
        im_region_batch = np.float32(im_region_batch) / 255.0

        # Permute dimensions from [B, H, W, D] to [B, D, H, W]
        im_region_batch = np.transpose(im_region_batch, (0, 3, 1, 2))
        #im_region_batch = np.ascontiguousarray(im_region_batch)

        # Create input tensor
        input_tensor = ov.Tensor(array=im_region_batch, shared_memory=False)
        # for shared_memory=True, input must be contiguous
        # TODO: try if this is faster

        # Set Input Tensor
        self.infer_request.set_input_tensor(input_tensor)

        # Start Inference
        self.infer_request.start_async()
        self.infer_request.wait()

        # Process the Inference Results
        output_batch = self.infer_request.get_output_tensor()

        # Decode Inference Results
        decoded = [self.ctc_decode(output_batch.data[i], self.characters) for i in range(len(output_batch.data))]

        return decoded

    
    @staticmethod
    def ctc_decode_old(preds: np.ndarray, characters: list[str]):
        """
        preds: numpy array [1, T, C], where
            T ^= number of predictions
            C ^= number of characters
        characters: list of vocab characters (with blank at index 0)
        """

        # Argmax across character dimension
        pred_indices = np.argmax(preds, axis=1)

        text = []
        prev_idx = -1

        for idx in pred_indices:
            if idx != 0 and idx != prev_idx:  # 0 = blank
                text.append(characters[idx])
            prev_idx = idx

        return "".join(text)