from PySide import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import random
import sys

class ThreeDPlot(QtGui.QWidget):
    amp = 5
    x_size = 160
    y_size = 150
    rand_noise = False


    def __init__(self):
        super(ThreeDPlot, self).__init__()
        self.setGeometry(300, 300, 800, 350)
        w = gl.GLViewWidget()
        self.rand_check = QtGui.QCheckBox('Enable Noise')
        self.amplitude_spin = QtGui.QDoubleSpinBox()
        self.amplitude_spin.setRange(1, 50)
        self.amplitude_spin.setValue(self.amp)

        self.x_spin = QtGui.QDoubleSpinBox()
        self.x_spin.setRange(1, 800)
        self.x_spin.setValue(self.x_size)


        self.y_spin = QtGui.QDoubleSpinBox()
        self.y_spin.setRange(1, 800)
        self.y_spin.setValue(self.y_size)

        w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
        w.setCameraPosition(distance=500)
        g = gl.GLGridItem()
        g.scale(20,20,1)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)

        curve = gl.GLSurfacePlotItem(shader='heightColor', computeNormals=False, smooth=False)
        curve.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
        curve.translate(-50, -50, 0)
        w.addItem(curve)

        grid = QtGui.QGridLayout()
        grid.addWidget(w, 0,0,13,12)
        grid.addWidget(QtGui.QLabel('Amplitude'), 0,13,1,1)
        grid.addWidget(self.amplitude_spin, 0,14,1,1)
        grid.addWidget(QtGui.QLabel('X Size'), 1,13,1,1)
        grid.addWidget(self.x_spin, 1,14,1,1)
        grid.addWidget(QtGui.QLabel('Y Size'), 2,13,1,1)
        grid.addWidget(self.y_spin, 2,14,1,1)
        grid.addWidget(self.rand_check, 3,13,1,1)

        def update():
            z = self.amp * pg.gaussianFilter(np.random.normal(size=(self.x_size, self.y_size)), (1,1))
            if self.rand_noise:
                for x in range(20):
                    z[random.randint(0, self.x_size - 1), random.randint(0, self.y_size - 1)] = self.amp * 2
            curve.setData(z=z)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(update)
        self.timer.start(0)

        def update_params():
            self.amp = self.amplitude_spin.value()
            self.x_size = self.x_spin.value()
            self.y_size = self.y_spin.value()
            self.rand_noise = self.rand_check.checkState()

        self.amplitude_spin.valueChanged.connect(update_params)
        self.x_spin.valueChanged.connect(update_params)
        self.y_spin.valueChanged.connect(update_params)
        self.rand_check.clicked.connect(update_params)

        self.setLayout(grid)

        self.show()

# Launch the application
app = QtGui.QApplication(sys.argv)
ex = ThreeDPlot()
sys.exit(app.exec_())
