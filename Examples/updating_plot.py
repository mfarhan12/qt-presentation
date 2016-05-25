import numpy as np
import pyqtgraph as pg
from PySide import QtGui, QtCore
import sys
import random

class PlotExample(QtGui.QWidget):

    freqs = np.concatenate([np.arange(0, 15, 1), np.arange(0, 15, 1)[::-1]])
    index = 0
    
    def __init__(self):
        super(PlotExample, self).__init__()
        self.setWindowTitle("Plot Example")
        grid = QtGui.QGridLayout()
        line_plot = pg.PlotWidget(title="Updating Plot")
        self.curve = line_plot.plot(pen = "y")
 

        grid.addWidget(line_plot,1,0,1,3)
        self.setLayout(grid)
        self.show()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._update_plot)
        self.timer.start(50)
    def _update_plot(self):
        x = np.linspace(0, 1, 1024)
        freq = self.freqs[self.index]
        self.index += 1
        if self.index >= len(self.freqs):
            self.index = 0
        wave = 5 * np.sin(2 * np.pi * freq * x)
        self.curve.setData(wave)




# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PlotExample()
sys.exit(app.exec_())

