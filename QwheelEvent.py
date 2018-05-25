from PyQt5 import QtWidgets


class Q(QtWidgets.QLabel):

    def wheelEvent(self, event):
        print(event.angleDelta())

app = QtWidgets.QApplication([])
w = Q()
w.show()
app.exec_()
