from PyQt5.QtCore import QTimer
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

    def __init__(self, list1, parent=None):
        threading.Thread.__init__(self)
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('智能门禁系统')
        self.Duigou.setVisible(False)
        self.Right.setVisible(False)

        self.faceRec = face.Face(list1)

        # 摄像头初始化
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, value=480)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, value=620)

        # test
        self.label_info.setVisible(True)
        self.label_info.raise_()
        # self.label_info.setVisible(False)


        # 动态显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.setTime)
        timer.start()


    def run(self):
        # 设置识别阈值

        count = 0
        while 1:
            threshold = 9


            flag, image = self.cap.read()
            c = cv2.waitKey(30) & 0xff
            if c == 27:
                self.cap.release()
                break

            # show = cv2.resize(image, (1920 , 1080))d
            show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            faces = self.face_cascade.detectMultiScale(show, 1.3, 5)

            # 匹配到人像
            faceCount = 0
            for (x, y, w, h) in faces:
                cv2.rectangle(show, (x, y), (x + w, y + h), (255, 0, 0), 2)
                faceCount += 1
                if faceCount > 1:
                    print("请不要多个人站在摄像头内")
                count += 1
                print("count:{}".format(count))

                if count == threshold:

                    print("成功捕获")
                    image1 = cv2.resize(image, (320, 240))
                    show1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                    showImage1 = QtGui.QImage(show1.data, show1.shape[1], show1.shape[0],
                                              QtGui.QImage.Format_RGB888)

                    self.CaptureLabel.setPixmap(QtGui.QPixmap.fromImage(showImage1))
                    print('标签设置成功')
                    print("开始图像匹配")
                    # 图像匹配
                    me = cv2.resize(image, (80, 45))
                    cv2.imwrite("capture.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 50])

                    score, feedback = self.faceRec.match("capture.jpg")
                    print('Score:', score, "Feedback", feedback)
                    self.SimLabel.setText(str(score))

                    # 查询失败
                    if int(score.replace("%", '')) < 80:
                        feedback = "Source/404.jpg"
                        self.Right.setVisible(True)
                        self.Right.setText("失败")

                    # 查询成功
                    if int(score.replace("%", '')) > 80:
                        self.Right.setVisible(True)
                        self.Duigou.setVisible(True)

                    img = cv2.imread(feedback, 1)
                    img = cv2.resize(img, (320, 240))
                    height, width, bytesPerComponent = img.shape
                    bytesPerLine = 3 * width
                    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                    QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(QImg)
                    self.DataBaseLabel.setPixmap(pixmap)
                    count = 0

            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                     QtGui.QImage.Format_RGB888)

            self.VedioLabel.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def setTime(self):

        WEEK = ['日','一,二', '三', '四', '五', '六', '日']

        hour = str(datetime.datetime.now().hour)
        menute = str(datetime.datetime.now().minute)
        second = str(datetime.datetime.now().second)
        week = datetime.datetime.now().weekday()
        week = str(WEEK[week])

        self.Hour.setText(hour)
        self.Menute.setText(menute)
        self.label_13.setText(second)
        self.WeekDay.setText(week)
        # print(week)
        # print("hello world")



if __name__ == '__main__':
    # k1 = base64.b64encode(open('Source/2.jpg', 'rb').read()).decode()
    # k2 = base64.b64encode(open('Source/3.jpg', 'rb').read()).decode()
    # k3 = base64.b64encode(open('Source/me.jpg', 'rb').read()).decode()
    list1 = app.search_iamge()

    #qt界面初始化
    app=QApplication(sys.argv)

    myWin = MyWindow(list1)
    myWin.show()
    myWin.start()

    sys.exit(app.exec())

