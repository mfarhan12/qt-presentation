#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
from wave_generator import WaveGenerator
from plot_controls import PlotControls
import pyqtgraph as pg


class WaveGeneratorApp(QtGui.QWidget):
    def __init__(self):
        super(WaveGeneratorApp, self).__init__()
        self.setWindowTitle('Signal Generator')
        self.wave_gen = WaveGenerator()
        self.plot_controls = PlotControls()
        self.plot_controls.config_change.connect(self.update_config)
        self.plot = pg.PlotWidget()
        self.plot_state = self.plot_controls.config
        self.curve = self.plot.plot(pen = 'g')
        self._data = self.wave_gen.wave
        self.curve.setData(self._data)
        grid = QtGui.QGridLayout()

        grid.addWidget(self.plot, 0,0,12,12)
        grid.addWidget(self.wave_gen, 0,13,1,1)
        grid.addWidget(self.plot_controls, 1,13,1,1)
        self.setLayout(grid)

        def plot_data(data):
            self._data = data
            self.update_plot()
        self.wave_gen.new_signal.connect(plot_data)

        self.show()
    def update_config(self, state, changed):
        self.plot_state = state
        if 'color' in changed:
            self.update_plot()
            self.curve.setData(self._data, pen = state['color'])
        if 'grid' in changed:
            self.plot.showGrid(state['grid'], state['grid'])
        if 'autoscale' in changed:
                 self.plot.enableAutoRange('xy', True)
        if 'fill' in changed:
                self.update_plot()

        if 'point' in changed:
                self.update_plot()
    def update_plot(self):
        if self.plot_state['fill']:
            fill = -0.3
            brush_color=(50,50,200,100)
        else:
            fill = 0
            brush_color = (0,0,0,0)

        if self.plot_state['point']:
            self.curve.setData(self._data,
                                pen = self.plot_state['color'],
                                fillLevel=fill,
                                brush=brush_color,
                                symbolBrush = (255,0,0),
                                symbolPen = 'w'
                                )
        else:
            self.curve.clear()
            self.curve.setData(self._data,
                                pen = self.plot_state['color'],
                                fillLevel=fill,
                                brush=brush_color,
                                symbolBrush = None,
                                symbolPen = None
                                )
# Launch the application
app = QtGui.QApplication(sys.argv)
ex = WaveGeneratorApp()
sys.exit(app.exec_())
