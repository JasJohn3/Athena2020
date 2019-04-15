from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QPainter

# Custom message dialog
class ScrollMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        # Load in parent clss
        QMessageBox.__init__(self, *args, **kwargs)

        # Add scroll area
        scroll = QScrollArea(self)
        # Set scroll area resizable
        scroll.setWidgetResizable(True)

        # Widget to hold the content
        self.content = QWidget()
        # Set widget to scroll area
        scroll.setWidget(self.content)
        # create layout for content
        self.grid = QVBoxLayout(self.content)

        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setStyleSheet("QScrollArea{min-width:300 px; min-height: 300px}")

    def setText(self, p_str):
        label = QLabel(p_str, self)
        label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.grid.addWidget(label)

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)