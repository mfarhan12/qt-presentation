#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
import sys
import numpy as np
import pyqtgraph as pg


class PLotExample(QtWidgets.QWidget):
    freqs = np.linspace(-1024, 1024, 200)
    index = 0
    def __init__(self):
        super(PLotExample, self).__init__()
        self.setWindowTitle('Updating PLot')

        line_plot = pg.PlotWidget()

        fft_plot = pg.PlotWidget()

        self.i_curve = line_plot.plot(pen = "r")
        self.q_curve = line_plot.plot(pen = "g")
        self.fft_curve = fft_plot.plot(pen = "y")
        grid = QtWidgets.QGridLayout()

        grid.addWidget(line_plot,1,0,1,3)
        grid.addWidget(fft_plot,2,0,1,3)
        self.setLayout(grid)
        self.show()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._update_plot)
        self.timer.start(50)

    def _update_plot(self):

        i_data, q_data = self.generate_iq()
        self.i_curve.setData(i_data)
        self.q_curve.setData(q_data)

        fft_data = self.compute_fft(i_data, q_data)
        self.fft_curve.setData(fft_data)


        self.show()

    # simple compute FFT

    def generate_iq(self):
        x = np.linspace(0, 1, 1024)
        freq = self.freqs[self.index]

        self.index += 1
        if self.index >= len(self.freqs):
            self.index = 0

        i_data  = 5 * np.sin(2 * np.pi * freq * x)
    
        i_data = np.add(5 *np.sin(2 * np.pi * freq * x), np.random.rand(len(x)))
        q_data = np.add(5 * np.sin((2 * np.pi * freq * x) + (np.pi / 4)), np.random.rand(len(x)))
        return i_data, q_data

    def compute_fft(self, i_data, q_data):


        # create complex IQ
        iq = i_data + 1j * q_data
        
        # apply hanning window
        iq = iq * np.hanning(len(i_data))

        # compute the fft
        fft_data = 20 * np.log10(np.abs(np.fft.fftshift(np.fft.fft(iq))))

        return fft_data

    def closeEvent(self, event):
        self.timer.stop()

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = PLotExample()
sys.exit(app.exec_())
