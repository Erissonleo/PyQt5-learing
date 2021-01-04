# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QLCDNumber, QWidget, QDial, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen


class Dial(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("拨号")

        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)

        dial.valueChanged.connect(lcd.display)

        self.show()


class Arrow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Arrow")

        self.lab = QLabel("方向", self)
        self.lab.setGeometry(150 ,100, 50, 50)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText("↑")
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')


class MouseMove(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle("鼠标移动")
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)
        self.label.setText(f"坐标：(x:{event.x()}, y:{event.y()})" + f"离中心点距离:{distance_from_center}")
        self.pos = event.pos()
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())



if __name__ == "__main__":
    # 拨号界面
    # app_dial = QApplication(sys.argv)
    # dial = Dial()
    # sys.exit(app_dial.exec_())
    # 方向显示界面
    # app = QApplication(sys.argv)
    # arrow = Arrow()
    # sys.exit(app.exec_())
    # 鼠标事件
    app = QApplication(sys.argv)
    ex = MouseMove()
    sys.exit(app.exec_())
