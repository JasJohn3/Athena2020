from PyQt5.QtWidgets import *

class QEEGWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.noDataLabel = QLabel(self)
        self.noDataLabel.setText("No data received...")