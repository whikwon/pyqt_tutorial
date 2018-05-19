from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QPushButton, QLineEdit
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.InitWindow()


    def InitWindow(self):

        self.linedit = QLineEdit(self)
        self.linedit.move(200,200)
        self.linedit.resize(280,40)

        self.button = QPushButton("Show Text", self)
        self.button.move(270,250)
        self.button.clicked.connect(self.onClick)


        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def onClick(self):
        textValue = self.linedit.text()
        QMessageBox.question(self, "Line Edit", "You Have Typed " + textValue,
                             QMessageBox.Ok, QMessageBox.Ok)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())