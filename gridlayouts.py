from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 GridLayouts"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()


    def InitWindow(self):

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.gridLayoutCreation()
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.groupBox)
        self.setLayout(vboxLayout)

        self.show()

    def gridLayoutCreation(self):
        self.groupBox = QGroupBox("Grid Layout Example")
        gridLayout = QGridLayout()
        gridLayout.addWidget(QPushButton('1'), 0, 0)
        gridLayout.addWidget(QPushButton('2'), 0, 1)

        self.groupBox.setLayout(gridLayout)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
