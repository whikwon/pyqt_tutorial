from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QPushButton, QLineEdit, QVBoxLayout, QDialogButtonBox, QListWidget, QAbstractItemView
from PyQt5 import QtWidgets
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

        # lineEdit
        self.linedit = QLineEdit(self)
        # default text
        self.linedit.setPlaceholderText("Hello")
        # text validator
        self.linedit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r'^[^ \t].+'), None))
        # text postprocess
        self.linedit.editingFinished.connect(self.postProcess)

#        self.linedit.move(200,200)
#        self.linedit.resize(280,40)

        layout = QVBoxLayout()
        layout.addWidget(self.linedit)

        # activates when connected
        self.buttonBox = bb = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self,
        )
        layout.addWidget(bb)

        # LableList
        self.labelList = QListWidget()
        self.labelList.addItem('Hello')
        self.labelList.setDragDropMode(
            QAbstractItemView.InternalMove)
        # lineedit + listwidget
        self.linedit.list_widget = self.labelList
        layout.addWidget(self.labelList)

        listLayout = QVBoxLayout()
        self.editButton = QtWidgets.QToolButton()
        self.editButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        listLayout.addWidget(self.labelList)
        listLayout.addWidget(self.editButton)  # 0, Qt.AlignCenter)
        self.labelListContainer = QWidget()
        self.labelListContainer.setLayout(listLayout)

        # uniqlabellist
        self.uniqLabelList = EscapableQListWidget()
        self.uniqLabelList.setToolTip(
            "Select label to start annotating for it. "
            "Press 'Esc' to deselect.")

        # Labelsdock
        self.labelsdock = QtWidgets.QDockWidget(u'Label List', self)
        self.labelsdock.setObjectName(u'Label List')
        self.labelsdock.setWidget(self.uniqLabelList)
        self.dock = QtWidgets.QDockWidget('Polygon Labels', self)
        self.dock.setObjectName('Labels')
        self.dock.setWidget(self.labelListContainer)

        self.addDockWidget(Qt.RightDockWidgetArea, self.labelsdock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

#        self.button = QPushButton("Show Text", self)
#        self.button.move(270,250)
#        self.button.clicked.connect(self.onClick)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def onClick(self):
        textValue = self.linedit.text()
        QMessageBox.question(self, "Line Edit", "You Have Typed " + textValue,
                             QMessageBox.Ok, QMessageBox.Ok)

    def postProcess(self):
        text = self.linedit.text()
        if hasattr(text, 'strip'):
            text = text.strip()
        else:
            text = text.trimmed()
        self.linedit.setText(text)

    def validate(self):
        text = self.edit.text()
        if hasattr(text, 'strip'):
            text = text.strip()
        else:
            text = text.trimmed()
        if text:
            self.accept()


class EscapableQListWidget(QtWidgets.QListWidget):

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.clearSelection()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
