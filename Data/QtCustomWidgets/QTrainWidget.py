from PyQt5.QtWidgets import *
from Data.Trainer.Epoch import Trainer

class QTrainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ===DATASETS COMBOBOX===
        self.datasets_Label = QLabel(self)
        self.datasets_Label.setText("Datasets:")
        self.datasets_Label.setToolTip("Your dataset or a custom dataset")
        self.datasets_Label.setGeometry(4, 4, self.datasets_Label.fontMetrics().boundingRect(self.datasets_Label.text()).width(), 15)
        self.datasets_ComboBox = QComboBox(self)
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.setGeometry(self.datasets_Label.width() + self.datasets_Label.x() + 4, self.datasets_Label.y(), 110, 15)

        # ===USER INPUT EPOCH===
        self.inputEpochs_Label = QLabel(self)
        self.inputEpochs_Label.setText("Desired Epochs:")
        self.inputEpochs_Label.setGeometry(4, 23, self.inputEpochs_Label.fontMetrics().boundingRect(self.inputEpochs_Label.text()).width(), 15)
        self.inputEpochs_SB = QSpinBox(self)
        self.inputEpochs_SB.setMinimum(1)
        self.inputEpochs_SB.setGeometry(self.inputEpochs_Label.width() + self.inputEpochs_Label.x() + 4, self.inputEpochs_Label.y(), 60, 15)

        # ===EPOCH ETA BOX===
        self.epochETA_Label = QLabel(self)
        self.epochETA_Label.setText("Epoch ETA:")
        self.epochETA_Label.setGeometry(34, 42, self.epochETA_Label.fontMetrics().boundingRect(self.epochETA_Label.text()).width(), 15)
        self.epochETA_Display = QLabel(self)
        self.epochETA_Display.setGeometry(self.epochETA_Label.width() + self.epochETA_Label.x() + 4, self.epochETA_Label.y(), 60, 15)

        # ===STEPS PROGRESS BAR===
        self.stepsPB_Label = QLabel(self)
        self.stepsPB_Label.setText("Steps:")
        self.stepsPB_Label.setGeometry(34, 63, self.stepsPB_Label.fontMetrics().boundingRect(self.stepsPB_Label.text()).width(), 15)
        self.steps_ProgressBar = QProgressBar(self)
        self.steps_ProgressBar.setTextVisible(False)
        self.steps_ProgressBar.setGeometry(self.stepsPB_Label.width() + self.stepsPB_Label.x() + 4, self.stepsPB_Label.y(), 120, 15)

        # ===CALCULATION ESTIMATION BOX===
        self.completionETA_Label = QLabel(self)
        self.completionETA_Label.setText("Completion ETA:")
        self.completionETA_Label.setGeometry(34, 86, self.completionETA_Label.fontMetrics().boundingRect(self.completionETA_Label.text()).width(), 15)
        self.completionETA_Display = QLabel(self)
        self.completionETA_Display.setGeometry(self.completionETA_Label.width() + self.completionETA_Label.x() + 4, self.completionETA_Label.y(), 60, 15)

        # ===EPOCHS PROGRESS BAR===
        self.epoch_PBLabel = QLabel(self)
        self.epoch_PBLabel.setText("Epochs:")
        self.epoch_PBLabel.setGeometry(34, 105, self.epoch_PBLabel.fontMetrics().boundingRect(self.epoch_PBLabel.text()).width(), 15)
        self.epoch_ProgressBar = QProgressBar(self)
        self.epoch_ProgressBar.setTextVisible(False)
        self.epoch_ProgressBar.setGeometry(self.epoch_PBLabel.width() + self.epoch_PBLabel.x() + 4, self.epoch_PBLabel.y(), 120, 15)

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
        self.train_Button.clicked.connect(self.train)
        # Trainer Button rework MARCH 1ST 2019
        # self.trainingTimer = QBasicTimer()  # Declare a timer for timing the training process
        # self.timerStep = 0  # STEPS OF TIMER NOT GAN

    def resizeEvent(self, *args, **kwargs):
        for child in self.children():
            if child == self.outputLog_TextBox:
                child.setGeometry(child.x(), child.y(), self.width() - (child.x() + 4), self.height() - (child.y() + 4))

    def train(self):
        self.epochs_Thread = Trainer(self.inputEpochs_SB.text())
        self.epochs_Thread.logSignal.connect(self.outputLog_TextBox.append)
        self.epochs_Thread.stepSignal.connect(self.steps_ProgressBar.setValue)
        self.epochs_Thread.epochSignal.connect(self.epoch_ProgressBar.setValue)
        self.epochs_Thread.maxstepsSignal.connect(self.steps_ProgressBar.setMaximum)
        self.epochs_Thread.maxepochsSignal.connect(self.epoch_ProgressBar.setMaximum)
        self.epochs_Thread.epochtimeSignal.connect(self.epochETA_Display.setText)
        self.epochs_Thread.totaltimeSignal.connect(self.completionETA_Display.setText)
        self.epochs_Thread.start()