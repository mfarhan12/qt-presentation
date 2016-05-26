from PySide import QtGui, QtCore
import sys

class SimpleWidget(QtGui.QWidget):
    def __init__(self):
        super(SimpleWidget, self).__init__()
        self.setWindowTitle('First Widget')
        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = SimpleWidget()
sys.exit(app.exec_())
