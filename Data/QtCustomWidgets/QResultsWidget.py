from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt

class QResultsWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.imageConv = QPixmap()
        self.imageConv_1 = QPixmap()
        self.signal = True
        self.initUI()

    def initUI(self):
        self.label_trained = QLabel(self)
        self.label_trained.setText("Training Set")
        self.image_trained = QLabel(self)

        self.label_created = QLabel(self)
        self.label_created.setText("Generated Set")
        self.image_created = QLabel(self)

    # Add Image to the QResults Widget from emitted images in QTrainWidget
    def addImage(self, Image):
        # Alternate emit signals to corresponding label
        if self.signal:
            # Hold and convert pass Pillow image to Pyqt format image
            self.imageConv = ImageQt(Image)
            # Save Qpixmap image of image
            self.pixmapTrained = QPixmap.fromImage(self.imageConv).scaled(self.image_trained.width(), self.image_trained.height(), Qt.KeepAspectRatio)
            # Set label to new Qpixmap
            self.image_trained.setPixmap(self.pixmapTrained)
        else:
            # Hold and convert pass Pillow image to Pyqt format image
            self.imageConv_1 = ImageQt(Image)
            # Save Qpixmap image of image
            self.pixmapGenerated = QPixmap.fromImage(self.imageConv_1).scaled(self.image_created.width(), self.image_created.height(), Qt.KeepAspectRatio)
            # Set label to new Qpixmap
            self.image_created.setPixmap(self.pixmapGenerated)
        # Swap emitted signal for label setting
        self.signal = not self.signal

    def resizeEvent(self, QResizeEvent):
        # Resize/center Trained image label & image
        self.label_trained.setGeometry(4, 4, self.width() - 8, 15)
        self.label_trained.setAlignment(Qt.AlignCenter)
        self.image_trained.resize(self.height()/2 - 27, self.height()/2 - 27)
        self.image_trained.move(self.width()/2 - self.image_trained.width()/2, self.label_trained.height() + self.label_trained.y() + 4)
        if type(self.imageConv) != QPixmap:
            self.image_trained.setPixmap(QPixmap.fromImage(self.imageConv).scaled(self.image_trained.width(), self.image_trained.height(), Qt.KeepAspectRatio))
        # Resize/center Created image label & image
        self.label_created.setGeometry(4, self.image_trained.height() + self.image_trained.y() + 8, self.width() - 8, 15)
        self.label_created.setAlignment(Qt.AlignCenter)
        self.image_created.resize(self.height()/2 - 27, self.height()/2 - 27)
        self.image_created.move(self.width()/2 - self.image_created.width()/2, self.label_created.height() + self.label_created.y() + 4)
        if type(self.imageConv_1) != QPixmap:
            self.image_created.setPixmap(QPixmap.fromImage(self.imageConv_1).scaled(self.image_created.width(), self.image_created.height(), Qt.KeepAspectRatio))

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)

# 23
# # image
# # 27
# # image
# # 4