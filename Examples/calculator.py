#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys

class CalculatorWidget(QtGui.QWidget):
    _num1 = 0
    _num2 = 0
    _operation = '+'

    def __init__(self):
        super(CalculatorWidget, self).__init__()
        self.setWindowTitle('Calculator Widget')
        self.setGeometry(300, 300, 50, 50)
        grid = QtGui.QGridLayout()
        
        self.add = QtGui.QRadioButton('+')
        self.add.click()
        self.sub = QtGui.QRadioButton('-')
        self.mul = QtGui.QRadioButton('X')
        self.div = QtGui.QRadioButton('/')
        self.spin1 = QtGui.QDoubleSpinBox()
        self.spin2 = QtGui.QDoubleSpinBox()
 
        self.result_label = QtGui.QLabel('')

        grid.addWidget(self.spin1, 0,0,1,2)
        grid.addWidget(self.spin2, 0,2,1,2)
        grid.addWidget(self.add, 1,0,1,1)
        grid.addWidget(self.sub, 1,1,1,1)
        grid.addWidget(self.mul, 1,2,1,1)
        grid.addWidget(self.div, 1,3,1,1)
        grid.addWidget(self.result_label, 2,0,1,2)

        self._connect_controls()
        self._calculate_result()
        self.setLayout(grid)
        self.show()

    def _connect_controls(self):

        def update_num():
            self._num1 = self.spin1.value()
            self._num2 = self.spin2.value()
            self._calculate_result()

        self.spin1.editingFinished.connect(update_num)
        self.spin2.editingFinished.connect(update_num)

        def update_operation(widget):
            self._operation = widget.text()
            self._calculate_result()

        self.add.clicked.connect(lambda: update_operation(self.add))
        self.sub.clicked.connect(lambda: update_operation(self.sub))
        self.div.clicked.connect(lambda: update_operation(self.div))
        self.mul.clicked.connect(lambda: update_operation(self.mul))

    def _calculate_result(self):

        try:
            if self._operation == '+':
                result = self._num1 + self._num2
            if self._operation == '-':
                result = self._num1 - self._num2
            if self._operation == 'X':
                result = self._num1 * self._num2
            if self._operation == '/':
                result = self._num1 / self._num2
            self.result_label.setText('%0.4f' % (result))

        except ZeroDivisionError:
                self.result_label.setText('INF')
        
# Launch the application
app = QtGui.QApplication(sys.argv)
ex = CalculatorWidget()
sys.exit(app.exec_())
