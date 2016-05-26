from PySide import QtGui, QtCore
import sys

class PositioningWidget(QtGui.QWidget):
    def __init__(self):
		super(PositioningWidget, self).__init__()
		self.setWindowTitle('Positioning Widget')
		self.setGeometry(300, 300, 300, 300)
		grid = QtGui.QGridLayout()
		green_label = QtGui.QLabel('')
		green_label.setStyleSheet('background-color: green')
		yellow_label = QtGui.QLabel('')
		yellow_label.setStyleSheet('background-color: yellow')
		red_label = QtGui.QLabel('')
		red_label.setStyleSheet('background-color: red')
		grid.addWidget(green_label, 0,0,1,1)
		grid.addWidget(yellow_label, 0,1,1,1)
		grid.addWidget(red_label, 1,0,1,2)
		self.setLayout(grid)
		self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PositioningWidget()
sys.exit(app.exec_())
