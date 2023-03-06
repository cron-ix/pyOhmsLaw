import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi('ohms_law_qt.ui')
window.show()
app.exec()