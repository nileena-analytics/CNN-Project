from tensorflow.keras.application import MobileNetV2
from tensorflow.keras.application.MobileNetV2 import decode_prediction
import numpy as np

class MobileNetClassifier:
    def __init__(self):
        print("Loading of the model...")
        self.model = MobileNetV2(weight = 'imagenet')


    def predict(self, frames):
        if len(frames.shape) = 3:
            frames = np.expand_dims(frames, axis=0)

    preds = self.model.predict(rames,verbose = 1)

    results = []
    for pred in preds:
        decode = decode_prediction(np.expand_dims(pred,0), top =5)[0]
        result.append([(name, float(prob)) for _, name, prob in decode])
    return results
    
