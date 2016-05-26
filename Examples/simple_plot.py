#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg


class PLotExample(QtGui.QWidget):
    def __init__(self):
        super(PLotExample, self).__init__()
        self.setWindowTitle('Simple PLot')

        line_plot = pg.PlotWidget()

        self.curve = line_plot.plot(pen = "r")
        line_plot .showGrid(x=True, y=True)
        line_plot .setLabel('left', "Voltage", units='V')
        line_plot .setLabel('bottom', "Time", units='T')
        x = np.linspace(0, 1, 1024)
        wave = 5 * np.sin(2 * np.pi * 5 * x)
        self.curve = line_plot.plot(pen = "r")
        self.curve.setData(x, wave)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(line_plot, 0,0,12,12)
        self.setLayout(grid)


        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PLotExample()
sys.exit(app.exec_())
