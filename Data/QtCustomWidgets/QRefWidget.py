from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui


class QRefWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        self.datasets_Label = QLabel(self)
        self.datasets_Label.setText("Datasets:")
        self.datasets_Label.setGeometry(4, 4, self.datasets_Label.fontMetrics().boundingRect(
            self.datasets_Label.text()).width(), 15)

    def setGeometry(self, *__args):
        QWidget.setGeometry(self, *__args)

    def paintEvent(self, event):
        super(QRefWidget, self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QtGui.QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_Widget, styleSheet, paint, self)