import sys
from PyQt4 import QtCore, QtGui
from MainWindow import Ui_MainWindow









if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = notifyerForm()
    myapp.show()
    sys.exit(app.exec())
    