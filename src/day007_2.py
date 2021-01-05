# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QMenu, qApp, QAction, QApplication, QTextEdit, QFormLayout, QLabel
from PyQt5.QtGui import QIcon


class Example1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("准备就绪")
        
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("带子菜单的窗口")

        extiAct = QAction(QIcon("./src/icons/exit.png"), "退出(&E)", self)
        extiAct.setShortcut("Ctrl+Q")
        extiAct.setToolTip("退出程序")
        extiAct.triggered.connect(qApp.quit)

        saveMenu = QMenu("保存方式(&S)", self)
        saveAct = QAction(QIcon("./src/icons/save.png"), "保存...", self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.setStatusTip("保存文件")
        saveAsAct = QAction(QIcon("src/icons/save-as.png"), "另存为...", self)
        saveAsAct.setStatusTip("文件另存为")
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveAsAct)

        newAct = QAction(QIcon("./src/icons/file.svg"), "新建(&N)", self)
        newAct.setShortcut("Ctrl+N")

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(extiAct)     
        
        self.show()


class Example2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("带上下文的窗口")
        self.statusBar().showMessage("准备就绪")

        saveMenu = QMenu("保存方式...", self)
        saveAct = QAction(QIcon("./src/icons/save.png"), "保存...", self)
        saveAct.setShortcut("Ctrl+S")
        saveAct.setStatusTip("保存文件")
        saveAsAct = QAction(QIcon("src/icons/save-as.png"), "另存为...", self)
        saveAsAct.setStatusTip("文件另存为")
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveAsAct)

        exitAct = QAction(QIcon("./src/icons/exit.png"), "退出(&E)", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setToolTip("退出程序")
        exitAct.triggered.connect(qApp.quit)

        newAct = QAction(QIcon("./src/icons/file.svg"), "新建(&N)", self)
        newAct.setShortcut("Ctrl+N")
        newAct.setStatusTip("新建文件")

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("文件(&F)")
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        # 增加工具栏
        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)  
        toolbar.addAction(saveAct)
        toolbar.addAction(saveAsAct)

        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction(QIcon("./src/icons/file.svg"), "新建")
        savaAct = cmenu.addAction(QIcon("./src/icons/save.png"), "保存")
        exitAct = cmenu.addAction(QIcon("./src/icons/exit.png"), "退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == exitAct:
            qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())