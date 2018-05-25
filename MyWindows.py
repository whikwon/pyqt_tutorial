from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.label = Label("Please, ", self)
        # size information
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

class Label(QLabel):
    def wheelEvent(self, event):
        print(event.angleDelta())

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
