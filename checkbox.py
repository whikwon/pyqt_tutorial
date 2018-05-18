from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Positioning"
        self.top = 100
        self.left = 500
        self.width = 300
        self.height = 600

        self.InitWindow()


    def InitWindow(self):
        checkBox = QCheckBox("Hello World", self)
        checkBox.move(100, 100)
        checkBox.toggle() # default check
        checkBox.stateChanged.connect(self.checkBoxChanged)

        self.label = QLabel("", self)
        self.label.move(120, 150)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.show()

    def checkBoxChanged(self, state):
        if state == Qt.Checked:
            self.label.setText("Hello")
        else:
            self.label.setText("Fuck you")



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
