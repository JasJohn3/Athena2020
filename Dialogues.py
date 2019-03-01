from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QDesktopServices, QColor
from PyQt5.QtCore import QUrl, QBasicTimer
import sys
import Training
import threading


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

        # ===EPOCHS PROGRESS BAR===
        epoch_PBLabel = QLabel(self)
        epoch_PBLabel.setText("Epochs:")
        epoch_PBLabel.move(20, 295)
        epoch_ProgressBar = QProgressBar(self)
        epoch_ProgressBar.setMaximum(100)
        epoch_ProgressBar.setGeometry(0, 0, 300, 25)
        epoch_ProgressBar.move(75, 300)

        # ===STEPS PROGRESS BAR===
        stepsPB_Label = QLabel(self)
        stepsPB_Label.setText("Steps:")
        stepsPB_Label.move(20, 245)
        steps_ProgressBar = QProgressBar(self)
        steps_ProgressBar.setMaximum(100)
        steps_ProgressBar.setGeometry(0, 0, 300, 25)
        steps_ProgressBar.move(75, 250)

        # ===OUTPUT LOG===
        self.output_Label = QLabel(self)
        self.output_Label.setText("Loss output ")
        self.output_Label.move(375, 20)
        self.outputLog_TextBox = QTextEdit(self)
        self.outputLog_TextBox.setReadOnly(True)
        self.outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLog_TextBox.verticalScrollBar()
        self.outputLog_TextBox.resize(250,260)
        self.outputLog_TextBox.move(375,50)

        # ===DATASETS COMBOBOX===
        datasets_Label = QLabel(self)
        datasets_Label.setText("Datasets: ")
        datasets_Label.move(25, 50)
        datasets_ComboBox = QComboBox(self)
        datasets_ComboBox.addItem("<Your Datasets>")
        datasets_ComboBox.move(75,50)
        datasets_ComboBox.resize(110, 30)

        # ===USER INPUT EPOCH===
        inputEpochs_Label = QLabel(self)
        inputEpochs_Label.setText("Desired Epochs: ")
        inputEpochs_Label.move(25, 100)
        inputEpochs_Textbox = QTextEdit(self)
        inputEpochs_Textbox.move(110, 100)

        # ===EPOCH ETA BOX===
        calculatedEstimation_Label = QLabel(self)
        calculatedEstimation_Label.setText("Epoch ETA: ")
        calculatedEstimation_Label.move(160, 150)
        calculatedEstimation_TextBox = QTextEdit(self)
        calculatedEstimation_TextBox.setReadOnly(True)
        calculatedEstimation_TextBox.move(240, 150)

        # ===CALCULATION ESTIMATION BOX===
        calculatedEstimation_Label = QLabel(self)
        calculatedEstimation_Label.setText("Completion ETA: ")
        calculatedEstimation_Label.move(160, 215)
        calculatedEstimation_TextBox = QTextEdit(self)
        calculatedEstimation_TextBox.setReadOnly(True)
        calculatedEstimation_TextBox.move(240, 215)

        # ===TRAIN BUTTON===
        self.train_Button = QPushButton('Train', self)
        self.train_Button.setToolTip('Athena Training')
        self.train_Button.move(500, 350)
        self.train_Button.clicked.connect(self.on_click)
        #Training Button rework MARCH 1ST 2019
        #self.trainingTimer = QBasicTimer()  # Declare a timer for timing the training process
        #self.timerStep = 0  # STEPS OF TIMER NOT GAN

    def on_click(self):
        #====CHANGE BUTTON TEXT=====
        #if self.trainingTimer.isActive():
         #   self.trainingTimer.stop()
          #  self.train_Button.setText('TRAIN')
        #else:
         #   self.trainingTimer.start(100, self)
          #  self.train_Button.setText('TRAINING')
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
        # JasonLink.move(50,50)

        TrevorLink = QLabel(self)
        TrevorLink.linkActivated.connect(self.link)
        TrevorLink.setText('<a href="https://trekinar.wixsite.com/portfolio">Trevor Kinard</a>')
        TrevorLink.move(50,100)

        ZackLink = QLabel(self)
        ZackLink.linkActivated.connect(self.link)
        ZackLink.setText('<a href="https://overclockedthompson.wixsite.com/mysite">Zack Thompson</a>')
        ZackLink.move(50, 150)

        # WyattLink = QLabel(self)
        # WyattLink.linkActivated.connect(self.link)
        # WyattLink.setText("<Insert link here>")
        # WyattLink.move(50,200)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('CSS.cfg').read())
    trainingDialogue = TrainingDialogue()
    trainingDialogue.show()
    aboutDevelopers = AboutDevs()
    aboutDevelopers.show()
    sys.exit(app.exec_())