##IMPORTING REQUIRED LIBRARIES
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from subprocess import call
import cv2
import copy
import os
import urllib.request
import cv2

#Global Variables
x1,y1 = 20,80
x2,y2 = 400,80
w = 200
numbers = ["0","1","2","3","4","5","+"]

## MAIN WINDOW CLASS
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.control_bt1.clicked.connect(self.Gesture_rgn)
        self.ui.control_bt2.clicked.connect(self.Digit_rgn)
        self.ui.control_bt3.clicked.connect(self.takedata)

    ## RUNNING THE Hand Written SCRIPT
    def Digit_rgn(self):
        print("Loading Hand Written Digit Recognition System...")
        call(["python","digitrecognition.py"])
    ##RUNNING THE Create Dataset SCRIPT
    def takedata(self):
        call(["python","takedata.py"])
    ##RUNNING THE Gesture Recognition SCRIPT
    def Gesture_rgn(self):
        call(["python","1project.py"])

## CLASS FOR SETTING THE ALIGNMENT OF WIDGETS
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        ##setting the dimensions of the application
        Form.resize(800, 500)
        self.bg = QtWidgets.QLabel(Form)     ##bg is the main window inside the application
        self.bg.setObjectName("bg")
        self.bg.setGeometry(0,0,800,500)    ##set the placement and size of bg window
        self.bg.setStyleSheet("QLabel {image: url(../Images/background.png)}")   ##set background image
        self.control_bt1 = QtWidgets.QPushButton(Form)  ##Hand Written  RGN button
        self.control_bt1.setGeometry(40,150,200,200)     ##setting the placement and size in the main window
        self.control_bt1.setStyleSheet("QPushButton {image: url(../Images/bt_1_black.png)}"      ##formatting the button
                                        "QPushButton {border-radius: 10px}"
                                        "QPushButton {background-color: black}"
                                        "QPushButton:pressed {image: url(../Images/bt_1_b_green.png)}"
                                        "QPushButton:hover:!pressed {image: url(../Images/bt_1_grey.png)}")
        self.control_bt2 = QtWidgets.QPushButton(Form)   ##Gesture RGN button
        self.control_bt2.setGeometry(300,150,200,200)    ##setting the placement and size in the main window
        self.control_bt2.setStyleSheet("QPushButton {image: url(../Images/bt_2_black.png)}"   ##formatting the button
                                        "QPushButton {border-radius: 10px}"
                                        "QPushButton {background-color: black}"
                                        "QPushButton:pressed {image: url(../Images/bt_2_b_green.png)}"
                                        "QPushButton:hover:!pressed {image: url(../Images/bt_2_grey.png)}")
        self.control_bt3 = QtWidgets.QPushButton(Form)    ##Create dataset button
        self.control_bt3.setGeometry(560,150,200,200)       ##setting the placement and size in the main window
        self.control_bt3.setStyleSheet("QPushButton {image: url(../Images/bt_3_black.png)}"     ##formatting the button
                                        "QPushButton {border-radius: 10px}"
                                        "QPushButton {background-color: black}"
                                        "QPushButton:pressed {image: url(../Images/bt_3_b_green.png)}"
                                        "QPushButton:hover:!pressed {image: url(../Images/bt_3_grey.png)}")

        self.members = QtWidgets.QLabel(Form)
        self.members.setText("<font color='green' size = 5 face = 'arial'>Members : </font>");
        self.members.setStyleSheet("QLabel{background-color:black}")
        self.members.setGeometry(40,350,350,40)

        self.logo = QtWidgets.QLabel(Form)
        self.logo.setStyleSheet("QLabel {image: url(../Images/kiitlogo.png)}")
        self.logo.setGeometry(650,10,100,100)

        self.text_area1 = QtWidgets.QLabel(Form)
        ##self.text_area.setText = "lol"
        self.text_area1.setText("<font color='white' size = 5 face = 'arial'>Anand Kumar&nbsp;&nbsp;&nbsp;Anish Hota&nbsp;&nbsp;&nbsp;Champak Sinha</font>");
        self.text_area1.setStyleSheet("QLabel{background-color:black}")
        self.text_area1.setGeometry(40,380,500,40)

        self.text_area2 = QtWidgets.QLabel(Form)
        self.text_area2.setText("<font color='white' size = 5 face = 'arial'>Pranesh Biswas&nbsp;&nbsp;&nbsp;Rishab</font>");
        self.text_area2.setStyleSheet("QLabel{background-color:black}")
        self.text_area2.setGeometry(40,410,350,40)

        self.text_area3 = QtWidgets.QLabel(Form)
        self.text_area3.setText("<font color='green' size = 5 face = 'arial'>Guide : Prof. Sushruta Mishra</font>");
        self.text_area3.setStyleSheet("QLabel{background-color:black}")
        self.text_area3.setGeometry(40,440,350,40)


        self.retranslateUi(Form)


    def retranslateUi(self, Form):
        translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(translate("Form", "Digit Recognition System"))


## MAIN FUNCTION RUNNING THE APPLICATION
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.setFixedSize(800,500)

    sys.exit(app.exec_())
