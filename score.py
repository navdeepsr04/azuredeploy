import json
import joblib
import numpy as np
import os

def init():
    global model
    
    # Azure automatically mounts model here
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    
    data = json.loads(raw_data)
    data = np.array(data)
    
    prediction = model.predict(data)
    
    return prediction.tolist()