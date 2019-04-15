from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter

class QElapsedTimeWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        self.noDataLabel = QLabel(self)
        self.noDataLabel.setText("No data received...")

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)