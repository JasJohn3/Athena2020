from PyQt5.QtWidgets import *
from Data.Trainer.Epoch import Trainer
from Data.QtCustomWidgets import *
from Data.QtCustomWidgets import QLinearWidget
#from PyQt5.QtGui import QPainter <-- Todo Fix paint event

class QTrainOutputWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        # Output log
        self.outputLog_TextBox = QTextEdit(self)
        self.outputLog_TextBox.setReadOnly(True)
        self.outputLog_TextBox.setLineWrapMode(QTextEdit.NoWrap)
        self.outputLog_TextBox.verticalScrollBar()

        # Graph Tab Pane
        self.graph_canvas = QWidget(self)
        self.graph_canvas.setStyleSheet("background-color: transparent; border: 0px;")
        # Tab Widget
        self.graph_tabs = QTabWidget(self.graph_canvas)
        self.graph_tabs.setTabsClosable(True)
        self.graph_tabs.tabCloseRequested.connect(self.removeTab)
        self.graph_tabs.setMovable(True)

    def createTab(self, root, widget, name):
        if not root.findChild(widget):
            tab = widget(root)
            tab.setStyleSheet(open('Data/CSS.cfg').read())
            root.addTab(tab, name)

    def activateTrainButton(self):
        self.train_Button.setEnabled(self.datasets_ComboBox.currentIndex() != 0)

    def resizeEvent(self, *args, **kwargs):
        self.outputLog_TextBox.setGeometry(4, 4, self.width() * .5 - 6, self.height() - (self.outputLog_TextBox.y() + 4))
        self.graph_canvas.setGeometry(self.outputLog_TextBox.x() + self.outputLog_TextBox.width() + 4, 4, self.width() * .5 - 6, self.height() - (self.outputLog_TextBox.y() + 4))
        self.graph_tabs.setGeometry(0, 0, self.graph_canvas.width(), self.graph_canvas.height())

    def removeTab(self, index):
        self.graph_tabs.removeTab(index)

    def train(self):
        self.train_Button.setDisabled(True)
        self.createTab(self.graph_tabs, QResultsWidget, "Results")
        self.createTab(self.graph_tabs, QHistogramWidget, "Histogram")
        #self.createTab(self.graph_tabs, QScatterplotWidget, "Scatterplot")
        self.createTab(self.graph_tabs, QEEGWidget, "EEG")
        self.createTab(self.graph_tabs, QLinearWidget, "Loss over time")

        # Grab parent tab widget to disable tab button
        self.parent().parent().tabBar().tabButton(self.parent().parent().currentIndex(), 1).setDisabled(True)
        # Use Parent function to create tab
        self.parent().parent().parent().parent().createTab(self.graph_tabs, QResultsWidget, "Results")
        self.parent().parent().parent().parent().createTab(self.graph_tabs, QHistogramWidget, "Histogram")
        self.parent().parent().parent().parent().createTab(self.graph_tabs, QScatterplotWidget, "Scatterplot")
        self.parent().parent().parent().parent().createTab(self.graph_tabs, QLinearWidget, "Loss over time")
        self.parent().parent().parent().parent().createTab(self.graph_tabs, QElapsedTimeWidget, "Elapsed Time")
        self.parent().parent().parent().parent().createTab(self.graph_tabs, QEEGWidget, "EEG")
        #Remove tab from graph tabs that are these widgets
        self.graph_tabs.removeTab(self.graph_tabs.indexOf(self.graph_tabs.findChild(QHistogramWidget)))
        self.graph_tabs.removeTab(self.graph_tabs.indexOf(self.graph_tabs.findChild(QScatterplotWidget)))
        self.graph_tabs.removeTab(self.graph_tabs.indexOf(self.graph_tabs.findChild(QLinearWidget)))
        self.graph_tabs.removeTab(self.graph_tabs.indexOf(self.graph_tabs.findChild(QElapsedTimeWidget)))
        self.graph_tabs.removeTab(self.graph_tabs.indexOf(self.graph_tabs.findChild(QEEGWidget)))

        # Create thread for training GAN
        self.epochs_Thread = Trainer(self.inputEpochs_SB.text(), self.datasets_ComboBox.currentText(), 'Test')
        # Update text output from emitted data
        self.epochs_Thread.logSignal.connect(self.outputLog_TextBox.append)
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
        self.epochs_Thread.completeSignal.connect(lambda: self.parent().parent().tabBar().tabButton(self.parent().parent().currentIndex(), 1).setDisabled(False))
        # Set displayed images from emitted training and testing images
        self.epochs_Thread.trainImageSignal.connect(self.graph_tabs.findChild(QResultsWidget).addImage)
        self.epochs_Thread.testImageSignal.connect(self.graph_tabs.findChild(QResultsWidget).addImage)
        #self.epochs_Thread.LossSignal.connect(self.graph_tabs.findChild(QHistogramWidget).updateGraph)
        self.epochs_Thread.LossSignal.connect(self.graph_tabs.findChild(QLinearWidget).loss_update_Graph)
        #self.epochs_Thread.discriminatorLossSignal.connect(self.graph_tabs.findChild(QHistogramWidget).set_DVals)
        # Start the GAN's training thread
        self.epochs_Thread.start()

    # Force change geometry when called
    # def setGeometry(self, *__args):
    #     super().setGeometry(*__args)
    #
    # def paintEvent(self, event):
    #     super(type(self), self).paintEvent(event)
    #     styleSheet = QStyleOption()
    #     styleSheet.initFrom(self)
    #     paint = QPainter(self)
    #     styling = self.style()
    #     styling.drawPrimitive(QStyle.PE_Widget, styleSheet, paint, self)