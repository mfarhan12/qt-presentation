from PyQt5 import QtWidgets, QtCore
import sys

class PositioningWidget(QtWidgets.QWidget):
    def __init__(self):
		super(PositioningWidget, self).__init__()
		self.setWindowTitle('Positioning Widget')
		self.setGeometry(300, 300, 300, 300)
		grid = QtWidgets.QGridLayout()
		green_label = QtWidgets.QLabel('')
		green_label.setStyleSheet('background-color: green')
		yellow_label = QtWidgets.QLabel('')
		yellow_label.setStyleSheet('background-color: yellow')
		red_label = QtWidgets.QLabel('')
		red_label.setStyleSheet('background-color: red')
		grid.addWidget(green_label, 0,0,1,1)
		grid.addWidget(yellow_label, 0,1,1,1)
		grid.addWidget(red_label, 1,0,1,2)
		self.setLayout(grid)
		self.show()

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = PositioningWidget()
sys.exit(app.exec_())
