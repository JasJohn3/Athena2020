from PyQt5.QtWidgets import *

class QHistogramWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.introduction_Label = QLabel(self)
        self.introduction_Label.setText("No training data received...")

