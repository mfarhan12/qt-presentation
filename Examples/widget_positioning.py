from PySide import QtGui, QtCore
import sys

class simpleWidget(QtGui.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('Positioning Widget')
        self.setGeometry(300, 300, 50, 50)
        grid = QtGui.QGridLayout()
        label11 = QtGui.QLabel('LABEL 1,1')
        label12 = QtGui.QLabel('LABEL 1,2')
        label21 = QtGui.QLabel('LABEL 2,1')
        label22 = QtGui.QLabel('LABEL 2,2')
        grid.addWidget(label11, 0,0,1,1)
        grid.addWidget(label12, 0,1,1,1)
        grid.addWidget(label21, 1,0,1,1)
        grid.addWidget(label22, 1,1,1,1)
        self.setLayout(grid)
        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
