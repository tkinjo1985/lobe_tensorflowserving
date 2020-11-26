
## Usage

Run TensorFlowServing from DcokerImage
```
# docker-compose up --build -d
```
if use your original model replace sample_model folder

Use POST requests to make predict.
```
from request_utils import predict_from_file, predict_from_url

# predict request url
prediction_url = 'http://localhost:8501/v1/models/{ model_name }:predict'
# if model namse sample_model
# prediction_url = 'http://localhost:8501/v1/models/{ sample_model }:predict'


# predict from image_file
predict_label = predict_from_file(prediction_url, 'image file')
print(predict_label)

# predict from image_url
image_url = 'image_url'
predict_label = predict_from_url(prediction_url, image_url)
print(predict_label)
```
