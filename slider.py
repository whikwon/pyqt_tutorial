from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QWidget, QSlider, QLineEdit, QVBoxLayout
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Positioning"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 200


        self.InitWindow()


    def InitWindow(self):
        vBoxLayout = QVBoxLayout()
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(100, 50)
        vBoxLayout.addWidget(self.lineEdit)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(100, 20)
        self.slider.setMinimum(1)
        self.slider.setMaximum(99)
        self.slider.setValue(20)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.changedValue)
        vBoxLayout.addWidget(self.slider)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def changedValue(self):
        size = str(self.slider.value())
        self.lineEdit.setText(size)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
