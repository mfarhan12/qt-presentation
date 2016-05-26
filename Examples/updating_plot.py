#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph as pg


class PLotExample(QtGui.QWidget):
    freqs = np.concatenate([np.arange(1, 15, 1), np.arange(1, 15, 1)[::-1]])
    index = 0
    def __init__(self):
        super(PLotExample, self).__init__()
        self.setWindowTitle('Updating PLot')

        line_plot = pg.PlotWidget()
        self.curve = line_plot.plot(pen = "y")
        grid = QtGui.QGridLayout()

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


        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PLotExample()
sys.exit(app.exec_())
