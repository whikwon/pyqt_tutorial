from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QLabel, QVBoxLayout
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 SpinBox"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200

        self.InitWindow()


    def InitWindow(self):

        vBoxLayout = QVBoxLayout()
        self.label = QLabel("Hello", self)
        self.label.move(60, 60)
        vBoxLayout.addWidget(self.label)

        self.spinBox = QDoubleSpinBox(self)
        self.spinBox.move(60, 30)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(20)
        self.spinBox.setMaximumWidth(50)
        self.spinBox.valueChanged.connect(self.valueChanged)
        vBoxLayout.addWidget(self.spinBox)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def valueChanged(self):
        self.label.setText("Current Value" + str(self.spinBox.value()))



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
