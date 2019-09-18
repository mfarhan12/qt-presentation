#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
import sys

TEXT_ITEMS = ['ITEM1', 'ITEM2', 'ITEM3']

class simpleWidget(QtWidgets.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('Controls Widget')
        self.setGeometry(300, 300, 50, 50)
        grid = QtWidgets.QGridLayout()
        text_box = QtWidgets.QLineEdit('Text Box')
        button = QtWidgets.QPushButton('Button')
        radio1 = QtWidgets.QRadioButton('Radio 1')
        radio2 = QtWidgets.QRadioButton('Radio 2')

        combobox = QtWidgets.QComboBox()
        combobox.addItems(TEXT_ITEMS)
        spinbox = QtWidgets.QSpinBox()
        checkbox = QtWidgets.QCheckBox('Check Box')

        grid.addWidget(text_box, 0,0,1,1)
        grid.addWidget(button, 0,1,1,1)
        grid.addWidget(radio1, 1,0,1,1)
        grid.addWidget(radio2, 1,1,1,1)
        grid.addWidget(spinbox, 2,0,1,1)
        grid.addWidget(combobox, 3,0,1,1)
        grid.addWidget(checkbox, 3,1,1,1)
        self.setLayout(grid)
        self.show()

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
