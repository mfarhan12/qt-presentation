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
        self.freq_label = QtGui.QLabel("")
        self.calc_label = QtGui.QLabel("")
        self.error_label = QtGui.QLabel("")
        fft_plot = pg.PlotWidget(title="FFT Plot")
        self.fft_curve = fft_plot.plot(pen = "y")
        
        grid.addWidget(self.freq_label,0,0,1,1)
        grid.addWidget(self.calc_label,0,1,1,1)
        grid.addWidget(self.error_label,0,2,1,1)
        
        grid.addWidget(line_plot,1,0,1,3)
        grid.addWidget(fft_plot,2,0,1,3)

        self.setLayout(grid)
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.generate_sine)
        self.timer.start(500)

    def generate_sine(self):
        
        x = np.linspace(0, 1, 1024)
        freq = random.randint(1,512)
        self.freq_label.setText("Signal Frequency %0.2f Hz" % freq)
        wave = 5 * np.sin(2 * np.pi * freq * x)
        self.curve.setData(wave)
        wave= wave * np.hanning(len(wave))
        power_spectrum = np.abs(np.fft.rfft(wave))/len(wave)
        peak_index =  np.where(power_spectrum == max(power_spectrum))[0][0]

        calc = (float(peak_index) / len(power_spectrum)) * 512
        self.calc_label.setText("Calculated Frequency: %0.2f Hz" % float(calc))
        self.error_label.setText("Error: %0.2f %%" % ((calc / float(freq)) * 100))
        self.fft_curve.setData(power_spectrum)

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PlotExample()
sys.exit(app.exec_())

