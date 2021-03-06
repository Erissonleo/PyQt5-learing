# -*- coding:utf-8 -*-


import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Erisson")
        # self.setWindowIcon("./icon/Arrow/CuredArrowUp.png")

        qbtn = QPushButton("退出", self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())