# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject

# 自定义信号
class Signal(QObject):
    showmouse = pyqtSignal()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("自定义信号")

        self.s = Signal()
        self.s.showmouse.connect(self.about)

        self.show()

    def about(self):
        QMessageBox.about(self, "鼠标", "你点鼠标了")

    # 发送自定义信号
    def mousePressEvent(self, event):
        self.s.showmouse.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())