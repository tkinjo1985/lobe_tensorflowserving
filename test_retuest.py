from request_utils import predict_from_file

# predict request url
prediction_url = 'http://localhost:8501/v1/models/sample_model:predict'

# predict from image_file
predict_label = predict_from_file(prediction_url, 'cat.99.jpg')
print(predict_label)
