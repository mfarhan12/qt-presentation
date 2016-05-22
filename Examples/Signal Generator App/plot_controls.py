#!/usr/bin/env python

from PySide import QtGui, QtCore
import sys
import numpy as np
from scipy import signal
import pyqtgraph as pg

plot_config = {'color': (0, 255, 0),
                'auto_scale': False,
                'grid': False,
                'fill': False,
                'point': False,
                }

class PlotControls(QtGui.QGroupBox):
    config_change = QtCore.Signal(dict, str)
    config = plot_config
    def __init__(self, title = 'PLot Controls'):
        super(PlotControls, self).__init__()

        grid = QtGui.QGridLayout()
        self.setTitle(title)

        self._color_button = QtGui.QPushButton()

        self._auto_scale = QtGui.QPushButton('Auto Scale')

        self._grid = QtGui.QCheckBox('Grid')

        self._fill = QtGui.QCheckBox('Fill')

        self._point = QtGui.QCheckBox('Point')


        grid.addWidget(QtGui.QLabel('Plot Color'), 0,0,1,1)
        grid.addWidget(self._color_button, 0,1,1,1)

        grid.addWidget(self._auto_scale, 1,0,1,1)
        grid.addWidget(self._grid, 1,1,1,1)

        grid.addWidget(self._fill, 2,0,1,1)
        grid.addWidget(self._point, 2,1,1,1)

        self._connect_controls()
        self.setLayout(grid)
        self.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        self.show()

    def _connect_controls(self):

        def new_color():
            qcol = QtGui.QColorDialog.getColor()
            self.config['color'] = (qcol.red(), qcol.green(), qcol.blue())

            self.config_change.emit(self.config, 'color')
            button_color = 'rgb(%s, %s, %s)' % (qcol.red(), qcol.green(), qcol.blue())
            self._color_button.setStyleSheet('background: %s' % button_color)

        self._color_button.clicked.connect(new_color)

        def set_autoscale():
                self.config_change.emit(self.config, 'autoscale')

        self._auto_scale.clicked.connect(set_autoscale)

        def set_grid():
                self.config['grid'] = self._grid.checkState()
                self.config_change.emit(self.config, 'grid')

        self._grid.clicked.connect(set_grid)

        def set_fill():
                self.config['fill'] = self._fill.checkState()
                self.config_change.emit(self.config, 'fill')

        self._fill.clicked.connect(set_fill)

        def set_point():
                self.config['point'] = self._point.checkState()
                self.config_change.emit(self.config, 'point')

        self._point.clicked.connect(set_point)
