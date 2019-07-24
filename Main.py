from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import app
from untitled import *
import cv2
import time
import datetime
import threading
import base64
import facematch as face

class MyWindow(QMainWindow,Ui_MainWindow,threading.Thread):

    def __init__(self,parent=None):
        threading.Thread.__init__(self)
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('智能门禁系统')
        self.Duigou.setVisible(False)
        self.Right.setVisible(False)


    def run(self):

        WEEK = ['日','一,二', '三', '四', '五', '六', '日']
        while True:
            hour = str(datetime.datetime.now().hour)
            menute = str(datetime.datetime.now().minute)
            second = str(datetime.datetime.now().second)
            week = datetime.datetime.now().weekday()
            week = str(WEEK[week])

            self.Hour.setText(hour)
            self.Menute.setText(menute)
            self.label_13.setText(second)
            self.WeekDay.setText(week)
            #print(week)
            #print("hello world")
            time.sleep(1)


if __name__ == '__main__':
    # k1 = base64.b64encode(open('Source/2.jpg', 'rb').read()).decode()
    # k2 = base64.b64encode(open('Source/3.jpg', 'rb').read()).decode()
    # k3 = base64.b64encode(open('Source/me.jpg', 'rb').read()).decode()
    list1 = app.search_iamge()

    faceRec=face.Face(list1)

    #摄像头初始化
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, value=480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, value=620)

    #qt界面初始化
    app=QApplication(sys.argv)

    myWin=MyWindow()
    myWin.show()
    myWin.start()

    #设置识别阈值
    threshold=9
    count=0
    while 1:
        flag, image = cap.read()
        c=cv2.waitKey(30)&0xff
        if c==27:
            cap.release()
            break

        #show = cv2.resize(image, (1920 , 1080))d
        show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = face_cascade.detectMultiScale(show, 1.3, 5)

        #匹配到人像
        for (x, y, w, h) in faces:
            cv2.rectangle(show, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count+=1

            if count==threshold:

                print("成功捕获")
                image1=cv2.resize(image,(320,240))
                show1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
                showImage1 = QtGui.QImage(show1.data, show1.shape[1], show1.shape[0],
                                         QtGui.QImage.Format_RGB888)

                myWin.CaptureLabel.setPixmap(QtGui.QPixmap.fromImage(showImage1))
                print('标签设置成功')
                print("开始图像匹配")
                #图像匹配
                me=cv2.resize(image,(80,45))
                cv2.imwrite("capture.jpg", image,[cv2.IMWRITE_JPEG_QUALITY, 50])

                score, feedback = faceRec.match("capture.jpg")
                print('Score:',score,"Feedback",feedback)
                myWin.SimLabel.setText(str(score))

                #查询失败
                if int(score.replace("%",''))<80:
                    feedback="Source/404.jpg"
                    myWin.Right.setVisible(True)
                    myWin.Right.setText("失败")

                #查询成功
                if int(score.replace("%",''))>80:
                    myWin.Right.setVisible(True)
                    myWin.Duigou.setVisible(True)

                img = cv2.imread(feedback, 1)
                img=cv2.resize(img,(320,240))
                height, width, bytesPerComponent = img.shape
                bytesPerLine = 3 * width
                cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(QImg)
                myWin.DataBaseLabel.setPixmap(pixmap)



        showImage = QtGui.QImage(show.data,show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)

        myWin.VedioLabel.setPixmap(QtGui.QPixmap.fromImage(showImage))

    #cv2.destroyAllWindows()
    cap.release()
    sys.exit(app.exec())

