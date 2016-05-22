from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

line_plot = win.addPlot(title="Multiple curves")
line_plot.showGrid(True, True)
curve1 = line_plot.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
curve2 = line_plot.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Blue curve")
curve3 = line_plot.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Green curve")

win.nextRow()

scatter_plot = win.addPlot(title="Scatter plot, axis labels, log scale")
scatter_plot.showGrid(True, True)
x = np.random.normal(size=1000) * 1e-5
y = x*1000 + 0.005 * np.random.normal(size=1000)
y -= y.min()-1.0
mask = x > 1e-15
x = x[mask]
y = y[mask]
scatter_plot.plot(x,
                y, pen=None,
                symbol='t',
                symbolPen=None,
                symbolSize=10,
                symbolBrush=(100, 100, 255, 100))
scatter_plot.setLabel('left', "Y Axis", units='A')
scatter_plot.setLabel('bottom', "X Axis", units='s')
scatter_plot.setLogMode(x=True, y=False)



QtGui.QApplication.instance().exec_()
