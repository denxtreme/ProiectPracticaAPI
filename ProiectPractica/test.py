# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import PrelucrareData


import requests


from PySide6.QtCore import (QCoreApplication,
    QMetaObject,QRect,
    QSize, QUrl)
from PySide6.QtGui import (QDesktopServices,QPixmap,)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,QStackedWidget, QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget,NrStackedWidgets,PrelucrareDataOBJ):
        self.butoane = []
        self.butoaneLink = []
        self.APIdata=PrelucrareDataOBJ


        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1051, 704)
        Widget.setMinimumSize(QSize(1051, 704))
        Widget.setMaximumSize(QSize(1051, 704))

        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setGeometry(QRect(170, 60, 881, 651))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(145, 0, 0);")


        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3=self.DefineButton(self.pushButton_3,"pushButton_3",730, 590, 111, 29,"background-color: rgb(255, 255, 255);","Widget","Next Article")
        self.pushButton_3.clicked.connect(self.ShowNextPage)


        self.pushButtonLink=QPushButton(self.page)
        self.pushButtonLink=self.DefineButton(self.pushButtonLink,"pushButtonLink",20,285,111,29,"background-color: rgb(255, 255, 255);","Widget","Open Article")
        self.pushButtonLink.clicked.connect(lambda: self.open_link(self.APIdata.Vector_CArticol[0].url))


        self.label_2 = QLabel(self.page)
        self.label_2=self.DefineLabel(self.label_2,"label_2",450, 40, 381, 211,self.WriteINFOArticle(self.APIdata.Vector_CArticol[0]))


        self.label_3 = QLabel(self.page)
        self.label_3=self.DefineLabel(self.label_3,"label_3",30, 310, 701, 291,self.WRITEdescArticle(self.APIdata.Vector_CArticol[0]))


        self.label_4 = QLabel(self.page)
        self.label_4=self.DefineLabel(self.label_4,"label_4",20, 20, 400, 250,"")

        #####Afiseaza imaginea articolului
        self.DisplayImageArticle(self.label_4,0)        



        for i in range(1,NrStackedWidgets-1):
            widgetNou = QWidget()
            widgetNou.setObjectName(u"page"+str(i))
            self.stackedWidget.addWidget(widgetNou) 

            Label2=QLabel(widgetNou)
            Label2=self.DefineLabel(Label2,"label_2",450, 40, 381, 211,self.WriteINFOArticle(self.APIdata.Vector_CArticol[i]))

            Label3=QLabel(widgetNou)
            Label3=self.DefineLabel(Label3,"label_3",30, 310, 701, 281,self.WRITEdescArticle(self.APIdata.Vector_CArticol[i]))

            Label4=QLabel(widgetNou)
            Label4=self.DefineLabel(Label4,"label_4",20, 20, 400, 250,"")
           
            #####Afiseaza imaginea articolului
            self.DisplayImageArticle(Label4,i)

           
            pushButtonLink=QPushButton(widgetNou)
            pushButtonLink=self.DefineButton(pushButtonLink,"pushButtonLink",20,285,111,29,"background-color: rgb(255, 255, 255);","Widget","Open Article")
            self.butoaneLink.append(pushButtonLink)


            pushButton = QPushButton(widgetNou)
            pushButton=self.DefineButton(pushButton,"pushButton"+str(2*i),730, 590, 111, 29,"background-color: rgb(255, 255, 255);","Widget","Next Article")            
            pushButton2 = QPushButton(widgetNou)
            pushButton2=self.DefineButton(pushButton2,"pushButton"+str(2*i+1),60, 590, 111, 29,"background-color: rgb(255, 255, 255);","Widget","Prev Article")
            self.butoane.append(pushButton)
            self.butoane.append(pushButton2)

             
               
        widgetNou3= QWidget()
        widgetNou3.setObjectName(u"page"+str(NrStackedWidgets-1))
        self.stackedWidget.addWidget(widgetNou3)


        self.pushButtonNou3 = QPushButton(widgetNou3)
        self.pushButtonNou3=self.DefineButton(self.pushButtonNou3,"pushButton"+str(2*NrStackedWidgets),60, 590, 111, 29,"background-color: rgb(255, 255, 255);","Widget","Prev Article")
        self.pushButtonNou3.clicked.connect(self.ShowPrevPage)

        self.pushButtonLink2=QPushButton(widgetNou3)
        self.pushButtonLink2=self.DefineButton(self.pushButtonLink2,"pushButtonLink",20, 285, 111, 29,"background-color: rgb(255, 255, 255);","Widget","Open Article")
        self.pushButtonLink2.clicked.connect(lambda: self.open_link(self.APIdata.Vector_CArticol[len(self.APIdata.Vector_CArticol)-1].url))


        self.label_2Last = QLabel(widgetNou3)
        self.label_2Last=self.DefineLabel(self.label_2Last,"label_2",460, 40, 380, 230,self.WriteINFOArticle(self.APIdata.Vector_CArticol[len(self.APIdata.Vector_CArticol)-1]))

        self.label_3Last = QLabel(widgetNou3)
        self.label_3Last=self.DefineLabel(self.label_3Last,"label_3",30, 310, 701, 281,self.WRITEdescArticle(self.APIdata.Vector_CArticol[len(self.APIdata.Vector_CArticol)-1]))

        self.label_4Last = QLabel(widgetNou3)
        self.label_4Last=self.DefineLabel(self.label_4Last,"label_4",20, 20, 400, 250,"")



        #####Afiseaza imaginea articolului
        self.DisplayImageArticle(self.label_4Last,len(self.APIdata.Vector_CArticol)-1)


        self.widget = QWidget(Widget)
        self.widget=self.DefineWidget(self.widget,"widget",-11,60,181,651,"background-color: rgb(85, 85, 255);\n""background-color: rgb(140, 0, 0);")

        self.widget_2 = QWidget(Widget)
        self.widget_2=self.DefineWidget(self.widget_2,"widget_2",0, -10, 1101, 71,"background-color: rgb(0, 0, 0);")


        self.frame = QFrame(self.widget)
        self.frame=self.DefineFrame(self.frame,"frame",30,100,150,120,"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")     

        self.frame_2 = QFrame(self.widget)
        self.frame_2=self.DefineFrame(self.frame_2,"frame_2",30,380,150,120,"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0,169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        


        self.pushButton = QPushButton(self.widget_2)
        self.pushButton=self.DefineButton(self.pushButton,"pushButton",20,20,51,41,"background-color: rgb(0, 0, 0);","","")


        for i in range(0,NrStackedWidgets-2):
            self.butoane[2*i+1].clicked.connect(self.ShowPrevPage)
            self.butoane[2*i].clicked.connect(self.ShowNextPage)
            self.butoaneLink[i].clicked.connect(lambda: self.open_link(self.APIdata.Vector_CArticol[len(self.APIdata.Vector_CArticol)-1].url))       


        self.label = QLabel(self.widget_2)
        self.label=self.DefineLabel(self.label,"label",180,20,691,41,"")


        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

        
    # setupUi

    def retranslateUi(self, Widget):
        _translate = QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic; color:#ffffff;\">Cele mai sigure stiri din intreaga tara! Siguranta si incredere!</span></p></body></html>", None))
    # retranslateUi

    def ShowNextPage(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(current_index + 1)

    def ShowPrevPage(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index > 0:
            self.stackedWidget.setCurrentIndex(current_index - 1)
    
    def WriteINFOArticle(self,CCarticol):
        return CCarticol.PresentArticols()
    def WRITEdescArticle(self,CCarticol):
        return CCarticol.PresentArticolsDesc()
    
    def open_link(self,url2):
        currentIndex=self.stackedWidget.currentIndex()
        url=self.APIdata.Vector_CArticol[currentIndex].url
        QDesktopServices.openUrl(QUrl(url))

    def display_image(self,label,image_url):
        response = requests.get(image_url)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)   
        if pixmap.isNull():
            response = requests.get("https://www.raynaudsdisease.com/user/products/large/image-unavailable-rd-2019.png")
            pixmap = QPixmap()
            pixmap.loadFromData(response.content) 
            return
        scaled_pixmap = pixmap.scaled(label.size())
        label.setPixmap(scaled_pixmap)

    def DefineButton(self,button,name,x,y,length,width,stylesheet,NumeSetTexT,text):
        button.setObjectName(name)
        button.setGeometry(QRect(x, y, length, width))
        button.setStyleSheet(stylesheet)
        button.setText(QCoreApplication.translate(NumeSetTexT, text, None))
        return button
    
    def DefineLabel(self,Label,name,x,y,length,width,text):
        Label.setGeometry(QRect(x, y, length, width))
        Label.setObjectName(name)
        Label.setText(text)
        return Label
    
    def DefineFrame(self,Frame,name,x,y,length,width,styleSheet):
        Frame.setObjectName(name)
        Frame.setGeometry(QRect(x, y, length, width))
        Frame.setStyleSheet(styleSheet)
        Frame.setFrameShape(QFrame.StyledPanel)
        Frame.setFrameShadow(QFrame.Raised)
        return Frame
    
    def DefineWidget(self,Widget,name,x,y,length,width,styleSheet):
        Widget.setObjectName(name)
        Widget.setGeometry(QRect(x,y,length,width))
        Widget.setStyleSheet(styleSheet)
        return Widget
    
    
    def DisplayImageArticle(self,Label,index_CArticle):
        self.display_image(Label,"https://www.raynaudsdisease.com/user/products/large/image-unavailable-rd-2019.png")
        if self.APIdata.Vector_CArticol[index_CArticle].urlToImage != "null" and self.APIdata.Vector_CArticol[index_CArticle].urlToImage != ":null" :
            if not ".gif" in self.APIdata.Vector_CArticol[index_CArticle].urlToImage :
                self.display_image(Label,self.APIdata.Vector_CArticol[index_CArticle].urlToImage)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self,10)
import sys




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Widget = QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget,7)
    
    Widget.show()
    sys.exit(app.exec())

