import numpy as np
from typing import Protocol
import openvino as ov
import numpy as np
import cv2

from dotenv import load_dotenv
import os
from zettelsortierung import Zettelwerk

load_dotenv()

class OCRModel(Protocol):
    def read(self, image: np.ndarray) -> str:
        ...

class PaddleOCR:
    def __init__(self):
        # Step 1. Create OpenVINO Runtime Core
        self.core = ov.Core()

        # Step 2. Compile the Model
        #path = '/home/jan/.cache/huggingface/hub/models--monkt--paddleocr-onnx/snapshots/7b02d0a30a07ba2b92ad1ff5a8941ae2c633de65/languages/latin/rec.onnx'
        model_path = os.getenv('PADDLE_OCR_ONNX_MODEL_PATH')
        self.compiled_model = self.core.compile_model(model_path, 'AUTO')
        self.input_layer = self.compiled_model.input(0)
        self.output_layer = self.compiled_model.output(0)

        # Step 3. Create an Inference Request
        self.infer_request = self.compiled_model.create_infer_request()

    def read(self, image: np.ndarray) -> str:
        result = self.model.predict(input=image)
        texts = []
        for res in result:
            print('res:', res)
            #return ' '.join(res['rec_texts'])
            text = ' '.join(res['rec_texts'])
            texts.append(text)
        return '\n'.join(texts)

    def predict(self, image_array: np.array) -> str:
        # More image processing
        image_array = np.float32([image_array]) / 255.0
        image_array = np.transpose(image_array, (0, 3, 1, 2))
        input_tensor = ov.Tensor(array=image_array, shared_memory=False)
        # for shared_memory=True, input must be contiguous
        # TODO: try if this is faster

        # TODO: See if batching helps with speeding up, so that requests become unnecessary
        #result = self.compiled_model(input_tensor)[self.output_layer]
        #return result

        # Set input tensor for model with one input
        self.infer_request.set_input_tensor(input_tensor)

        # Step 5. Start Inference
        self.infer_request.start_async()
        self.infer_request.wait()

        # Step 6. Process the Inference Results
        output = self.infer_request.get_output_tensor()
        output_buffer = output.data
        return output_buffer

    @staticmethod
    def load_character_dict(dict_path):
        with open(dict_path, "r", encoding="utf-8") as f:
            chars = [line.strip("\n") for line in f]
        chars.insert(0, "")     # CTC blank at index 0
        chars.insert(503, ' ')  # Space at index 503
        return chars
    
    # Should eventually be replaced by some kind of beamsearch
    # Also, needs to be adjusted once we batch inputs
    @staticmethod
    def ctc_decode(preds, characters):
        """
        preds: numpy array [1, T, C]
        characters: list of vocab characters (with blank at index 0)
        """
        preds = preds[0]  # remove batch dimension

        # Argmax across character dimension
        pred_indices = np.argmax(preds, axis=1)

        text = []
        prev_idx = -1

        for idx in pred_indices:
            if idx != 0 and idx != prev_idx:  # 0 = blank
                text.append(characters[idx])
            prev_idx = idx

        return "".join(text)

'''
if __name__ == "__main__":
    root = os.getenv('ZETTELSAMMLUNG_ROOT')
    zettel = Zettelwerk.Zettelsammlung.collect_zettel(root, 1)[0]
    image = cv2.imread(zettel.recto_file_path)

    model = Paddle()
    result = model.read(image)

    print(result)
'''