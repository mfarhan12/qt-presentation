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
        
        x = np.linspace(-100, 100, 1000)
        data = np.sin(x) / x
        
        full_plot =  pg.PlotWidget(title="Region Selection")
        full_plot.plot(data, pen=(255,255,255,200))
        region_selector = pg.LinearRegionItem([400,700])

        full_plot.addItem(region_selector)

        region_plot = pg.PlotWidget(title="Zoom on selected region")
        region_plot.plot(data)

        def updatePlot():
            region_plot.setXRange(*region_selector.getRegion(), padding=0)

        def updateRegion():
            region_selector.setRegion(region_plot.getViewBox().viewRange()[0])

        region_selector.sigRegionChanged.connect(updatePlot)
        region_plot.sigXRangeChanged.connect(updateRegion)
        updatePlot()

        grid.addWidget(full_plot,0,0,1,3)
        grid.addWidget(region_plot,1,0,1,3)

        self.setLayout(grid)
        self.show()



# Launch the application
app = QtGui.QApplication(sys.argv)
ex = PlotExample()
sys.exit(app.exec_())
