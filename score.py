# import json
# import joblib
# import numpy as np
# import os

# def init():
#     global model
    
#     # Azure automatically mounts model here
#     model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model.pkl")
#     model = joblib.load(model_path)

# def run(raw_data):
    
#     data = json.loads(raw_data)
#     data = np.array(data)
    
#     prediction = model.predict(data)
    
#     return prediction.tolist()

import json
import joblib
import os
import numpy as np

def init():
    global model
    try:
        model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
        model = joblib.load(model_path)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Error loading model: {e}")

def run(raw_data):
    try:
        # Parse input JSON
        data = json.loads(raw_data)

        # Expect input like: {"data": [[...features...]]}
        inputs = data.get("data")

        if inputs is None:
            return {"error": "Missing 'data' key in input"}

        # Convert to numpy array (important for sklearn)
        inputs = np.array(inputs)

        # Make prediction
        prediction = model.predict(inputs)

        # Optional: probabilities (for classifiers)
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(inputs).tolist()
            return {
                "prediction": prediction.tolist(),
                "probability": prob
            }

        return {
            "prediction": prediction.tolist()
        }

    except Exception as e:
        return {"error": str(e)}