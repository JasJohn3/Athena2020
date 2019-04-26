from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from Data.Trainer.Epoch import Trainer
from Data.QtCustomWidgets import *


class QTrainInputWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.initUI()

    def initUI(self):
        # Header Label
        self.ref_Label = QLabel(self)
        self.ref_Label.setText("GAN Training")
        self.ref_Label.setFont(QFont("Times", 12, QFont.Bold))
        self.ref_Label.setStyleSheet("Color: #55abec")

        # Dataset Selection
        self.datasets_ComboBox = QComboBox(self)
        self.datasets_ComboBox.setToolTip("Your current uploaded datasets.")
        for name in ["Datasets", "cifar10", "cifar100", "mnist", "stl10", "lsun", "imagenet"]: self.datasets_ComboBox.addItem(name)
        self.datasets_ComboBox.currentTextChanged.connect(lambda: self.train_Button.setEnabled(True) if self.datasets_ComboBox.currentText() != "Datasets" else self.train_Button.setEnabled(False))

        # Epochs Selection
        self.epochsSB_Label = QLabel(self)
        self.epochsSB_Label.setText("Epochs:")
        # Up/Down Number
        self.inputEpochs_SB = QSpinBox(self)
        self.inputEpochs_SB.setToolTip("How many epochs the GAN will execute.")
        self.inputEpochs_SB.setMinimum(1)

        # Session Selection
        self.sessionTB_Label = QLabel(self)
        self.sessionTB_Label.setText("Session Name")
        # Input Text
        self.sessionName_TextBox = QLineEdit(self)
        self.sessionName_TextBox.setToolTip("Name your session.")
        self.sessionName_TextBox.setStyleSheet("Color: #F0F0F0;")

        # Save Image Check
        self.image_Check = QPushButton(self)
        self.image_Check.setText("Save Images")
        self.image_Check.setToolTip("Save images at end of each epoch.")
        self.image_Check.setCheckable(True)
        self.image_Check.setStyleSheet("QPushButton{border-radius: 5px;} QPushButton::checked{background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4670B2,  stop: 1.0 #648ED0);}")

        # Save Histogram Check
        self.histogram_Check = QPushButton(self)
        self.histogram_Check.setText("Save Histogram")
        self.histogram_Check.setToolTip("Save histogram at end of full execution.")
        self.histogram_Check.setCheckable(True)
        self.histogram_Check.setStyleSheet("QPushButton{border-radius: 5px;} QPushButton::checked{background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4670B2,  stop: 1.0 #648ED0);}")

        # Training Button
        self.train_Button = QPushButton(self)
        self.train_Button.setEnabled(False)
        self.train_Button.setText("Train")
        self.train_Button.clicked.connect(self.train)
        self.train_Button.setToolTip("You have not selected a dataset yet!") if not self.train_Button.isEnabled() else self.train_Button.setToolTip("Begin Training")

        # Progress indicator
        self.panel_progress = QWidget(self)
        self.panel_progress.setStyleSheet("border: 2px")
        # Epoch Progress
        self.epochETA_Label = QLabel(self.panel_progress)
        self.epochETA_Label.setText("Epoch ETA:")
        self.epochETA_Display = QLabel(self.panel_progress)
        self.steps_ProgressBar = QProgressBar(self.panel_progress)
        self.steps_ProgressBar.setTextVisible(False)
        # Training Progress
        self.completionETA_Label = QLabel(self.panel_progress)
        self.completionETA_Label.setText("Completion ETA:")
        self.completionETA_Display = QLabel(self.panel_progress)
        self.epoch_ProgressBar = QProgressBar(self.panel_progress)
        self.epoch_ProgressBar.setTextVisible(False)

    def train(self):
        self.train_Button.setDisabled(True)
        # Grab parent tab widget to disable tab button
        self.parent().parent().panel_tabs.tabBar().tabButton(self.parent().parent().panel_tabs.indexOf(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget)), 1).setDisabled(True)
        # Use Parent function to create tab and hide all but results
        for tab in [(QResultsWidget, "Results"), (QHistogramWidget, "Histogram"), (QScatterplotWidget, "Scatterplot"), (QLinearWidget, "Loss over time"), (QElapsedTimeWidget, "Elapsed Time"), (QEEGWidget, "EEG")]:
            self.parent().parent().createTab(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs, tab[0], tab[1])
            if tab[0] != QResultsWidget: self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs.removeTab(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs.indexOf(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(tab[0])))

        # Create thread for training GAN
        self.epochs_Thread = Trainer(self.inputEpochs_SB.text(), self.datasets_ComboBox.currentText(), self.sessionName_TextBox.text(), self.image_Check.isChecked())
        # Update text output from emitted data
        self.epochs_Thread.logSignal.connect(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).outputLog_TextBox.append)
        # Set Value bar's maximum from emitted total epoch's and step size
        self.epochs_Thread.maxstepsSignal.connect(self.steps_ProgressBar.setMaximum)
        self.epochs_Thread.maxepochsSignal.connect(self.epoch_ProgressBar.setMaximum)
        # Update the progress of the Value bar's from emitted intervals
        self.epochs_Thread.stepSignal.connect(self.steps_ProgressBar.setValue)
        self.epochs_Thread.epochSignal.connect(self.epoch_ProgressBar.setValue)
        # Update ETA labels with emitted calculated time
        self.epochs_Thread.epochtimeSignal.connect(self.epochETA_Display.setText)
        self.epochs_Thread.totaltimeSignal.connect(self.completionETA_Display.setText)
        # Re-enable Train button and Train tab exit when thread ends
        self.epochs_Thread.completeSignal.connect(lambda: self.train_Button.setDisabled(False))
        self.epochs_Thread.completeSignal.connect(lambda: self.parent().parent().panel_tabs.tabBar().tabButton(self.parent().parent().panel_tabs.currentIndex(), 1).setDisabled(False))
        # Set displayed images from emitted training and testing images
        self.epochs_Thread.trainImageSignal.connect(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QResultsWidget).addImage)
        self.epochs_Thread.testImageSignal.connect(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QResultsWidget).addImage)
        self.epochs_Thread.LossSignal.connect(self.parent().parent().panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QHistogramWidget).updateGraph)
        # self.epochs_Thread.discriminatorLossSignal.connect(self.graph_tabs.findChild(QHistogramWidget).set_DVals)
        # Start the GAN's training thread
        self.epochs_Thread.start()

    def resizeEvent(self, QResizeEvent):
        # Header
        self.ref_Label.setGeometry(4, 4, self.ref_Label.fontMetrics().boundingRect(self.ref_Label.text()).width(), 20)

        # Dataset
        self.datasets_ComboBox.setGeometry(4, self.ref_Label.height() + self.ref_Label.y() + 16, self.width() - 8, 15)

        # Epochs
        self.epochsSB_Label.setGeometry(4, self.datasets_ComboBox.y() + self.datasets_ComboBox.height() + 8, self.epochsSB_Label.fontMetrics().boundingRect(self.epochsSB_Label.text()).width(), 15)
        self.inputEpochs_SB.setGeometry(4, self.epochsSB_Label.y() + self.epochsSB_Label.height() + 4, self.width() - 8, 15)

        # Session
        self.sessionTB_Label.setGeometry(4, self.inputEpochs_SB.y() + self.inputEpochs_SB.height() + 8, self.width() - 8, 15)
        self.sessionTB_Label.setAlignment(Qt.AlignCenter)
        self.sessionName_TextBox.setGeometry(4, self.sessionTB_Label.y() + self.sessionTB_Label.height(), self.width() - 8, 15)
        self.sessionName_TextBox.setAlignment(Qt.AlignCenter)

        # Image
        self.image_Check.setGeometry(4, self.sessionName_TextBox.y() + self.sessionName_TextBox.height() + 4, self.width() - 8, 15)

        # Histogram
        self.histogram_Check.setGeometry(4, self.image_Check.y() + self.image_Check.height() + 4, self.width() - 8, 15)

        # Button
        self.train_Button.setGeometry(4, self.histogram_Check.y() + self.histogram_Check.height() + 4, self.width() - 8, 15)

        # Progress Panel
        self.panel_progress.setGeometry(0, self.height() - 104, self.width(), 104)
        # Epoch Progress size update
        self.epochETA_Label.setGeometry(4, 4, self.epochETA_Label.fontMetrics().boundingRect(self.epochETA_Label.text()).width(), 15)
        self.epochETA_Display.setGeometry(self.epochETA_Label.width() + self.epochETA_Label.x() + 4, self.epochETA_Label.y(), self.panel_progress.width() - self.epochETA_Label.width() - 12, 15)
        self.steps_ProgressBar.setGeometry(4, self.epochETA_Label.y() + self.epochETA_Label.height() + 4, self.panel_progress.width() - 8, 15)
        # Training progress size update
        self.completionETA_Label.setGeometry(4, self.steps_ProgressBar.y() + self.steps_ProgressBar.height() + 8, self.completionETA_Label.fontMetrics().boundingRect(self.completionETA_Label.text()).width(), 15)
        self.completionETA_Display.setGeometry(self.completionETA_Label.width() + self.completionETA_Label.x() + 4, self.completionETA_Label.y(), self.panel_progress.width() - self.completionETA_Label.width() - 12, 15)
        self.epoch_ProgressBar.setGeometry(4, self.completionETA_Display.y() + self.completionETA_Display.height() + 4, self.panel_progress.width() - 8, 15)

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    # Todo Fix Custom widget style sheets (borders & backgrounds are non-functonal atm)
    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_Widget, styleSheet, paint, self)