# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 542)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.button_on = QtWidgets.QPushButton(self.centralWidget)
        self.button_on.setGeometry(QtCore.QRect(150, 180, 141, 101))
        self.button_on.setStyleSheet("QPushButton {\n"
"    background-color: green;\n"
"}")
        self.button_on.setObjectName("button_on")
        self.button_off = QtWidgets.QPushButton(self.centralWidget)
        self.button_off.setGeometry(QtCore.QRect(390, 180, 141, 101))
        self.button_off.setStyleSheet("QPushButton {\n"
"    background-color: red\n"
"}")
        self.button_off.setObjectName("button_off")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_on.setText(_translate("MainWindow", "ON"))
        self.button_off.setText(_translate("MainWindow", "OFF"))

