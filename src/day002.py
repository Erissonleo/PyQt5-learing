# -*- coding:utf-8 -*-

'''
simple windows 
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500,300)
    w.move(300, 300)
    w.setWindowTitle("My First Window")
    w.show()

    sys.exit(app.exec_())