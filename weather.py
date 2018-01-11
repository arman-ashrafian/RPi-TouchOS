# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\weather.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(800, 480)
        Weather.setMinimumSize(QtCore.QSize(800, 480))
        Weather.setStyleSheet("* {\n"
"    background: #64B5F6;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: black;\n"
"    font-size: 20pt;\n"
"}\n"
"\n"
"QPushButton#button_back {\n"
"    font-size: 12pt;\n"
"    background-color: #1565C0\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QLabel#label_temp {\n"
"    font-size: 45pt;\n"
"}\n"
"\n"
"QLabel#label_status,#label_city {\n"
"    font-size: 30pt;\n"
"}")
        self.button_back = QtWidgets.QPushButton(Weather)
        self.button_back.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.button_back.setObjectName("button_back")
        self.label_city = QtWidgets.QLabel(Weather)
        self.label_city.setGeometry(QtCore.QRect(210, 40, 341, 81))
        self.label_city.setAlignment(QtCore.Qt.AlignCenter)
        self.label_city.setObjectName("label_city")
        self.label_icon = QtWidgets.QLabel(Weather)
        self.label_icon.setGeometry(QtCore.QRect(430, 150, 91, 81))
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap("weather icons/01d.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.label_temp = QtWidgets.QLabel(Weather)
        self.label_temp.setGeometry(QtCore.QRect(230, 150, 181, 71))
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.label_status = QtWidgets.QLabel(Weather)
        self.label_status.setGeometry(QtCore.QRect(230, 250, 321, 51))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.label = QtWidgets.QLabel(Weather)
        self.label.setGeometry(QtCore.QRect(250, 330, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Weather)
        self.label_2.setGeometry(QtCore.QRect(250, 380, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Weather)
        self.label_3.setGeometry(QtCore.QRect(250, 430, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_max_temp = QtWidgets.QLabel(Weather)
        self.label_max_temp.setGeometry(QtCore.QRect(420, 330, 111, 31))
        self.label_max_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_max_temp.setObjectName("label_max_temp")
        self.label_min_temp = QtWidgets.QLabel(Weather)
        self.label_min_temp.setGeometry(QtCore.QRect(420, 380, 111, 31))
        self.label_min_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_min_temp.setObjectName("label_min_temp")
        self.label_humidity = QtWidgets.QLabel(Weather)
        self.label_humidity.setGeometry(QtCore.QRect(420, 430, 111, 31))
        self.label_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humidity.setObjectName("label_humidity")

        self.retranslateUi(Weather)
        QtCore.QMetaObject.connectSlotsByName(Weather)

    def retranslateUi(self, Weather):
        _translate = QtCore.QCoreApplication.translate
        Weather.setWindowTitle(_translate("Weather", "Form"))
        self.button_back.setText(_translate("Weather", "BACK"))
        self.label_city.setText(_translate("Weather", "City Name"))
        self.label_temp.setText(_translate("Weather", "60"))
        self.label_status.setText(_translate("Weather", "Sunny"))
        self.label.setText(_translate("Weather", "Max:"))
        self.label_2.setText(_translate("Weather", "Min:"))
        self.label_3.setText(_translate("Weather", "Humidity:"))
        self.label_max_temp.setText(_translate("Weather", "65"))
        self.label_min_temp.setText(_translate("Weather", "55"))
        self.label_humidity.setText(_translate("Weather", "2%"))

