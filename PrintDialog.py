from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
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
        self.button = QPushButton("Print", self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.clicked.connect(self.createPrintDialog)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(100, 150, 200, 200)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        # size information
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def createPrintDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
