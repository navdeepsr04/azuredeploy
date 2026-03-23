import joblib
import json

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.joblib")
    return model

def input_fn(request_body, request_content_type):
    data = json.loads(request_body)
    return data

def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction

def output_fn(prediction, content_type):
    return json.dumps(prediction.tolist())