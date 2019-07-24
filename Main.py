from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from untitled import *
import cv2
import numpy
import time
import datetime
import threading


class MyWindow(QMainWindow,Ui_MainWindow,threading.Thread):
    def __init__(self,parent=None):
        threading.Thread.__init__(self)
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('智能门禁系统')
        self.Duigou.setVisible(True)
        self.Hour.setText("11")



    def run(self):
        WEEK = ['一,二', '三', '四', '五', '六', '日']

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
            #print("hello world")
            time.sleep(1)



if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, value=480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, value=620)

    app=QApplication(sys.argv)
    myWin=MyWindow()
    myWin.show()
    myWin.start()

    #设置识别阈值
    threshold=10
    count=0
    while 1:
        flag, image = cap.read()

        c=cv2.waitKey(30)&0xff
        if c==27:
            cap.release()
            break

        #show = cv2.resize(image, (1920 , 1080))
        show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = face_cascade.detectMultiScale(show, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(show, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count+=1
            #print(count)
            if count==threshold:
                # img = cv2.imread("capture.png", 1)
                # cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
                # cv2.imshow("Image", img)
                # k = cv2.waitKey(0)
                # if k == 27:
                #     cv2.destroyAllWindows()
                image1=cv2.resize(image,(320,240))
                show1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
                showImage1 = QtGui.QImage(show1.data, show1.shape[1], show1.shape[0],
                                         QtGui.QImage.Format_RGB888)

                myWin.CaptureLabel.setPixmap(QtGui.QPixmap.fromImage(showImage1))

        showImage = QtGui.QImage(show.data,show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)

        myWin.VedioLabel.setPixmap(QtGui.QPixmap.fromImage(showImage))

    #cv2.destroyAllWindows()
    cap.release()
    sys.exit(app.exec())

