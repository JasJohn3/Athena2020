from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QDesktopServices, QColor
from PyQt5.QtCore import QUrl, QBasicTimer
import sys
import Training
import threading

''' ==========================================TRAINING DIALOGUE WINDOW========================================= '''
class Train:
    def __init__(self, tab):
        self.tab = createTab(tab, "Model Training")
        self.initUI()

    def initUI(self):
        # ===EPOCHS PROGRESS BAR===
        self.epoch_PBLabel = QLabel(self.tab)
        self.epoch_PBLabel.setText("Epochs:")
        self.epoch_PBLabel.move(20, 295)
        self.epoch_ProgressBar = QProgressBar(self.tab)
        self.epoch_ProgressBar.setMaximum(100)
        self.epoch_ProgressBar.setGeometry(0, 0, 300, 25)
        self.epoch_ProgressBar.move(75, 300)

        # ===STEPS PROGRESS BAR===
        self.stepsPB_Label = QLabel(self.tab)
        self.stepsPB_Label.setText("Steps:")
        self.stepsPB_Label.move(20, 245)
        self.steps_ProgressBar = QProgressBar(self.tab)
        self.steps_ProgressBar.setMaximum(100)
        self.steps_ProgressBar.setGeometry(0, 0, 300, 25)
        self.steps_ProgressBar.move(75, 250)

        # ===OUTPUT LOG===
        self.output_Label = QLabel(self.tab)
        self.output_Label.setText("Loss output ")
        self.output_Label.move(375, 20)
        self.outputLog_TextBox = QTextEdit(self.tab)
        self.outputLog_TextBox.setReadOnly(True)
        self.outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLog_TextBox.verticalScrollBar()
        self.outputLog_TextBox.resize(250, 260)
        self.outputLog_TextBox.move(375, 50)

        # ===DATASETS COMBOBOX===
        self.datasets_Label = QLabel(self.tab)
        self.datasets_Label.setText("Datasets: ")
        self.datasets_Label.move(25, 50)
        self.datasets_ComboBox = QComboBox(self.tab)
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.move(75, 50)
        self.datasets_ComboBox.resize(110, 30)

        # ===USER INPUT EPOCH===
        self.inputEpochs_Label = QLabel(self.tab)
        self.inputEpochs_Label.setText("Desired Epochs: ")
        self.inputEpochs_Label.move(25, 100)
        self.inputEpochs_Textbox = QTextEdit(self.tab)
        self.inputEpochs_Textbox.move(110, 100)

        # ===EPOCH ETA BOX===
        self.calculatedEstimation_Label = QLabel(self.tab)
        self.calculatedEstimation_Label.setText("Epoch ETA: ")
        self.calculatedEstimation_Label.move(160, 150)
        self.calculatedEstimation_TextBox = QTextEdit(self.tab)
        self.calculatedEstimation_TextBox.setReadOnly(True)
        self.calculatedEstimation_TextBox.move(240, 150)

        # ===CALCULATION ESTIMATION BOX===
        self.calculatedEstimation_Label = QLabel(self.tab)
        self.calculatedEstimation_Label.setText("Completion ETA: ")
        self.calculatedEstimation_Label.move(160, 215)
        self.calculatedEstimation_TextBox = QTextEdit(self.tab)
        self.calculatedEstimation_TextBox.setReadOnly(True)
        self.calculatedEstimation_TextBox.move(240, 215)

        # ===TRAIN BUTTON===
        self.train_Button = QPushButton('Train', self.tab)
        self.train_Button.setToolTip('Athena Training')
        self.train_Button.move(500, 350)
        self.train_Button.clicked.connect(self.on_click)
        # Training Button rework MARCH 1ST 2019
        # self.trainingTimer = QBasicTimer()  # Declare a timer for timing the training process
        # self.timerStep = 0  # STEPS OF TIMER NOT GAN

    def updateLog(self, stringToUpdate):
        self.outputLog_TextBox.append(self, stringToUpdate)

    def on_click(self):
        # ====CHANGE BUTTON TEXT=====
        # if self.trainingTimer.isActive():
        #   self.trainingTimer.stop()
        #  self.train_Button.setText('TRAIN')
        # else:
        #   self.trainingTimer.start(100, self)
        #  self.train_Button.setText('TRAINING')
        Training.Train()


''' ==========================================ABOUT DEVELOPERS DIALOGUE WINDOW========================================= '''
class AboutDev:
    def __init__(self):
        self.title = 'About The Developers!'
        self.left = 520
        self.top = 280
        self.width = 640
        self.height = 400
        self.initUI()

    # Allows for linking to personal websites of developers.
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
        greetingLabel.setText(
            "<font color = white>About the developers: Click a link to visit their portfolio sites!</font>")

        # JasonLink = QLabel(self)
        # JasonLink.linkActivated.connect(self.link)
        # JasonLink.setText("<Insert link here>")
        # JasonLink.move(50,50)

        TrevorLink = QLabel(self)
        TrevorLink.linkActivated.connect(self.link)
        TrevorLink.setText('<a href="https://trekinar.wixsite.com/portfolio">Trevor Kinard</a>')
        TrevorLink.move(50, 100)

        ZackLink = QLabel(self)
        ZackLink.linkActivated.connect(self.link)
        ZackLink.setText('<a href="https://overclockedthompson.wixsite.com/mysite">Zack Thompson</a>')
        ZackLink.move(50, 150)

        # WyattLink = QLabel(self)
        # WyattLink.linkActivated.connect(self.link)
        # WyattLink.setText("<Insert link here>")
        # WyattLink.move(50,200)


def train(self):
    tab = createTab(self, "Model Training")

    # ===EPOCHS PROGRESS BAR===
    epoch_PBLabel = QLabel(tab)
    epoch_PBLabel.setText("Epochs:")
    epoch_PBLabel.move(20, 295)
    epoch_ProgressBar = QProgressBar(tab)
    epoch_ProgressBar.setMaximum(100)
    epoch_ProgressBar.setGeometry(0, 0, 300, 25)
    epoch_ProgressBar.move(75, 300)

    # ===STEPS PROGRESS BAR===
    stepsPB_Label = QLabel(tab)
    stepsPB_Label.setText("Steps:")
    stepsPB_Label.move(20, 245)
    steps_ProgressBar = QProgressBar(tab)
    steps_ProgressBar.setMaximum(100)
    steps_ProgressBar.setGeometry(0, 0, 300, 25)
    steps_ProgressBar.move(75, 250)

    # ===OUTPUT LOG===
    output_Label = QLabel(tab)
    output_Label.setText("Loss output ")
    output_Label.move(375, 20)
    outputLog_TextBox = QTextEdit(tab)
    outputLog_TextBox.setReadOnly(True)
    outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
    outputLog_TextBox.verticalScrollBar()
    outputLog_TextBox.resize(250, 260)
    outputLog_TextBox.move(375, 50)

    # ===DATASETS COMBOBOX===
    datasets_Label = QLabel(tab)
    datasets_Label.setText("Datasets: ")
    datasets_Label.move(25, 50)
    datasets_ComboBox = QComboBox(tab)
    datasets_ComboBox.addItem("<Your Datasets>")
    datasets_ComboBox.move(75, 50)
    datasets_ComboBox.resize(110, 30)

    # ===USER INPUT EPOCH===
    inputEpochs_Label = QLabel(tab)
    inputEpochs_Label.setText("Desired Epochs: ")
    inputEpochs_Label.move(25, 100)
    inputEpochs_Textbox = QTextEdit(tab)
    inputEpochs_Textbox.move(110, 100)

    # ===EPOCH ETA BOX===
    calculatedEstimation_Label = QLabel(tab)
    calculatedEstimation_Label.setText("Epoch ETA: ")
    calculatedEstimation_Label.move(160, 150)
    calculatedEstimation_TextBox = QTextEdit(tab)
    calculatedEstimation_TextBox.setReadOnly(True)
    calculatedEstimation_TextBox.move(240, 150)

    # ===CALCULATION ESTIMATION BOX===
    calculatedEstimation_Label = QLabel(tab)
    calculatedEstimation_Label.setText("Completion ETA: ")
    calculatedEstimation_Label.move(160, 215)
    calculatedEstimation_TextBox = QTextEdit(tab)
    calculatedEstimation_TextBox.setReadOnly(True)
    calculatedEstimation_TextBox.move(240, 215)

    # ===TRAIN BUTTON===
    train_Button = QPushButton('Train', tab)
    train_Button.setToolTip('Athena Training')
    train_Button.move(500, 350)
    train_Button.clicked.connect(on_click)

def aboutDev(self):
    self = createTab(self, "About The Developers!")

    greetingLabel = QLabel(self)
    greetingLabel.setGeometry(170, 50, 300, 50)
    greetingLabel.setText(
        "<font color = white>About the developers: Click a link to visit their portfolio sites!</font>")

    # JasonLink = QLabel(self)
    # JasonLink.linkActivated.connect(self.link)
    # JasonLink.setText("<Insert link here>")
    # JasonLink.move(50,50)

    TrevorLink = QLabel(self)
    TrevorLink.linkActivated.connect(link)
    TrevorLink.setText('<a href="https://trekinar.wixsite.com/portfolio">Trevor Kinard</a>')
    TrevorLink.move(50, 100)

    ZackLink = QLabel(self)
    ZackLink.linkActivated.connect(link)
    ZackLink.setText('<a href="https://overclockedthompson.wixsite.com/mysite">Zack Thompson</a>')
    ZackLink.move(50, 150)

    # WyattLink = QLabel(self)
    # WyattLink.linkActivated.connect(self.link)
    # WyattLink.setText("<Insert link here>")
    # WyattLink.move(50,200)

def link(linkstr):
    QDesktopServices.openUrl(QUrl(linkstr))

def on_click():
    Training.Train()

def createTab(self, name):
    tab = QWidget(self.panel_tabs)
    tab.setStyleSheet("background-color: #1C1C1C;")
    self.panel_tabs.addTab(tab, name)
    return tab


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyleSheet(open('CSS.cfg').read())
#     td = TrainingDialogue()  # this does fuck all
#     td.show()  # this does fuck all
#     aboutDevelopers = AboutDevs()  # this does fuck all
#     aboutDevelopers.show()  # this does fuck all
#     sys.exit(app.exec_())
