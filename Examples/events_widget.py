from PySide import QtGui, QtCore
import sys

class EventWidget(QtGui.QWidget):
    def __init__(self):
        super(EventWidget, self).__init__()
        self.setWindowTitle('Event WIdget')
        self.show()

    def resizeEvent(self, event):
        print event.size()

    def mousePressEvent(self, event):
        print event.button()

    def keyPressEvent(self, event):
        print event.text()

    def moveEvent(self, event):
        print event.pos()

    def closeEvent(self, event):
        print 'Widget Closed'
# Launch the application
app = QtGui.QApplication(sys.argv)
ex = EventWidget()
sys.exit(app.exec_())
