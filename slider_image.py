from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QWidget, QSlider, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Positioning"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()


    def InitWindow(self):

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(60, 60, 100, 20)
        self.slider.valueChanged[int].connect(self.ChangedValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('sample.png'))
        self.label.setGeometry(60, 100, 150, 120)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def ChangedValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('sample.png'))
        elif value < 50:
            self.label.setPixmap(QPixmap('sample2.png'))
        else:
            self.label.setPixmap(QPixmap('sample3.png'))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
