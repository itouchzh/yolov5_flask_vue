# -*- coding: utf-8 -*-
# @Time    : 2022/9/3
# @Author  : rickHan
# @Software: PyCharm
# @File    : app.py.py
import base64
import os
import json
from PIL import Image
import cv2
from io import BytesIO, StringIO
from flask import Flask, request
from yolov5 import getbase64

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello World'


@app.route('/students', methods=['POST'])
def get_students():
    # getbase64(img)
    if request.method == 'POST':
        base64_data = request.json['img']
        print('已经收到了')
        head,context = base64_data.split(',')
        img_data = base64.b64decode(context)
        image =getbase64(img_data)
        print('success')
        return image
        # image.show()
    # img = ''
    # detect_image = getbase64(img)
    # return detect_image
    return 'false'


if __name__ == '__main__':
    app.run()
