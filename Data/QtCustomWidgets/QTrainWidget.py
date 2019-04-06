from PyQt5.QtWidgets import *
from Data.Trainer.Epoch import Trainer


"""
NOTE: Improvements as of March 24th are based on Pytorch tutorial at link below
https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html

Graphs will be implemented in the manner done by tutorial. 
"""

class QTrainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        #===SCROLL AREA===
        self.scrollBar = QScrollArea(self)
        self.scrollBar.setGeometry(0, self.height() - 15, self.width(), 15)
        self.scrollBar.setWidgetResizable(True)
        self.scrollContent = QWidget(self.scrollBar)
        self.scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scrollLayout)

        self.scrollBar.setWidget(self.scrollContent)

        def comboBoxChecker():
            currentSet = self.datasets_ComboBox.currentIndex()


        # ===DATASETS COMBOBOX===
        self.datasets_Label = QLabel(self)
        self.datasets_Label.setText("Datasets:")
        self.datasets_Label.setGeometry(4, 4, self.datasets_Label.fontMetrics().boundingRect(self.datasets_Label.text()).width(), 15)
        self.datasets_ComboBox = QComboBox(self)
        self.datasets_ComboBox.setToolTip("Your current uploaded datasets.")
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.addItem("cifar10")
        self.datasets_ComboBox.addItem("cifar100")
        self.datasets_ComboBox.addItem("mnist")
        self.datasets_ComboBox.addItem("stl10")
        self.datasets_ComboBox.addItem("lsun")
        self.datasets_ComboBox.addItem("imagenet")
        comboBoxChecker()
        self.datasets_ComboBox.setGeometry(self.datasets_Label.width() + self.datasets_Label.x() + 4, self.datasets_Label.y(), 110, 15)

        # ===USER INPUT EPOCH===
        self.inputEpochs_Label = QLabel(self)

        self.inputEpochs_Label.setText("Desired Epochs:")
        self.inputEpochs_Label.setGeometry(4, 43, self.inputEpochs_Label.fontMetrics().boundingRect(self.inputEpochs_Label.text()).width(), 15)
        self.inputEpochs_SB = QSpinBox(self)
        self.inputEpochs_SB.setMinimum(1)
        self.inputEpochs_SB.setGeometry(self.inputEpochs_Label.width() + self.inputEpochs_Label.x() + 4, self.inputEpochs_Label.y(), 60, 15)

        # ===EPOCH ETA BOX===
        self.epochETA_Label = QLabel(self)
        self.epochETA_Label.setText("Epoch ETA:")
        self.epochETA_Label.setGeometry(34, 86, self.epochETA_Label.fontMetrics().boundingRect(self.epochETA_Label.text()).width(), 15)
        self.epochETA_Display = QLabel(self)
        self.epochETA_Display.setGeometry(self.epochETA_Label.width() + self.epochETA_Label.x() + 4, self.epochETA_Label.y(), 60, 15)

        # ===STEPS PROGRESS BAR===
        self.stepsPB_Label = QLabel(self)
        self.stepsPB_Label.setText("Steps:")
        self.stepsPB_Label.setGeometry(34, 105, self.stepsPB_Label.fontMetrics().boundingRect(self.stepsPB_Label.text()).width(), 15)
        self.steps_ProgressBar = QProgressBar(self)
        self.steps_ProgressBar.setTextVisible(False)
        self.steps_ProgressBar.setGeometry(self.stepsPB_Label.width() + self.stepsPB_Label.x() + 4, self.stepsPB_Label.y(), 120, 15)

        # ===CALCULATION ESTIMATION BOX===
        self.completionETA_Label = QLabel(self)
        self.completionETA_Label.setText("Completion ETA:")
        self.completionETA_Label.setGeometry(34, 185, self.completionETA_Label.fontMetrics().boundingRect(self.completionETA_Label.text()).width(), 15)
        self.completionETA_Display = QLabel(self)
        self.completionETA_Display.setGeometry(self.completionETA_Label.width() + self.completionETA_Label.x() + 4, self.completionETA_Label.y(), 60, 15)

        # ===EPOCHS PROGRESS BAR===
        self.epoch_PBLabel = QLabel(self)
        self.epoch_PBLabel.setText("Epochs:")
        self.epoch_PBLabel.setGeometry(34, 205, self.epoch_PBLabel.fontMetrics().boundingRect(self.epoch_PBLabel.text()).width(), 15)
        self.epoch_ProgressBar = QProgressBar(self)
        self.epoch_ProgressBar.setTextVisible(False)
        self.epoch_ProgressBar.setGeometry(self.epoch_PBLabel.width() + self.epoch_PBLabel.x() + 4, self.epoch_PBLabel.y(), 120, 15)

        # ===OUTPUT LOG===
        self.outputLog_TextBox = QTextEdit(self)
        self.outputLog_TextBox.setReadOnly(True)
        self.outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLog_TextBox.verticalScrollBar()
        self.outputLog_TextBox.setMinimumWidth(295)
        self.outputLog_TextBox.setGeometry(200, 4, self.width() - (self.outputLog_TextBox.x() + 4), self.height() - (self.outputLog_TextBox.y() + 4))

        # ===TRAIN BUTTON===
        self.train_Button = QPushButton('Train', self)
        #self.train_Button.setEnabled(False)
        self.train_Button.setToolTip('Begin Training')
        self.train_Button.setGeometry(100, 300, 90, 30)
        self.train_Button.clicked.connect(self.train)

        # ===LOAD BUTTON====
        self.load_button = QPushButton('Load', self)
        self.load_button.setToolTip('Load your neural network weights')
        self.load_button.setGeometry(100,350,90,30)
        #self.load_button.clicked.connect(self.Load)

        # ====SAVE BUTTON====
        self.save_button = QPushButton('Save', self)
        self.save_button.setToolTip('Save your current epoch')
        self.save_button.setGeometry(100,400,90,30)
        #self.save_button.clicked.connect()

        # ====RESULTS BUTTON====
        self.results_button = QPushButton('Results', self)
        self.results_button.setToolTip('Show your results')
        self.results_button.setGeometry(100, 450, 90, 30)


        # ===GRAPHS PANE===
        self.graph_canvas = QWidget(self)
        #self.graph_canvas.setStyleSheet("background-color: transparent; border: 0px;")
        self.graph_canvas.setGeometry(365, 4, self.width() *.5, self.height() - 12)
        # ==== Graph Tab Pane ====
        self.graph_tabs = QTabWidget(self.graph_canvas)
        self.graph_tabs.setTabsClosable(True)
        self.graph_tabs.tabCloseRequested.connect(self.removeTab)
        self.graph_tabs.setMovable(True)
        self.graph_tabs.setGeometry(0, 0, self.graph_canvas.width(), self.graph_canvas.height())

    def resizeEvent(self, *args, **kwargs):
                self.train_Button.move(100, self.height() - (self.train_Button.height() + 75))
                self.load_button.move(100, self.height() - (self.load_button.height() + 35))
                self.save_button.move(4, self.height() - (self.save_button.height() + 75))
                self.results_button.move(4, self.height() - (self.results_button.height() + 35))
                self.outputLog_TextBox.setGeometry(self.outputLog_TextBox.x(), self.outputLog_TextBox.y(), (self.width() - self.outputLog_TextBox.x()) * .5 + 4, self.height() - (self.outputLog_TextBox.y() + 19))
                self.graph_canvas.setGeometry(self.outputLog_TextBox.x() + self.outputLog_TextBox.width() + 4, self.graph_canvas.y(), (self.width() - self.outputLog_TextBox.x()) * .5 + 4, self.height() - (self.outputLog_TextBox.y() + 19))
                self.graph_tabs.setGeometry(0, 0, self.graph_canvas.width(), self.graph_canvas.height())
                self.scrollBar.setGeometry(0, self.height() - 15, self.width(), 15)


    def removeTab(self, index):
        widget = self.graph_tabs.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.graph_tabs.removeTab(index)

    def train(self):
        self.train_Button.setDisabled(True)

        self.epochs_Thread = Trainer(self.inputEpochs_SB.text(), self.datasets_ComboBox.currentText())
        self.epochs_Thread.logSignal.connect(self.outputLog_TextBox.append)
        self.epochs_Thread.stepSignal.connect(self.steps_ProgressBar.setValue)
        self.epochs_Thread.epochSignal.connect(self.epoch_ProgressBar.setValue)
        self.epochs_Thread.maxstepsSignal.connect(self.steps_ProgressBar.setMaximum)
        self.epochs_Thread.maxepochsSignal.connect(self.epoch_ProgressBar.setMaximum)
        self.epochs_Thread.epochtimeSignal.connect(self.epochETA_Display.setText)
        self.epochs_Thread.totaltimeSignal.connect(self.completionETA_Display.setText)
        self.epochs_Thread.completeSignal.connect(lambda: self.train_Button.setDisabled(False))
        self.epochs_Thread.start()