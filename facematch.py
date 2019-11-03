from aip import AipFace
import base64
import app

class Face(object):

    def __init__(self, img2):
        APP_ID = '17682690'
        API_KEY = '5eCle0cSXa8PHsgjUOiklXVo'
        SECRET_KEY = 'u5P7KVK31knFK6T8i59Sj9ysXq200Hxf'

        self.feedback=None
        self.img2 = img2
        self.client = AipFace(APP_ID, API_KEY, SECRET_KEY)
        print('AIP构造成功')



    def match(self,src):
        self.src = base64.b64encode(open(src, 'rb').read()).decode()
        self.score = 0
        json1 = {
            'image': self.src,
            'image_type': 'BASE64'
        }
        for i in range(len(self.img2)):
            json2 = {
                'image': self.img2[i],
                'image_type': 'BASE64'
            }
            result = self.client.match([json1, json2])
            if result['error_msg'] == 'SUCCESS':
                if result['result']['score'] > 70:
                    self.score = int(result['result']['score'])
                    self.feedback = self.img2[i]
        if self.feedback!=None:
            file = open('feedback.jpg', "wb")
            file.write(base64.b64decode(self.feedback))
            file.close()
        return str(self.score)+'%','feedback.jpg'







if __name__ == '__main__':
    # k1 = base64.b64encode(open('Source/2.jpg', 'rb').read()).decode()
    # k2 = base64.b64encode(open('Source/3.jpg', 'rb').read()).decode()
    # k3=base64.b64encode(open('capture.jpg','rb').read()).decode()
    # print(len(k3))
    list1=app.search_iamge()
    for i in list1:
        print(i)
    # face=Face(list1)
    # scroe,feedback=face.match("capture.jpg")
    # print(scroe,feedback)
