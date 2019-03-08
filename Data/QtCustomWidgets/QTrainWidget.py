from PyQt5.QtWidgets import *
from Data.Trainer import Threader


class QTrainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ===DATASETS COMBOBOX===
        self.datasets_Label = QLabel(self)
        self.datasets_Label.setText("Datasets:")
        self.datasets_Label.setGeometry(4, 4, 40, 15)
        self.datasets_ComboBox = QComboBox(self)
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.setGeometry(self.datasets_Label.width() + self.datasets_Label.x() + 4, self.datasets_Label.y(), 110, 15)

        # ===USER INPUT EPOCH===
        self.inputEpochs_Label = QLabel(self)
        self.inputEpochs_Label.setText("Desired Epochs:")
        self.inputEpochs_Label.setGeometry(4, 23, 65, 15)
        self.inputEpochs_Textbox = QTextEdit(self)
        self.inputEpochs_Textbox.setGeometry(self.inputEpochs_Label.width() + self.inputEpochs_Label.x() + 4, self.inputEpochs_Label.y(), 60, 15)

        # ===EPOCH ETA BOX===
        self.calculatedEstimation_Label = QLabel(self)
        self.calculatedEstimation_Label.setText("Epoch ETA:")
        self.calculatedEstimation_Label.setGeometry(34, 42, 45, 15)
        self.calculatedEstimation_TextBox = QTextEdit(self)
        self.calculatedEstimation_TextBox.setReadOnly(True)
        self.calculatedEstimation_TextBox.setGeometry(self.calculatedEstimation_Label.width() + self.calculatedEstimation_Label.x() + 4, self.calculatedEstimation_Label.y(), 60, 15)

        # ===EPOCHS PROGRESS BAR===
        self.epoch_PBLabel = QLabel(self)
        self.epoch_PBLabel.setText("Epochs:")
        self.epoch_PBLabel.setGeometry(34, 63, 30, 15)
        self.epoch_ProgressBar = QProgressBar(self)
        self.epoch_ProgressBar.setMaximum(100)
        self.epoch_ProgressBar.setGeometry(self.epoch_PBLabel.width() + self.epoch_PBLabel.x() + 4, self.epoch_PBLabel.y(), 120, 15)

        # ===CALCULATION ESTIMATION BOX===
        self.calculatedEstimation_Label = QLabel(self)
        self.calculatedEstimation_Label.setText("Completion ETA:")
        self.calculatedEstimation_Label.setGeometry(34, 86, 65, 15)
        self.calculatedEstimation_TextBox = QTextEdit(self)
        self.calculatedEstimation_TextBox.setReadOnly(True)
        self.calculatedEstimation_TextBox.setGeometry(self.calculatedEstimation_Label.width() + self.calculatedEstimation_Label.x() + 4, self.calculatedEstimation_Label.y(), 60, 15)

        # ===STEPS PROGRESS BAR===
        self.stepsPB_Label = QLabel(self)
        self.stepsPB_Label.setText("Steps:")
        self.stepsPB_Label.setGeometry(34, 105, 25, 15)
        self.steps_ProgressBar = QProgressBar(self)
        self.steps_ProgressBar.setMaximum(100)
        self.steps_ProgressBar.setGeometry(self.stepsPB_Label.width() + self.stepsPB_Label.x() + 4, self.stepsPB_Label.y(), 120, 15)

        # ===OUTPUT LOG===
        #self.output_Label = QLabel(self)
        #self.output_Label.setText("Loss output" + str(self.width()))
        #self.output_Label.move(200, 4)
        self.outputLog_TextBox = QTextEdit(self)
        self.outputLog_TextBox.setReadOnly(True)
        self.outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLog_TextBox.verticalScrollBar()
        self.outputLog_TextBox.setGeometry(200, 4, self.width() - (self.outputLog_TextBox.x() + 4), self.height() - (self.outputLog_TextBox.y() + 4))

        # ===TRAIN BUTTON===
        self.train_Button = QPushButton('Train', self)
        self.train_Button.setToolTip('Athena Trainer')
        self.train_Button.setGeometry(4, 124, 90, 30)
        self.train_Button.clicked.connect(Threader.createThread)
        # Trainer Button rework MARCH 1ST 2019
        # self.trainingTimer = QBasicTimer()  # Declare a timer for timing the training process
        # self.timerStep = 0  # STEPS OF TIMER NOT GAN

    def resizeEvent(self, *args, **kwargs):
        for child in self.children():
            if child == self.outputLog_TextBox:
                child.setGeometry(child.x(), child.y(), self.width() - (child.x() + 4), self.height() - (child.y() + 4))

    def updateLog(self, stringToUpdate):
        self.outputLog_TextBox.append(self, stringToUpdate)