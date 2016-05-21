#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
import numpy as np
from scipy import signal
import pyqtgraph as pg
SAMPLES = ['128',
           '256',
           '512',
           '1024',
           '4096',
           '8192',
           '16384',
           '32768']
class SignalGenerator(QtGui.QGroupBox):
    newArray = QtCore.Signal(list)
    def __init__(self, title = 'Signal Generator'):
        super(SignalGenerator, self).__init__()

        grid = QtGui.QGridLayout()
        self.setTitle(title)
        self._freq = 5.0
        self._n_samples = 1024
        self._amp = 5.0
        self._phase = 0.0
        self._operation = 'Sine'

        self._sine_button = QtGui.QRadioButton('Sine')
        self._sine_button.click()

        self._square_button = QtGui.QRadioButton('square')

        self._freq_spin = QtGui.QDoubleSpinBox()
        self._freq_spin.setRange(0.0001, 20000)
        self._freq_spin.setValue(self._freq)

        self._amp_spin = QtGui.QDoubleSpinBox()
        self._amp_spin.setRange(1, 20000)
        self._amp_spin.setValue(self._amp)

        self._phase_spin = QtGui.QDoubleSpinBox()
        self._phase_spin.setValue(self._phase)

        self._sample_combo = QtGui.QComboBox()
        self._sample_combo.addItems(SAMPLES)
        self._sample_combo.setCurrentIndex(3)

        grid.addWidget(QtGui.QLabel('Signal Type'), 0,0,1,1)
        grid.addWidget(self._sine_button, 0,1,1,1)
        grid.addWidget(self._square_button, 0,2,1,1)

        grid.addWidget(QtGui.QLabel('Frequency:'), 1,0,1,1)
        grid.addWidget(self._freq_spin, 1,1,1,1)

        grid.addWidget(QtGui.QLabel('Amplitude:'),1,2,1,1)
        grid.addWidget(self._amp_spin, 1,3,1,1)

        grid.addWidget(QtGui.QLabel('Phase:'),2,0,1,1)
        grid.addWidget(self._phase_spin, 2,1,1,1)

        grid.addWidget(QtGui.QLabel('Samples:'),2,2,1,1)
        grid.addWidget(self._sample_combo, 2,3,1,1)

        self._connect_controls()
        self._calculate_list()
        self._calculate_list()
        self.setLayout(grid)
        self.show()

    def _connect_controls(self):

        def update_signal():
            self._freq = self._freq_spin.value()
            self._amp = self._amp_spin.value()
            self._phase = self._phase_spin.value()
            self._n_samples = int(self._sample_combo.currentText())
            if self._sine_button.isChecked():
                self._operation = 'sine'
            else:
                self._operation = 'square'
            self._calculate_list()
        self._freq_spin.valueChanged.connect(update_signal)
        self._amp_spin.valueChanged.connect(update_signal)
        self._phase_spin.valueChanged.connect(update_signal)
        self._sample_combo.currentIndexChanged.connect(update_signal)
        self._sine_button.clicked.connect(update_signal)
        self._square_button.clicked.connect(update_signal)

    def _calculate_list(self):
        if self._operation == 'sine':
            x = np.linspace(0, 1, self._n_samples)
            y = self._amp * np.sin((2 * np.pi * self._freq * x) + self._phase)
            self.newArray.emit(y)
        else:
            x = np.linspace(0, 1, self._n_samples)
            y = self._amp * signal.square((2 * np.pi *self._freq * x) + self._phase)
            self.newArray.emit(y)

class simpleWidget(QtGui.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('Signal Generator')
        self.sig_gen = SignalGenerator()
        self.plot = pg.PlotWidget()
        self.curve = self.plot.plot(pen = 'g')
        grid = QtGui.QGridLayout()
        grid.addWidget(self.sig_gen, 0,0,1,1)
        grid.addWidget(self.plot, 1,0,1,1)
        self.setLayout(grid)

        def plot_data(data):
            self.curve.setData(data)
        self.sig_gen.newArray.connect(plot_data)

        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
