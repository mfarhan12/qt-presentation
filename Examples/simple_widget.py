from PySide import QtGui, QtCore
import sys

class simpleWidget(QtGui.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('First WIdget')
        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
