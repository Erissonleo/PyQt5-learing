# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("表单")

        formlayout = QFormLayout()
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")

        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)
        self.setLayout(formlayout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
