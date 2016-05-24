import numpy as np
import pyqtgraph as pg
from PySide import QtGui, QtCore
import sys
import random

class PlotExample(QtGui.QWidget):
    def __init__(self):
        super(PlotExample, self).__init__()
        self.setWindowTitle('Plot Example')
        grid = QtGui.QGridLayout()
        line_plot = pg.PlotWidget(title="Simple Plot")
        self.curve = line_plot.plot(pen = 'r')
        
        fft_plot = pg.PlotWidget(title="FFT Plot")
        self.fft_curve = fft_plot.plot(pen = 'y')
        grid.addWidget(line_plot,0,0,1,1)
        grid.addWidget(fft_plot,1,0,1,1)

        self.setLayout(grid)
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.generate_sine)
        self.timer.start(500)

    def generate_sine(self):
        
        x = np.linspace(0, 1, 1024)
        freq = random.randint(1,200)

        wave = 5 * np.sin(2 * np.pi * freq * x)
        self.curve.setData(wave)
        wave= wave * np.hanning(len(wave))
        power_spectrum = np.abs(np.fft.rfft(wave))/len(wave)
        self.fft_curve.setData(power_spectrum)

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PlotExample()
sys.exit(app.exec_())

