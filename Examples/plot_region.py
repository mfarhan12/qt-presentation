from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Region Selection Example")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')



x = np.linspace(-100, 100, 1000)
data = np.sin(x) / x
full_plot = win.addPlot(title="Region Selection")
full_plot.plot(data, pen=(255,255,255,200))
region_selector = pg.LinearRegionItem([400,700])

full_plot.addItem(region_selector)

win.nextRow()

region_plot = win.addPlot(title="Zoom on selected region")
region_plot.plot(data)
def updatePlot():
    region_plot.setXRange(*region_selector.getRegion(), padding=0)
def updateRegion():
    region_selector.setRegion(region_plot.getViewBox().viewRange()[0])
region_selector.sigRegionChanged.connect(updatePlot)
region_plot.sigXRangeChanged.connect(updateRegion)
updatePlot()

QtGui.QApplication.instance().exec_()