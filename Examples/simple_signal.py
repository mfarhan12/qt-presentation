#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys

class SimpleSignal(QtGui.QWidget):
    def __init__(self):
        super(SimpleSignal, self).__init__()
        self.setWindowTitle('Simple Signals')
        self.setGeometry(300, 300, 50, 50)
        grid = QtGui.QGridLayout()
        self._count = 0

        self.result_label = QtGui.QLabel('%d' % self._count)
        self.button = QtGui.QPushButton('+')
        self.reset = QtGui.QPushButton('RESET')
        

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

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = SimpleSignal()
sys.exit(app.exec_())
