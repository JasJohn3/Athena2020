from PyQt5.QtWidgets import *
import Training

class QTrainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ===EPOCHS PROGRESS BAR===
        self.epoch_PBLabel = QLabel(self)
        self.epoch_PBLabel.setText("Epochs:")
        self.epoch_PBLabel.move(20, 295)
        self.epoch_ProgressBar = QProgressBar(self)
        self.epoch_ProgressBar.setMaximum(100)
        self.epoch_ProgressBar.setGeometry(0, 0, 300, 25)
        self.epoch_ProgressBar.move(75, 300)

        # ===STEPS PROGRESS BAR===
        self.stepsPB_Label = QLabel(self)
        self.stepsPB_Label.setText("Steps:")
        self.stepsPB_Label.move(20, 245)
        self.steps_ProgressBar = QProgressBar(self)
        self.steps_ProgressBar.setMaximum(100)
        self.steps_ProgressBar.setGeometry(0, 0, 300, 25)
        self.steps_ProgressBar.move(75, 250)

        # ===OUTPUT LOG===
        self.output_Label = QLabel(self)
        self.output_Label.setText("Loss output ")
        self.output_Label.move(375, 20)
        self.outputLog_TextBox = QTextEdit(self)
        self.outputLog_TextBox.setReadOnly(True)
        self.outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLog_TextBox.verticalScrollBar()
        self.outputLog_TextBox.resize(250, 260)
        self.outputLog_TextBox.move(375, 50)

        # ===DATASETS COMBOBOX===
        self.datasets_Label = QLabel(self)
        self.datasets_Label.setText("Datasets: ")
        self.datasets_Label.move(25, 50)
        self.datasets_ComboBox = QComboBox(self)
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.move(75, 50)
        self.datasets_ComboBox.resize(110, 30)

        # ===USER INPUT EPOCH===
        self.inputEpochs_Label = QLabel(self)
        self.inputEpochs_Label.setText("Desired Epochs: ")
        self.inputEpochs_Label.move(25, 100)
        self.inputEpochs_Textbox = QTextEdit(self)
        self.inputEpochs_Textbox.move(110, 100)

        # ===EPOCH ETA BOX===
        self.calculatedEstimation_Label = QLabel(self)
        self.calculatedEstimation_Label.setText("Epoch ETA: ")
        self.calculatedEstimation_Label.move(160, 150)
        self.calculatedEstimation_TextBox = QTextEdit(self)
        self.calculatedEstimation_TextBox.setReadOnly(True)
        self.calculatedEstimation_TextBox.move(240, 150)

        # ===CALCULATION ESTIMATION BOX===
        self.calculatedEstimation_Label = QLabel(self)
        self.calculatedEstimation_Label.setText("Completion ETA: ")
        self.calculatedEstimation_Label.move(160, 215)
        self.calculatedEstimation_TextBox = QTextEdit(self)
        self.calculatedEstimation_TextBox.setReadOnly(True)
        self.calculatedEstimation_TextBox.move(240, 215)

        # ===TRAIN BUTTON===
        self.train_Button = QPushButton('Train', self)
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