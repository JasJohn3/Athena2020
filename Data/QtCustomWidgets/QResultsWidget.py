from PyQt5.QtWidgets import *

class QResultsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.introductionLabel = QLabel(self)
        self.introductionLabel.setText("Your results!")

        self.resultsPane_canvas = QWidget(self)
        self.resultsPane_options = QWidget(self)
        self.resultsPane_options