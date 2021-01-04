# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class SimpleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪")
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("简单窗口")
        self.show()


class SimpleWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪")
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("简单窗口，带菜单栏")

        exitAct = QAction(QIcon("./src/icons/image-file.svg"),
        "退出(&E)", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("退出程序")
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("文件(&F)")
        fileMenu.addAction(exitAct)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # simple_window = SimpleWindow()
    simple_window2 = SimpleWindow2()
    sys.exit(app.exec_())

