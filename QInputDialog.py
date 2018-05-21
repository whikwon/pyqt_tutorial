from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QLabel, QPushButton
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Input Diaglogs"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.InitWindow()


    def InitWindow(self):
        self.button = QPushButton("Open Dialog", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.createInputDialog)

        self.label = QLabel("Hello", self)
        self.label.setGeometry(100, 150, 300, 50)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        # size information
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def createInputDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter Name")
        if ok:
            self.label.setText(str(text))




App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

