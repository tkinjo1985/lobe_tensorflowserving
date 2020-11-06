
## Usage

Run TensorFlowServing from DcokerImage
```
# docker run -t --rm -p 8501:8501 -v "`pwd`/sample_model:/models/sample_model" -e MODEL_NAME=sample_model tensorflow/serving
```

Use POST requests to make predict.
```
from prediction_request import predict_from_file, predict_from_url

# predict request url
prediction_url = 'http://localhost:8501/v1/models/sample_model:predict'

# predict from image_file
predict_label = predict_from_file(prediction_url, 'test.jpg')
print(predict_label)

# predict from image_url(.jpg)
image_url = 'image_url'
predict_label = predict_from_url(prediction_url, image_url)
print(predict_label)
```
