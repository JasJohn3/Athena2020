from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class QResultsWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.initUI()


    def initUI(self):


        self.trainingSet_Label = QLabel(self)
        self.trainingSet_Label.setText("Training set")
        self.trainingSet_Label.move(15,35)
        self.trainingImage = QLabel(self)
        pixmapTrained = QPixmap("real_samples.png")
        self.trainingImage.setPixmap(pixmapTrained)
        self.trainingImage.move(15,50)
        
        self.producedSet_Label = QLabel(self)
        self.producedSet_Label.setText("Generated set")
        self.producedSet_Label.move(15, 605)
        self.producedImg = QLabel(self)
        pixmapGenerated = QPixmap("fake_samples_epoch_000.png")
        self.producedImg.setPixmap(pixmapGenerated)
        self.producedImg.move(15, 625)

    def refresh(self):
        placeholder = "placeholder"


