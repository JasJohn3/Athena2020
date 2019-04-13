from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

class QResultsWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.signal = True
        self.initUI()

    def initUI(self):
        self.trainingSet_Label = QLabel(self)
        self.trainingSet_Label.setText("Training set")
        self.trainingSet_Label.move(15,35)
        self.trainingImage = QLabel(self)
        self.trainingImage.resize(530, 530)
        self.trainingImage.move(15,50)

        self.producedSet_Label = QLabel(self)
        self.producedSet_Label.setText("Generated set")
        self.producedSet_Label.move(15, 605)
        self.producedImg = QLabel(self)
        self.producedImg.resize(530, 530)
        # Previous location (15, 625)
        self.producedImg.move(15, 100)

    # Add Image to the QResults Widget from emitted images in QTrainWidget
    def addImage(self, Image):
        # Alternate emit signals to corresponding label
        if self.signal:
            # Hold and convert pass Pillow image to Pyqt format image
            self.imageConv = ImageQt(Image)
            # Save Qpixmap image of image
            self.pixmapTrained = QPixmap.fromImage(self.imageConv)
            # Set label to new Qpixmap
            self.trainingImage.setPixmap(self.pixmapTrained)
        else:
            # Hold and convert pass Pillow image to Pyqt format image
            self.imageConv_1 = ImageQt(Image)
            # Save Qpixmap image of image
            self.pixmapGenerated = QPixmap.fromImage(self.imageConv_1)
            # Set label to new Qpixmap
            self.producedImg.setPixmap(self.pixmapGenerated)
        # Swap emitted signal for label setting
        self.signal = not self.signal


    def refresh(self):
        placeholder = "placeholder"


