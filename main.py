import sys
import serial
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class ButtonClickGui(QMainWindow):
    def __init__(self):
        super(ButtonClickGui,self).__init__()
        uic.loadUi("main.ui", self)
        self.startButton.clicked.connect(self.LEDon)
        self.stopButton.clicked.connect(self.LEDoff)
        self.arduino = serial.Serial('COM6', 9600) 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_data)
        self.timer.start(100)  


    def LEDon(self):
        self.arduino.write(b'1')  

    def LEDoff(self):
        self.arduino.write(b'0')  

    def read_data(self):
        if self.arduino.in_waiting > 0:
            distance = self.arduino.readline().decode().strip()
            self.label_4.setText(f'{distance} cm')


app = QApplication([])
mainwindow = ButtonClickGui()
widget = QStackedWidget()
widget.addWidget(mainwindow)
widget.showFullScreen
widget.setFixedHeight(900)
widget.setFixedWidth(800)
widget.show()
app.exec()

#End 