#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
TEXT_ITEMS = ['ITEM1', 'ITEM2', 'ITEM3']
class simpleWidget(QtGui.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('Controls Widget')
        self.setGeometry(300, 300, 50, 50)
        grid = QtGui.QGridLayout()
        text_box = QtGui.QLineEdit('Text Box')
        button = QtGui.QPushButton('Button')
        radio1 = QtGui.QRadioButton('Radio 1')
        radio2 = QtGui.QRadioButton('Radio 2')

        combobox = QtGui.QComboBox()
        combobox.addItems(TEXT_ITEMS)
        spinbox = QtGui.QSpinBox()

        grid.addWidget(text_box, 0,0,1,1)
        grid.addWidget(button, 0,1,1,1)
        grid.addWidget(radio1, 1,0,1,1)
        grid.addWidget(radio2, 1,1,1,1)
        grid.addWidget(spinbox, 2,0,1,1)
        grid.addWidget(combobox, 3,0,1,2)
        self.setLayout(grid)
        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
