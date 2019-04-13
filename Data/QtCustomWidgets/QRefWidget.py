from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class QRefWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        ###
        #Labels
        ###
            # Control panel label
        self.ref_Label = QLabel(self)
        self.ref_Label.setText("Your Training Settings")
        self.ref_Label.setFont(QFont("Times", 12, QFont.Bold))
        self.ref_Label.setStyleSheet("Color: #55abec")
        self.ref_Label.setGeometry(0, 5, self.ref_Label.fontMetrics().boundingRect(self.ref_Label.text()).width() + 4, 20)
            # dataset combobox label
        self.dataCB_Label = QLabel(self)
        self.dataCB_Label.setText("Dataset")
        self.dataCB_Label.setGeometry(4, 50, self.dataCB_Label.fontMetrics().boundingRect(self.dataCB_Label.text()).width()+4, 15)
            # epochs spin box label
        self.epochsSB_Label = QLabel(self)
        self.epochsSB_Label.setText("Epochs")
        self.epochsSB_Label.setGeometry(4,100, self.epochsSB_Label.fontMetrics().boundingRect(self.epochsSB_Label.text()).width()+4, 15)
            # Session name textbox label
        self.sessionTB_Label = QLabel(self)
        self.sessionTB_Label.setText("Session Name")
        self.sessionTB_Label.setGeometry(4, 175, self.sessionTB_Label.fontMetrics().boundingRect(self.sessionTB_Label.text()).width()+4, 15)
            #Save image checkbox label
        self.saveImageCB_Label = QLabel(self)
        self.saveImageCB_Label.setText("Save images")
        self.saveImageCB_Label.setGeometry(4, 225, self.saveImageCB_Label.fontMetrics().boundingRect(self.saveImageCB_Label.text()).width() + 4, 15)
            # Save histogram checkbox label
        self.histogramCB_Label = QLabel(self)
        self.histogramCB_Label.setText("Save Histogram")
        self.histogramCB_Label.setGeometry(4, 250, self.histogramCB_Label.fontMetrics().boundingRect(self.histogramCB_Label.text()).width()+4, 15)
            # Progess area label
        self.progressArea_Label = QLabel(self)
        self.progressArea_Label.setText("Progress")
        self.progressArea_Label.setFont(QFont("Times", 12, QFont.Bold))
        self.progressArea_Label.setStyleSheet("Color: #55abec")
        self.progressArea_Label.setGeometry(0, 350, self.progressArea_Label.fontMetrics().boundingRect(self.progressArea_Label.text()).width() + 4,
                                   20)
        # dataset combobox label
        ###
        #Dataset combo box
        ###
        self.datasets_ComboBox = QComboBox(self)
        self.datasets_ComboBox.setToolTip("Your current uploaded datasets.")
        self.datasets_ComboBox.addItem("<Your Datasets>")
        self.datasets_ComboBox.addItem("cifar10")
        self.datasets_ComboBox.addItem("cifar100")
        self.datasets_ComboBox.addItem("mnist")
        self.datasets_ComboBox.addItem("stl10")
        self.datasets_ComboBox.addItem("lsun")
        self.datasets_ComboBox.addItem("imagenet")
        self.datasets_ComboBox.setGeometry(self.dataCB_Label.width() + self.dataCB_Label.x() + 4,
                                           self.dataCB_Label.y(), 100, 25)
        ###
        #Epoch scroll box
        ###
        self.inputEpochs_SB = QSpinBox(self)
        self.inputEpochs_SB.setToolTip("How many epochs the GAN will execute.")
        self.inputEpochs_SB.setMinimum(1)
        self.inputEpochs_SB.setGeometry(self.epochsSB_Label.width() + self.epochsSB_Label.x() + 4,
                                        self.epochsSB_Label.y(), 100, 25)
        ###
        #Session name textbox
        ###
        self.sessionName_TextBox = QLineEdit(self)
        self.sessionName_TextBox.setToolTip("Name your session.")
        self.sessionName_TextBox.setGeometry(self.sessionTB_Label.width() + self.sessionTB_Label.x()+4,
                                             self.sessionTB_Label.y(), 115, 25)

        ###
        #Save images check box
        ###
        self.saveImages_CheckBox = QCheckBox(self)
        self.saveImages_CheckBox.setToolTip("Save images at end of each epoch.")
        #self.saveImages_CheckBox.setLayoutDirection(Qt.LeftToRight)
        self.saveImages_CheckBox.setGeometry(self.saveImageCB_Label.width() + self.saveImageCB_Label.x()+4,
                                             self.saveImageCB_Label.y(), 15, 15)


        ###
        #Save Histogram
        ###
        self.saveHistogram_CheckBox = QCheckBox(self)
        self.saveHistogram_CheckBox.setToolTip("Save histogram at end of full execution.")
        self.saveHistogram_CheckBox.setGeometry(self.histogramCB_Label.width() + self.histogramCB_Label.x() + 4,
                                                self.histogramCB_Label.y(), 15, 15)


        ###
        #Epoch Progress bar
        ###
        #self.epoch_ProgressBar = QProgressBar(self)
        #self.epoch_ProgressBar.setTextVisible(False)
        #self.epoch_ProgressBar.setGeometry(self.stepsPB_Label.width() + self.stepsPB_Label.x() + 4,
                                          # self.stepsPB_Label.y(), 120, 15)

        #self.datasets_ComboBox.currentTextChanged.connect(lambda: self.train_Button.setEnabled(
        #    True) if self.datasets_ComboBox.currentText() != "<Your Datasets>" else self.train_Button.setEnabled(False))