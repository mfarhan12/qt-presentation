import numpy as np
import pyqtgraph as pg
from PySide import QtGui, QtCore
import sys
import random

class PlotExample(QtGui.QWidget):
    def __init__(self):
        super(PlotExample, self).__init__()
        self.setWindowTitle("Plot Example")
        grid = QtGui.QGridLayout()
        line_plot = pg.PlotWidget(title="Simple Plot")
        self.curve = line_plot.plot(pen = "r")
        line_plot .showGrid(x=True, y=True)
        line_plot .setLabel('left', "Voltage", units='V')
        line_plot .setLabel('bottom', "Time", units='T')
        x = np.linspace(0, 1, 1024)
        wave = 5 * np.sin(2 * np.pi * 5 * x)
        self.curve.setData(x, wave)
        grid.addWidget(line_plot,1,0,1,3)

        self.setLayout(grid)
        self.show()



# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PlotExample()
sys.exit(app.exec_())

