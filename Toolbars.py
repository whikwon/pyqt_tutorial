from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Toolbars"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.InitWindow()


    def InitWindow(self):

        exitAct = QAction(QIcon('exit.png'), 'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.CloseApp)

        copyAct = QAction(QIcon('Copy.png'), 'Copy', self)
        copyAct.setShortcut('Ctrl+C')

        pasteAct = QAction(QIcon('Paste.png'), 'Paste', self)
        pasteAct.setShortcut('Ctrl+V')

        deleteAct = QAction(QIcon('Delete.png'), 'Delete', self)
        deleteAct.setShortcut('Ctrl+D')

        saveAct = QAction(QIcon('Save.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')

        self.toolbar = self.addToolBar('Toolbar')

        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)
        self.toolbar.addAction(deleteAct)
        self.toolbar.addAction(saveAct)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def CloseApp(self):
        self.close()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())