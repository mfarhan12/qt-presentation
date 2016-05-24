#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
TEXT_ITEMS = ['ITEM1', 'ITEM2', 'ITEM3']
class Calculator(QtGui.QWidget):
    new_calculation = QtCore.Signal(float, float, str, str)
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle('Controls Widget')
        self.setGeometry(300, 300, 50, 50)

        grid = QtGui.QGridLayout()

        self._num1 = 0
        self._num2 = 0
        self._operation = '+'

        self.add = QtGui.QRadioButton('+')
        self.add.click()
        self.sub = QtGui.QRadioButton('-')
        self.mul = QtGui.QRadioButton('X')
        self.div = QtGui.QRadioButton('/')

        self.spin1 = QtGui.QDoubleSpinBox()
        self.spin2 = QtGui.QDoubleSpinBox()

        grid.addWidget(self.spin1, 0,0,1,1)
        grid.addWidget(self.spin2, 0,1,1,1)
        grid.addWidget(self.add, 1,0,1,1)
        grid.addWidget(self.sub, 1,1,1,1)
        grid.addWidget(self.mul, 1,2,1,1)
        grid.addWidget(self.div, 1,3,1,1)

        self._connect_controls()
        self._calculate_result()
        self.setLayout(grid)
        self.show()

    def _connect_controls(self):

        def update_num():
            self._num1 = self.spin1.value()
            self._num2 = self.spin2.value()
            self._calculate_result()

        self.spin1.valueChanged.connect(update_num)
        self.spin2.valueChanged.connect(update_num)

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
            self.new_calculation.emit(self._num1, self._num2, self._operation, '%0.4f' % result)

        except ZeroDivisionError:
            self.new_calculation.emit(self._num1, self._num2, self._operation, 'INF')

class CalculatorWidget(QtGui.QWidget):
    def __init__(self):
        super(CalculatorWidget, self).__init__()
        self.setWindowTitle('Calculator')
        self.calculator = Calculator()
        self.list = QtGui.QListWidget()
        grid = QtGui.QGridLayout()
        grid.addWidget(self.calculator, 0,0,1,1)
        grid.addWidget(self.list, 1,0,1,1)
        self.setLayout(grid)

        def got_result(num1,num2, operation, result):
            txt = ('%0.4f %s %0.4f = %s' % (num1, operation, num2, result))
            self.list.addItem(txt)
        self.calculator.new_calculation.connect(got_result)
        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = CalculatorWidget()
sys.exit(app.exec_())
