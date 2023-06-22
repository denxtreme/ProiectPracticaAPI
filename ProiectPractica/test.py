# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget,NrStackedWidgets):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1001, 634)
        Widget.setMinimumSize(QSize(1001, 634))
        Widget.setMaximumSize(QSize(1001, 634))
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(170, 60, 841, 581))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(145, 0, 0);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(662, 490, 111, 29))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 200, 221, 20))
        self.stackedWidget.addWidget(self.page)

        for i in range(1,NrStackedWidgets-1):
            widgetNou = QWidget()
            widgetNou.setObjectName(u"page"+str(i))
            pushButton = QPushButton(widgetNou)
            pushButton.setObjectName(u"pushButton_4"+str(2*i))
            pushButton.setGeometry(QRect(680, 500, 111, 29))
            pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            pushButton2 = QPushButton(widgetNou)
            pushButton2.setObjectName(u"pushButton_4"+str(2*i+1))
            pushButton2.setGeometry(QRect(60, 500, 111, 29))
            pushButton2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.stackedWidget.addWidget(widgetNou)      
        widgetNou3= QWidget()
        widgetNou3.setObjectName(u"page"+str(NrStackedWidgets-1))
        pushButtonNou3 = QPushButton(widgetNou3)
        pushButtonNou3.setObjectName(u"pushButton"+str(2*NrStackedWidgets))
        pushButtonNou3.setGeometry(QRect(60, 500, 111, 29))
        pushButtonNou3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(widgetNou3)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-11, 60, 181, 581))
        self.widget.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"background-color: rgb(140, 0, 0);")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 100, 120, 80))
        self.frame.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 240, 131, 51))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 380, 120, 80))
        self.frame_2.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(Widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, -10, 1001, 71))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 51, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        icon = QIcon()
        icon.addFile(u"Resources/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(35, 35))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 691, 41))
        

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Next Article", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Next Article", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"Prev Article", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"Next Article", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"Prev Article", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"Prev Article", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Insert new API", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#ffffff;\">Cele mai sigure stiri din intreaga tara! Siguranta si incredere!</span></p></body></html>", None))
    # retranslateUi

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self,10)
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
