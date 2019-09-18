#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
import sys

class simpleWidget(QtWidgets.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('Style Widget')
        self.setGeometry(300, 300, 50, 50)
        grid = QtWidgets.QGridLayout()
        bold_text = QtWidgets.QLabel('BOLD LABEL')
        bold_text.setStyleSheet('font-weight: bold')

        blue_text = QtWidgets.QLabel('BLUE TEXT')
        blue_text.setStyleSheet('color: blue')

        blue_background = QtWidgets.QLabel('BLUE BACKGROUND')
        blue_background.setStyleSheet('background-color: rgb(0,25,255); color: white')

        size_label = QtWidgets.QLabel('TEXT SIZE 8')
        size_label.setStyleSheet('font-size:20pt')
        grid.addWidget(bold_text, 0,0,1,1)
        grid.addWidget(blue_text, 0,1,1,1)
        grid.addWidget(blue_background, 1,0,1,1)
        grid.addWidget(size_label, 1,1,1,1)
        self.setLayout(grid)
        self.show()

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
