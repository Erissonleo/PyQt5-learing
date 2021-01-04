# -*- coding:utf-8 -*-


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication

class SigSlog(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("XXOO")
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)

        slider.valueChanged.connect(lcd.display)
        self.resize(350, 250)


app = QApplication(sys.argv)
qb = SigSlog()
qb.show()
sys.exit(app.exec_())