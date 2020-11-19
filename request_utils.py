import json
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image


def predict_from_file(request_url, image_path):
    """
    predict label from image

    parameter:
    request_url: predict url
    image_path: image path

    return:
    label: label
    """
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = image.astype(np.float32) / 255.0
    image = image.tolist()

    return send_predict_request(request_url, image)


def predict_from_url(request_url, image_url):
    """
    predict label from image(url)

    parameter:
    request_url: predict url
    image_path: image path

    return
    label: label
    """
    image = BytesIO(requests.get(image_url).content)
    image = Image.open(image)
    image = np.array(image, dtype=np.float32) / 255.0
    image = image.tolist()

    return send_predict_request(request_url, image)


def send_predict_request(url, image):
    headers = {"content-type": "application/json"}
    body = {"inputs": [image]}
    r = requests.post(url, data=json.dumps(body), headers=headers)
    r_json = json.loads(r.text)
    return r_json['outputs']['Prediction'][0]
