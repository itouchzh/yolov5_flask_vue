import base64

import torch
import os
from PIL import Image
import cv2
from io import BytesIO, StringIO


def getbase64(img):
    # os.environ["CUDA_VISIBLE_DEVICES"]
    model = torch.hub.load('./', 'custom', path='./yolov5s.pt', source='local')
    # model.cuda()
    # print(model)
    img1 = Image.open(BytesIO(img))
    # img2 = cv2.imread('./data/images/zidane.jpg')[:,:,::-1]
    imgs = [img1]

    results = model(imgs, size=640)
    print('识别成功')
    results.imgs
    results.render()
    base64_image = ''
    for img in results.imgs:
        buffered = BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(buffered, format='JPEG')
        base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        # with open('./result.txt', 'a+') as f:
        #     f.write(base64_image)
        #     f.close()
    print(results)
    results.save()
    base64_image = 'data:image/jpeg;base64,%s' % base64_image
    return base64_image
    # print(results.xyxy[0])
    # print(results.pandas().xyxy[0])
