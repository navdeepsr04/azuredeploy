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



# AmazonSageMakerServiceCatalogProductsUseRole
# sagemaker-executionrole-xxxx


# {
#  "Version": "2012-10-17",
#  "Statement": [
#   {
#    "Effect": "Allow",
#    "Action": [
#      "s3:GetObject",
#      "s3:PutObject",
#      "s3:ListBucket"
#    ],
#    "Resource": [
#      "arn:aws:s3:::fatpractice2104",
#      "arn:aws:s3:::fatpractice2104/*"
#    ]
#   }
#  ]
# }