from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sys import argv, exit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitWindow()

    def InitWindow(self):
        self.layout = BoxLayout()
        self.label = QLabel('please', self)
        self.setGeometry(50, 100, 100, 50)
        self.show()


class BoxLayout(QWidget):
    def init(self, parent=None):
        QWidget.init(self, parent)
        self.resize(100, 300)

        vbox=QVBoxLayout(self)
        self.textEdit = QTextEdit("""
            This function returns true if the contents of the MIME data object,
            specified by source , can be decoded and inserted into the document.
            It is called for example when during a drag operation the mouse
            enters this widget and it is necessary to determine whether it is
            possible to accept the drag and drop operation.
        """)
        vbox.addWidget(self.textEdit)
        vbox.addWidget(QPushButton("OK", self))
        vbox.addWidget(QPushButton("Cancel", self))

    def wheelEvent(self, event):
        vsb=self.textEdit.verticalScrollBar()
        dy=((-event.angleDelta()/8)/15)*vsb.singleStep()
        vsb.setSliderPosition(vsb.sliderPosition()+dy)


if __name__ == "main":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
