import json
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image
import os


def predict_from_file(request_url, image_path):
    """
    predict label from image

    parameter:
    request_url: predict url
    image_path: image path

    return:
    label: label
    """
    if os.path.exists(image_path):
        file_extension = os.path.splitext(os.path.basename(image_path))[-1]
        if file_extension == '.jpg' or file_extension == '.jpeg' or file_extension == '.png':
            image = _image2numpy(image_path)
            return _send_predict_request(request_url, image.tolist())
        else:
            print('画像ではありません。')
    else:
        print('ファイルが見つかりません。')


def predict_from_url(request_url, image_url):
    """
    predict label from image(url)

    parameter:
        request_url url: predict url
        image_path str: image path

    return
        label str
    """
    res = requests.get(image_url)
    content_type = res.headers['Content-Type']
    if res.status_code == 200 and 'jpeg' in content_type or 'png' in content_type:
        try:
            image_bytes = BytesIO(res.content)
        except Exception as err:
            print(err)
        else:
            image = np.array(image_bytes, dtype=np.float32) / 255.0
            image = image.tolist()
            return _send_predict_request(request_url, image)
    else:
        print('Image Not Found')


def _send_predict_request(url, image):
    headers = {"content-type": "application/json"}
    body = {"inputs": [image]}
    r = requests.post(url, data=json.dumps(body), headers=headers)
    r_json = json.loads(r.text)
    # return r_json['outputs']['Prediction'][0]
    return r_json


def _image2numpy(image_file):
    try:
        image = Image.open(image_file).convert('RGB')
    except Exception as err:
        print(err)
    else:
        image = np.asarray(image, dtype=np.float32) / 255.0
        return image
