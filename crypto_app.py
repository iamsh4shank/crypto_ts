from operator import imod
import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit, QFileDialog, QHBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap  
import webbrowser
import cv2
from lstm import forecast_dl 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 580)
        self.crypto_name = ''
        self.model_name = ''
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(190, 20, 256, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 110, 221, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.crypto_dd = QtWidgets.QComboBox(Dialog)
        self.crypto_dd.setGeometry(QtCore.QRect(270, 110, 131, 37))
        self.crypto_dd.setObjectName("crypto_dd")
        self.crypto_dd.addItem("")
        self.crypto_dd.addItem("")
        self.crypto_dd.addItem("")
        self.crypto_dd.addItem("")
        self.crypto_dd.addItem("")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 160, 221, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.model_dd = QtWidgets.QComboBox(Dialog)
        self.model_dd.setGeometry(QtCore.QRect(270, 160, 131, 37))
        self.model_dd.setObjectName("model_dd")
        self.model_dd.addItem("")
        self.model_dd.addItem("")
        self.model_dd.addItem("")
        self.twitter_img = QtWidgets.QLabel(Dialog)
        self.twitter_img.setGeometry(QtCore.QRect(340, 290, 261, 181))
        self.twitter_img.setObjectName("twitter_img")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(330, 220, 271, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.model_img = QtWidgets.QLabel(Dialog)
        self.model_img.setGeometry(QtCore.QRect(30, 290, 261, 181))
        self.model_img.setObjectName("model_img")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 220, 261, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.log_btn = QtWidgets.QPushButton(Dialog)
        self.log_btn.setGeometry(QtCore.QRect(420, 520, 86, 37))
        self.log_btn.setObjectName("log_btn")
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(520, 520, 86, 37))
        self.exit_btn.setObjectName("exit_btn")
        self.gen_model_btn = QtWidgets.QPushButton(Dialog)
        self.gen_model_btn.setGeometry(QtCore.QRect(30, 520, 86, 37))
        self.gen_model_btn.setObjectName("gen_model_btn")
        self.gen_tw_btn = QtWidgets.QPushButton(Dialog)
        self.gen_tw_btn.setGeometry(QtCore.QRect(140, 520, 86, 37))
        self.gen_tw_btn.setObjectName("gen_tw_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.init_ui()


    def init_ui(self):
        self.crypto_dd.currentIndexChanged.connect(self.crypto_change_dd)
        self.model_dd.currentIndexChanged.connect(self.model_change_dd)
        self.gen_tw_btn.clicked.connect(self.show_t_img)
        self.gen_model_btn.clicked.connect(self.show_m_img)
        self.exit_btn.clicked.connect(self.on_click)


    def crypto_change_dd(self, i):
        self.crypto_name = self.crypto_dd.currentText()

    def model_change_dd(self, i):
        self.model_name = self.model_dd.currentText()

    @pyqtSlot()
    def show_m_img(self):
        crypto_code = ''
        if (self.crypto_name == 'Bitcoin'):
            crypto_code = 'BTC'
        elif (self.crypto_name == 'XRP'):
            crypto_code = 'XRP'
        elif (self.crypto_name == 'Dogecoin'):
            crypto_code = 'DOGE'
        elif (self.crypto_name == 'Tether'):
            crypto_code = 'USDT'
        elif (self.crypto_name == 'Ethereum'):
            crypto_code = 'ETH'

        if (self.model_name == 'Deep Learning'):
            forecast_dl(f'?fsym={crypto_code}&tsym=CAD&limit=700',self.crypto_name)
            file_name = f'plots/{self.crypto_name}_m.png'

        elif (self.model_name == 'ARIMA'):
            file_name = f'plots/arima/{crypto_code}.png'

        #print (f"plots/{crypto}_m.png")
        pixmap = QPixmap(file_name)
        #pixmap2 = pixmap.scaledToWidth(100)
        #pixmap3 = pixmap.scaledToHeight(400)
        self.model_img.setPixmap(pixmap)
        self.model_img.setScaledContents(True)
        self.showImg(file_name)

    @pyqtSlot()
    def show_t_img(self):
        file_name = f'plots/{self.crypto_name}.png'
        print (file_name)
        pixmap = QPixmap(file_name)
        #pixmap2 = pixmap.scaledToWidth(100)
        #pixmap3 = pixmap.scaledToHeight(400)
        self.twitter_img.setPixmap(pixmap)
        self.twitter_img.setScaledContents(True)
        self.showImg(file_name)
            
    def showImg(self, img ):
        hbox = QHBoxLayout(self)                                                                                                           
        pixmap = QPixmap(img)                                                                                                        

        lbl = QLabel(self)                                                                                                                 
        lbl.setPixmap(pixmap)                                                                                                              

        hbox.addWidget(lbl)                                                                                                                
        self.setLayout(hbox)                                                                                                               

        self.move(300, 200)                                                                                                                
        self.setWindowTitle('Image with PyQt')                                                                                             
        self.show() 


    @pyqtSlot()
    def on_click(self):
        sys.exit()



















    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Garuda\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cryptocurency Analyser</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Garuda\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the crypto currency</p></body></html>"))
        self.crypto_dd.setItemText(0, _translate("Dialog", "Bitcoin"))
        self.crypto_dd.setItemText(1, _translate("Dialog", "Ethereum"))
        self.crypto_dd.setItemText(2, _translate("Dialog", "XRP"))
        self.crypto_dd.setItemText(3, _translate("Dialog", "Tether"))
        self.crypto_dd.setItemText(4, _translate("Dialog", "Dogecoin"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Garuda\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the Forecasting model</p></body></html>"))
        self.model_dd.setItemText(0, _translate("Dialog", "ARIMA"))
        self.model_dd.setItemText(2, _translate("Dialog", "Deep Learning"))
        self.twitter_img.setText(_translate("Dialog", "Image..."))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Garuda\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Twitter based results</p></body></html>"))
        self.model_img.setText(_translate("Dialog", "Image..."))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Garuda\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Model Based Result</p></body></html>"))
        self.log_btn.setText(_translate("Dialog", "Save Log"))
        self.exit_btn.setText(_translate("Dialog", "Exit"))
        self.gen_model_btn.setText(_translate("Dialog", "Model"))
        self.gen_tw_btn.setText(_translate("Dialog", "Twitter"))

