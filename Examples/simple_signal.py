#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
import sys

class SimpleSignal(QtWidgets.QWidget):
    def __init__(self):
        super(SimpleSignal, self).__init__()
        self.setWindowTitle('Simple Signals')
        self.setGeometry(300, 300, 50, 50)
        grid = QtWidgets.QGridLayout()
        self._count = 0

        self.result_label = QtWidgets.QLabel('%d' % self._count)
        self.button = QtWidgets.QPushButton('+')
        self.reset = QtWidgets.QPushButton('RESET')


        def add_count():
            self._count += 1
            self.result_label.setText('%d' % self._count)
        self.button.clicked.connect(add_count)

        def reset_count():
            self._count = 0
            self.result_label.setText('%d' % self._count)
        self.reset.clicked.connect(reset_count)

        grid.addWidget(self.button, 0,0,1,1)
        grid.addWidget(self.reset, 0,1,1,1)
        grid.addWidget(self.result_label, 1,0,1,1)

        self.setLayout(grid)
        self.show()
    def keyPressEvent(self, event):
        if event.text() == '+':
            self._count += 1
            self.result_label.setText('%d' % self._count)

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = SimpleSignal()
sys.exit(app.exec_())
