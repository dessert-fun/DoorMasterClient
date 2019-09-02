# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1492, 866)
        MainWindow.setMinimumSize(QtCore.QSize(1492, 866))
        MainWindow.setMaximumSize(QtCore.QSize(1492, 886))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VedioLabel = QtWidgets.QLabel(self.centralwidget)
        self.VedioLabel.setGeometry(QtCore.QRect(10, 40, 640, 480))
        self.VedioLabel.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:1px solid;")
        self.VedioLabel.setText("")
        self.VedioLabel.setScaledContents(False)
        self.VedioLabel.setObjectName("VedioLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.CaptureLabel = QtWidgets.QLabel(self.centralwidget)
        self.CaptureLabel.setGeometry(QtCore.QRect(680, 40, 320, 240))
        self.CaptureLabel.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:1px solid")
        self.CaptureLabel.setText("")
        self.CaptureLabel.setObjectName("CaptureLabel")
        self.DataBaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.DataBaseLabel.setGeometry(QtCore.QRect(1140, 40, 320, 240))
        self.DataBaseLabel.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:1px solid; ")
        self.DataBaseLabel.setText("")
        self.DataBaseLabel.setObjectName("DataBaseLabel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1010, 110, 120, 120))
        self.label_4.setStyleSheet("image: url(:/ico/Source/yuan.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.SimLabel = QtWidgets.QLabel(self.centralwidget)
        self.SimLabel.setGeometry(QtCore.QRect(1030, 130, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(28)
        self.SimLabel.setFont(font)
        self.SimLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SimLabel.setObjectName("SimLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 560, 631, 221))
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:1px solid;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1030, 80, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 620, 251, 141))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Duigou = QtWidgets.QLabel(self.centralwidget)
        self.Duigou.setGeometry(QtCore.QRect(40, 630, 101, 91))
        self.Duigou.setStyleSheet("image: url(:/ico/Source/duigou.png);")
        self.Duigou.setText("")
        self.Duigou.setObjectName("Duigou")
        self.Right = QtWidgets.QLabel(self.centralwidget)
        self.Right.setGeometry(QtCore.QRect(390, 610, 251, 151))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.Right.setFont(font)
        self.Right.setObjectName("Right")
        # label_6是天气面板展示的内容,现在设一个label_info展示信息
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 310, 801, 471))
        self.label_6.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:1px solid")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        # 使用label_info作为成功后的展示面板
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(670, 310, 801, 471))
        self.label_info.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                      "border:1px solid")
        self.label_info.setText("我是测试")
        self.label_info.setObjectName("label_info")
        self.label_info.setVisible(False)

        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(940, 380, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(36)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(830, 480, 151, 61))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(36)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(830, 580, 141, 51))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(36)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.nameinfo = QtWidgets.QLabel(self.centralwidget)
        self.nameinfo.setGeometry(QtCore.QRect(980, 480, 181, 61))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(36)
        self.nameinfo.setFont(font)
        self.nameinfo.setStyleSheet("backgroud-color:rgb(0, 255, 255)")
        self.nameinfo.setObjectName("name")
        self.number = QtWidgets.QLabel(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(990, 580, 151, 61))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(36)
        self.number.setFont(font)
        self.number.setObjectName("number")





        self.Month = QtWidgets.QLabel(self.centralwidget)
        self.Month.setGeometry(QtCore.QRect(700, 350, 111, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Month.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(72)
        self.Month.setFont(font)
        self.Month.setObjectName("Month")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(810, 350, 121, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(56)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Day = QtWidgets.QLabel(self.centralwidget)
        self.Day.setGeometry(QtCore.QRect(900, 350, 121, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Day.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(72)
        self.Day.setFont(font)
        self.Day.setObjectName("Day")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1020, 360, 91, 111))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(52)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Temp = QtWidgets.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(1200, 360, 151, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Temp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(72)
        self.Temp.setFont(font)
        self.Temp.setAutoFillBackground(False)
        self.Temp.setObjectName("Temp")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1320, 370, 101, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(52)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 500, 191, 141))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(52)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.WeekDay = QtWidgets.QLabel(self.centralwidget)
        self.WeekDay.setGeometry(QtCore.QRect(880, 520, 111, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.WeekDay.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(52)
        self.WeekDay.setFont(font)
        self.WeekDay.setObjectName("WeekDay")
        self.Weather = QtWidgets.QLabel(self.centralwidget)
        self.Weather.setGeometry(QtCore.QRect(710, 610, 281, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Weather.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.Weather.setFont(font)
        self.Weather.setObjectName("Weather")
        self.Hour = QtWidgets.QLabel(self.centralwidget)
        self.Hour.setGeometry(QtCore.QRect(970, 540, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        self.Hour.setFont(font)
        self.Hour.setObjectName("Hour")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1100, 540, 61, 151))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.Menute = QtWidgets.QLabel(self.centralwidget)
        self.Menute.setGeometry(QtCore.QRect(1140, 530, 131, 171))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        self.Menute.setFont(font)
        self.Menute.setObjectName("Menute")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1260, 540, 61, 151))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1290, 540, 171, 151))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1492, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "视频输入"))
        self.SimLabel.setText(_translate("MainWindow", "90%"))
        self.label_3.setText(_translate("MainWindow", "相似度"))
        self.label_5.setText(_translate("MainWindow", "核验"))
        self.Right.setText(_translate("MainWindow", "成功"))
        self.Month.setText(_translate("MainWindow", "07"))
        self.label_7.setText(_translate("MainWindow", "月"))
        self.Day.setText(_translate("MainWindow", "25"))
        self.label_8.setText(_translate("MainWindow", "日"))
        self.Temp.setText(_translate("MainWindow", "25"))
        self.label_9.setText(_translate("MainWindow", "℃"))
        self.label_10.setText(_translate("MainWindow", "星期"))
        self.WeekDay.setText(_translate("MainWindow", "四"))
        self.Weather.setText(_translate("MainWindow", "多云"))
        self.Hour.setText(_translate("MainWindow", "10"))
        self.label_11.setText(_translate("MainWindow", ":"))
        self.Menute.setText(_translate("MainWindow", "10"))
        self.label_12.setText(_translate("MainWindow", ":"))
        self.label_13.setText(_translate("MainWindow", "59"))
        self.welcome.setText(_translate("MainWindow", "欢迎光临"))

        self.label_15.setText(_translate("MainWindow", "姓名:"))
        self.label_14.setText(_translate("MainWindow", "编号:"))
        self.nameinfo.setText(_translate("MainWindow", "张三"))
        self.number.setText(_translate("MainWindow", "001"))

import Resource_rc
