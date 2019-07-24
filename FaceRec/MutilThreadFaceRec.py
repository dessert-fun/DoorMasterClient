import threading
from aip import AipFace
import base64
import time


def init( img1, img2):
    global src
    global src1
    global client
    global  json1

    src=img1
    src1=img2

    APP_ID = '16866155'
    API_KEY = 'kSzesGu8TY60LgcMxKRuer4p'
    SECRET_KEY = 'naKW6b2KfUsWV03DbDUaspg0gtQ1xeYA'
    src = base64.b64encode(open(src, 'rb').read()).decode()

    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    json1 = {
        'image': src,
        'image_type': 'BASE64'
    }
    print(json1)
    print("初始化成功")


def ImgtoBase64(img):
     return base64.b64encode(open(img, 'rb').read()).decode()

def run(i):
    i=int(i)
    json2 = {
        'image': src1[i],
        'image_type': 'BASE64'
    }
    result = client.match([json1, json2])
    if result['error_msg'] == 'SUCCESS':
        if result['result']['score'] > 80:
            print('他是第{}张图片'.format(i))





if __name__ == '__main__':
    k1 = base64.b64encode(open('../Source/2.jpg', 'rb').read()).decode()
    k2 = base64.b64encode(open('../Source/3.jpg', 'rb').read()).decode()

    list1=[]
    list1.append(k1)
    list1.append(k2)
    #print(list1)
    init('../Source/1.jpg',list1)

    for i in range(len(src1)):
            threading.Thread(target=run,args=str(i)).start()