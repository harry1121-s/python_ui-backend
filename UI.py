# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spd_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from control import DAC_Control
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QDial, QDialog, QLCDNumber,
    QLabel, QPushButton, QSizePolicy, QWidget)
from PyQt5 import QtWidgets

class Ui_main_screen(object):

    def __init__(self):
        self.control = DAC_Control(115200)
    
    def setupUi(self, main_screen):
        if not main_screen.objectName():
            main_screen.setObjectName(u"main_screen")
        main_screen.resize(612, 549)
        main_screen.setAutoFillBackground(False)
        main_screen.setStyleSheet(u"background-color: rgb(9, 8, 22);")

        # self.control = DAC_Control(115200)
        
        self.dial = QDial(main_screen)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(60, 130, 131, 141))
        self.dial.setRange(0,1000)
        self.dial.setStyleSheet(u"background-color: rgb(234, 247, 237);")
        self.lcdNumber = QLCDNumber(main_screen)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(60, 60, 121, 51))
        self.lcdNumber.smallDecimalPoint()
        self.lcdNumber.setStyleSheet(u"background-color: rgb(179, 227, 234);")
        self.lcdNumber_2 = QLCDNumber(main_screen)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(360, 60, 121, 51))
        self.lcdNumber_2.smallDecimalPoint()
        self.lcdNumber_2.setStyleSheet(u"background-color: rgb(179, 227, 234);")
        self.dial_2 = QDial(main_screen)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setGeometry(QRect(360, 130, 131, 141))
        self.dial_2.setRange(0,1000)
        self.dial_2.setStyleSheet(u"background-color: rgb(234, 247, 237);")
        self.label = QLabel(main_screen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 90, 41, 21))
        self.label.setStyleSheet(u"background-color: rgb(179, 227, 234);")
        self.pushButton = QPushButton(main_screen)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 10, 100, 32))
        self.pushButton.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_2 = QPushButton(main_screen)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(370, 10, 100, 32))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_3 = QPushButton(main_screen)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 340, 131, 51))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_4 = QPushButton(main_screen)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(350, 340, 131, 51))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_5 = QPushButton(main_screen)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 410, 131, 51))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_6 = QPushButton(main_screen)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(350, 410, 131, 51))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_7 = QPushButton(main_screen)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(70, 490, 131, 51))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.pushButton_8 = QPushButton(main_screen)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(350, 490, 131, 51))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(204, 239, 200);\n"
"")
        self.label_3 = QLabel(main_screen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 90, 41, 21))
        self.label_3.setStyleSheet(u"background-color: rgb(179, 227, 234);")

        self.retranslateUi(main_screen)
        self.dial.valueChanged.connect(lambda: self.dec2Volts_dac1())
        self.dial_2.valueChanged.connect(lambda: self.dec2Volts_dac2())
        self.pushButton.clicked.connect(lambda: self.dac1_write())
        self.pushButton_2.clicked.connect(lambda: self.dac2_write())

        QMetaObject.connectSlotsByName(main_screen)
    # setupUi


    def retranslateUi(self, main_screen):
        main_screen.setWindowTitle(QCoreApplication.translate("main_screen", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("main_screen", u"Volts", None))
        self.pushButton.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("main_screen", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("main_screen", u"Volts", None))
    # retranslateUi

    def dec2Volts_dac1(self):
        lcd_value = self.dial.value()*1.185/1000
        self.lcdNumber.display(lcd_value)
    
    def dec2Volts_dac2(self):
        lcd_value = self.dial_2.value()*3.300/1000
        self.lcdNumber_2.display(lcd_value)

    def dac1_write(self):
        # val = self.dial.value()
        frame_value = int(self.dial.value()*4095/1000)
        result = self.control.dacWrite(0,1,frame_value)
        print(self.dial.value())
    
    def dac2_write(self):
        frame_value = int(self.dial_2.value()*4095/1000)
        result = self.control.dacWrite(0,2,frame_value)
        print(self.dial_2.value())

    

def init(self, parent=None):

        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

   

#     fig1 = Figure()


Dialog = type("Dialog", (QtWidgets.QDialog, Ui_main_screen), {"__init__": init})

 

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    Dialog().exec_()