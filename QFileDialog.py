from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QPushButton
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 File Dialog"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500


        self.InitWindow()


    def InitWindow(self):
        self.button = QPushButton("Open File", self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.clicked.connect(self.openFileDialog)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(100, 150, 400, 300)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        # size information
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
