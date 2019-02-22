from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QDesktopServices, QColor
from PyQt5.QtCore import QUrl
import sys
import Training


''' ==========================================TRAINING DIALOGUE WINDOW========================================= '''
class TrainingDialogue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Model Training'
        self.left = 520
        self.top = 280
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        epoch_PBLabel = QLabel(self)
        epoch_PBLabel.setText("Epochs:")
        epoch_PBLabel.move(20, 50)
        epoch_ProgressBar = QProgressBar(self)
        epoch_ProgressBar.setMaximum(100)
        epoch_ProgressBar.setGeometry(0, 0, 300, 25)
        epoch_ProgressBar.move(75, 50)

        stepsPB_Label = QLabel(self)
        stepsPB_Label.setText("Steps:")
        stepsPB_Label.move(20, 100)
        steps_ProgressBar = QProgressBar(self)
        steps_ProgressBar.setMaximum(100)
        steps_ProgressBar.setGeometry(0, 0, 300, 25)
        steps_ProgressBar.move(75, 100)


        output_Label = QLabel(self)
        output_Label.setText("Loss output ")
        output_Label.move(375, 20)
        outputLog_TextBox = QTextEdit(self)
        outputLog_TextBox.setReadOnly(True)
        outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        outputLog_TextBox.verticalScrollBar()
        outputLog_TextBox.resize(250,260)
        outputLog_TextBox.move(375,50)


        datasets_Label = QLabel(self)
        datasets_Label.setText("Datasets: ")
        datasets_Label.move(25, 150)
        datasets_ComboBox = QComboBox(self)
        datasets_ComboBox.addItem("<Your Datasets>")
        datasets_ComboBox.move(110,150)

        calculatedEstimation_Label = QLabel(self)
        calculatedEstimation_Label.setText("Calculated ETA: ")
        calculatedEstimation_Label.move(25, 250)
        calculatedEstimation_TextBox = QTextEdit(self)
        calculatedEstimation_TextBox.setReadOnly(True)
        calculatedEstimation_TextBox.move(110, 250)


        train_Button = QPushButton('Train', self)
        train_Button.setToolTip('Athena Training')
        train_Button.move(500, 350)
        train_Button.clicked.connect(self.on_click)

    def on_click(self):
        Training.Train()

''' ==========================================ABOUT DEVELOPERS DIALOGUE WINDOW========================================= '''
class AboutDevs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'About The Developers!'
        self.left = 520
        self.top = 280
        self.width = 640
        self.height = 400
        self.initUI()

    #Allows for linking to personal websites of developers.
    def link(self, linkstr):
        QDesktopServices.openUrl(QUrl(linkstr))

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setAutoFillBackground(True)
        colorPalette = self.palette()
        colorPalette.setColor(self.backgroundRole(),
                                                QColor(28, 28, 28))  # set background color to black.
        self.setPalette(colorPalette)

        greetingLabel = QLabel(self)
        greetingLabel.setGeometry(170, 50, 300, 50)
        greetingLabel.setText("<font color = white>About the developers: Click a link to visit their portfolio sites!</font>")

        # JasonLink = QLabel(self)
        # JasonLink.linkActivated.connect(self.link)
        # JasonLink.setText("<Insert link here>")
        # JasonLink.move(100,50)

        TrevorLink = QLabel(self)
        TrevorLink.linkActivated.connect(self.link)
        TrevorLink.setText('<a href="https://trekinar.wixsite.com/portfolio">Trevor Kinard</a>')
        TrevorLink.move(50,100)

        ZackLink = QLabel(self)
        ZackLink.linkActivated.connect(self.link)
        ZackLink.setText('<a href="https://overclockedthompson.wixsite.com/mysite">Zack Thompson</a>')
        ZackLink.move(50, 150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    td = TrainingDialogue()
    td.show()
    ad = AboutDevs()
    ad.show()
    sys.exit(app.exec_())