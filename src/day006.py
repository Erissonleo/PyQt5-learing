# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400 ,400)
        self.setWindowTitle("布局")

        bt1 = QPushButton("剪刀", self)
        bt2 = QPushButton("石头", self)
        bt3 = QPushButton("布", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("计算器界面")

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(4, 9) for j in range(0, 4)]
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender().text()
        ls = ["/", "*", "+", "-"]
        if sender in ls:
            self.lcd.display("not defined")
        else:
            self.lcd.display(sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())