#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore
import sys
import numpy as np
import pyqtgraph as pg


class PLotExample(QtWidgets.QWidget):
    def __init__(self):
        super(PLotExample, self).__init__()
        self.setWindowTitle('Simple PLot')
        x = np.linspace(-100, 100, 1000)
        data = np.sin(x) / x


        full_plot =  pg.PlotWidget()
        full_plot.plot(data, pen=(255,255,255,200))
        region_selector = pg.LinearRegionItem([400,700])

        full_plot.addItem(region_selector)

        region_plot = pg.PlotWidget(title="Zoom on selected region")
        region_plot.plot(data)

        def updatePlot():
            region_plot.setXRange(region_selector.getRegion()[0],
                                    region_selector.getRegion()[1], padding=0)

        def updateRegion():
            region_selector.setRegion(region_plot.getViewBox().viewRange()[0])

        region_selector.sigRegionChanged.connect(updatePlot)
        region_plot.sigXRangeChanged.connect(updateRegion)
        updatePlot()
        grid = QtWidgets.QGridLayout()

        grid.addWidget(full_plot,0,0,1,3)
        grid.addWidget(region_plot,1,0,1,3)
        self.setLayout(grid)
        self.show()

# Launch the application
app = QtWidgets.QApplication(sys.argv)
ex = PLotExample()
sys.exit(app.exec_())
