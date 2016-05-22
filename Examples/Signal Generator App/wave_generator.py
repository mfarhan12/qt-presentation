#!/usr/bin/env python

from PySide import QtGui, QtCore
import numpy as np
from scipy import signal
SAMPLES = ['128',
           '256',
           '512',
           '1024',
           '4096',
           '8192',
           '16384',
           '32768']

class WaveGenerator(QtGui.QGroupBox):
    new_signal = QtCore.Signal(list)
    _freq = 5.0
    _n_samples = 1024
    _amp = 5.0
    _phase = 0.0
    _operation = 'Sine'

    def __init__(self, title = 'Signal Generator'):
        super(WaveGenerator, self).__init__()

        grid = QtGui.QGridLayout()
        self.setTitle(title)

        x = np.linspace(0, 1, self._n_samples)
        self.wave = self._amp * np.sin((2 * np.pi * self._freq * x) + self._phase)

        self._sine_button = QtGui.QRadioButton('Sine')

        self._square_button = QtGui.QRadioButton('square')
        self._square_button.click()

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
        self._generate_signal()
        self.setLayout(grid)
        self.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
            self._generate_signal()
        self._freq_spin.valueChanged.connect(update_signal)
        self._amp_spin.valueChanged.connect(update_signal)
        self._phase_spin.valueChanged.connect(update_signal)
        self._sample_combo.currentIndexChanged.connect(update_signal)
        self._sine_button.clicked.connect(update_signal)
        self._square_button.clicked.connect(update_signal)

    def _generate_signal(self):
        if self._operation == 'sine':
            x = np.linspace(0, 1, self._n_samples)
            self.wave = self._amp * np.sin((2 * np.pi * self._freq * x) + self._phase)
            self.new_signal.emit(self.wave)
        else:
            x = np.linspace(0, 1, self._n_samples)
            self.wave = self._amp * signal.square((2 * np.pi *self._freq * x) + self._phase)
            self.new_signal.emit(self.wave)
