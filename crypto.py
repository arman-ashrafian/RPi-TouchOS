# -*- coding: UTF-8 -*-

# Form implementation generated from reading ui file '.\ui\crypto.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Crypto(object):
    def setupUi(self, Crypto):
        Crypto.setObjectName("Crypto")
        Crypto.resize(800, 480)
        Crypto.setMinimumSize(QtCore.QSize(800, 480))
        Crypto.setStyleSheet("* {\n"
"    background: #191919;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: black;\n"
"    font-size: 30pt;\n"
"}\n"
"\n"
"QPushButton#button_back {\n"
"    font-size: 12pt;\n"
"    background-color: #1565C0;\n"
"}\n"
"\n"
"QLabel#label_eth {\n"
"    color: #ECF0F1;\n"
"    font-size: 40pt;\n"
"    background-color: #3C3C3D;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #ECF0F1;\n"
"    font-size: 30pt;\n"
"}\n"
"\n"
"QLabel#label_btc {\n"
"    color: #ECF0F1;\n"
"    font-size: 40pt;\n"
"    background-color: #FF9900;\n"
"}\n"
"\n"
"QLabel#label_ethbalance {\n"
"    color: #448AFF;\n"
"}\n"
"\n"
"\n"
"")
        self.button_back = QtWidgets.QPushButton(Crypto)
        self.button_back.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.button_back.setObjectName("button_back")
        self.label = QtWidgets.QLabel(Crypto)
        self.label.setGeometry(QtCore.QRect(40, 310, 124, 49))
        self.label.setObjectName("label")
        self.label_eth = QtWidgets.QLabel(Crypto)
        self.label_eth.setGeometry(QtCore.QRect(20, 80, 191, 61))
        self.label_eth.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eth.setObjectName("label_eth")
        self.label_btc = QtWidgets.QLabel(Crypto)
        self.label_btc.setGeometry(QtCore.QRect(20, 200, 191, 61))
        self.label_btc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_btc.setObjectName("label_btc")
        self.widget = QtWidgets.QWidget(Crypto)
        self.widget.setGeometry(QtCore.QRect(250, 70, 511, 91))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_eth_price = QtWidgets.QLabel(self.widget)
        self.label_eth_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eth_price.setObjectName("label_eth_price")
        self.horizontalLayout.addWidget(self.label_eth_price)
        self.label_eth_delta = QtWidgets.QLabel(self.widget)
        self.label_eth_delta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eth_delta.setObjectName("label_eth_delta")
        self.horizontalLayout.addWidget(self.label_eth_delta)
        self.widget1 = QtWidgets.QWidget(Crypto)
        self.widget1.setGeometry(QtCore.QRect(243, 190, 521, 81))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_btc_price = QtWidgets.QLabel(self.widget1)
        self.label_btc_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_btc_price.setObjectName("label_btc_price")
        self.horizontalLayout_2.addWidget(self.label_btc_price)
        self.label_btc_delta = QtWidgets.QLabel(self.widget1)
        self.label_btc_delta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_btc_delta.setObjectName("label_btc_delta")
        self.horizontalLayout_2.addWidget(self.label_btc_delta)
        self.widget2 = QtWidgets.QWidget(Crypto)
        self.widget2.setGeometry(QtCore.QRect(320, 310, 311, 121))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_ethbalance = QtWidgets.QLabel(self.widget2)
        self.label_ethbalance.setObjectName("label_ethbalance")
        self.verticalLayout.addWidget(self.label_ethbalance)
        self.label_usdbalance = QtWidgets.QLabel(self.widget2)
        self.label_usdbalance.setObjectName("label_usdbalance")
        self.verticalLayout.addWidget(self.label_usdbalance)

        self.retranslateUi(Crypto)
        QtCore.QMetaObject.connectSlotsByName(Crypto)

    def retranslateUi(self, Crypto):
        _translate = QtCore.QCoreApplication.translate
        Crypto.setWindowTitle(_translate("Crypto", "Form"))
        self.button_back.setText(_translate("Crypto", "BACK"))
        self.label.setText(_translate("Crypto", "Wallet:"))
        self.label_eth.setText(_translate("Crypto", "ETH"))
        self.label_btc.setText(_translate("Crypto", "BTC"))
        self.label_eth_price.setText(_translate("Crypto", "$800"))
        self.label_eth_delta.setText(_translate("Crypto", "(+10.0%)"))
        self.label_btc_price.setText(_translate("Crypto", "$13,000"))
        self.label_btc_delta.setText(_translate("Crypto", "(+12.0%)"))
        self.label_ethbalance.setText(_translate("Crypto", "6.604 ETH"))
        self.label_usdbalance.setText(_translate("Crypto", "$7,000"))

