from PySide import QtGui, QtCore
import sys

class simpleWidget(QtGui.QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        self.setWindowTitle('First WIdget')
        self.show()

    def resizeEvent(self, event):
        print event.size()

    def mousePressEvent(self, event):
        print event.button()

    def keyPressEvent(self, event):
        print event.key()

    def moveEvent(self, event):
        print event.pos()

    def moveEvent(self, event):
        print event.pos()

    def closeEvent(self, event):
        print 'Widget Closed'
# Launch the application
app = QtGui.QApplication(sys.argv)
ex = simpleWidget()
sys.exit(app.exec_())
