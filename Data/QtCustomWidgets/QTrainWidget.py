from PyQt5.QtWidgets import *
from Data.Trainer.Epoch import Trainer
from Data.QtCustomWidgets import *


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

        # ===DATASETS COMBOBOX===
        self.datasets_Label = QLabel(self)
        self.datasets_Label.setText("Datasets:")
        self.datasets_Label.setGeometry(4, 4, self.datasets_Label.fontMetrics().boundingRect(self.datasets_Label.text()).width(), 15)
        self.datasets_ComboBox = QComboBox(self)
        # self.datasets_ComboBox.changeEvent(lambda: self.train_Button.setEnabled(self.datasets_ComboBox.currentIndex() != 0)) <-- Todo lookup

        print(self.datasets_ComboBox.activated)
        print(self.datasets_ComboBox.currentIndex())
        self.datasets_ComboBox.setToolTip("Your current uploaded datasets.")
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.addItem("cifar10")
        self.datasets_ComboBox.addItem("cifar100")
        self.datasets_ComboBox.addItem("mnist")
        self.datasets_ComboBox.addItem("stl10")
        self.datasets_ComboBox.addItem("lsun")
        self.datasets_ComboBox.addItem("imagenet")
        self.datasets_ComboBox.setGeometry(self.datasets_Label.width() + self.datasets_Label.x() + 4, self.datasets_Label.y(), 110, 15)

        self.datasets_ComboBox.currentTextChanged.connect(lambda: self.train_Button.setEnabled(True) if self.datasets_ComboBox.currentText() != "<Your Datasets>" else self.train_Button.setEnabled(False))

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
        self.train_Button.setEnabled(False)
        self.train_Button.setToolTip('Begin Training')
        self.train_Button.setGeometry(100, 300, 90, 30)
        self.train_Button.clicked.connect(self.train)

        # ==== Graph Tab Pane ====
        self.graph_canvas = QWidget(self)
        self.graph_canvas.setStyleSheet("background-color: transparent; border: 0px;")

        self.graph_tabs = QTabWidget(self.graph_canvas)
        self.graph_tabs.setTabsClosable(True)
        self.graph_tabs.tabCloseRequested.connect(self.removeTab)
        self.graph_tabs.setMovable(True)

        # ===Scroll Bar===
        self.scrollbar = QScrollBar(self)
        self.scrollbar.setOrientation(1)

    def activateTrainButton(self):
        self.train_Button.setEnabled(self.datasets_ComboBox.currentIndex() != 0)

    def resizeEvent(self, *args, **kwargs):
        self.train_Button.move(57, self.height() - (self.train_Button.height() + 75))
        self.outputLog_TextBox.setGeometry(self.outputLog_TextBox.x(), self.outputLog_TextBox.y(), (self.width() - self.outputLog_TextBox.x()) * .5 + 4, self.height() - (self.outputLog_TextBox.y() + 19))
        self.graph_canvas.setGeometry(self.outputLog_TextBox.x() + self.outputLog_TextBox.width() + 4, self.outputLog_TextBox.y(), (self.width() - self.outputLog_TextBox.x()) * .5 - 12, self.height() - (self.outputLog_TextBox.y() + 19))
        self.graph_tabs.setGeometry(0, 0, self.graph_canvas.width(), self.graph_canvas.height())
        self.scrollbar.setGeometry(0, self.height() - 15, self.width(), 15)

    def createTab(self, root, widget, name):
        if not root.findChild(widget):
            tab = widget(root)
            tab.setStyleSheet(open('Data/CSS.cfg').read())
            root.addTab(tab, name)

    def removeTab(self, index):
        self.graph_tabs.removeTab(index)

    def train(self):
        self.train_Button.setDisabled(True)
        self.createTab(self.graph_tabs, QResultsWidget, "Results")

        self.epochs_Thread = Trainer(self.inputEpochs_SB.text(), self.datasets_ComboBox.currentText())
        self.epochs_Thread.logSignal.connect(self.outputLog_TextBox.append)
        self.epochs_Thread.stepSignal.connect(self.steps_ProgressBar.setValue)
        self.epochs_Thread.epochSignal.connect(self.epoch_ProgressBar.setValue)
        self.epochs_Thread.maxstepsSignal.connect(self.steps_ProgressBar.setMaximum)
        self.epochs_Thread.maxepochsSignal.connect(self.epoch_ProgressBar.setMaximum)
        self.epochs_Thread.epochtimeSignal.connect(self.epochETA_Display.setText)
        self.epochs_Thread.totaltimeSignal.connect(self.completionETA_Display.setText)
        self.epochs_Thread.completeSignal.connect(lambda: self.train_Button.setDisabled(False))
        self.epochs_Thread.trainImageSignal.connect(self.graph_tabs.findChild(QResultsWidget).addImage)
        self.epochs_Thread.testImageSignal.connect(self.graph_tabs.findChild(QResultsWidget).addImage)
        self.epochs_Thread.start()