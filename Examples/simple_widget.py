from PyQt5 import QtWidgets, QtCore
import sys

class SimpleWidget(QtWidgets.QWidget):
    def __init__(self):
        super(SimpleWidget, self).__init__()
        self.setWindowTitle('First Widget')
        self.show()

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = SimpleWidget()
sys.exit(app.exec_())
