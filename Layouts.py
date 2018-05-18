from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Positioning"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 100


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.HorizontalLayout()
        
        vBox = QVBoxLayout()
        vBox.addWidget(self.groupBox)
        self.setLayout(vBox)

        self.show()

    def HorizontalLayout(self):
        self.groupBox = QGroupBox("what is your name")
        hBoxlayout = QHBoxLayout()

        button1 = QPushButton("Football", self)
        hBoxlayout.addWidget(button1)
        button1.clicked.connect(self.buttonClicked)

        button2 = QLabel("Cricket", self)
        hBoxlayout.addWidget(button2)

        self.groupBox.setLayout(hBoxlayout)

    def buttonClicked(self):
        QMessageBox.information(self, "Football", "yes i like it")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
