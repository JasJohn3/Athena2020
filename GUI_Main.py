# Abstract: Athena Launchpad GUI: generates UI for Athena texture generator
# Author: Zack Thompson
# last updates February 1, 2019

# Version 0.01

# TODO Athena Neural network graph Owl Logo.

import sys
from PyQt5.QtWidgets import *
from Data.QtCustomWidgets import *
from PyQt5.QtGui import QIcon, QColor, QPalette
import PyQt5.QtCore as QtCore
import PyQt5


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('Data/Athena_v1.ico'))
        self.setWindowTitle('Athena')
        self.resize(640, 400)

        # Center window
        window = self.frameGeometry()
        window.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(window.topLeft())

        self.initUI()

    def initUI(self):
        ###
        # Panel options
        ###
        self.panel_options = QWidget(self)
        self.panel_options.setGeometry(4, 20, self.width() * .2, self.height() - 24)

        ###
        # Panel Canvas
        ###
        self.panel_canvas = QWidget(self)
        self.panel_canvas.setStyleSheet("background-color: transparent; border: 0px;")
        self.panel_canvas.setGeometry(self.panel_options.width() + 8, 20, self.width() - (self.panel_options.width() + 12), self.panel_options.height())
        #Tab pane
        self.panel_tabs = QTabWidget(self.panel_canvas)
        self.panel_tabs.setTabsClosable(True)
        self.panel_tabs.tabCloseRequested.connect(self.removeTab)
        self.panel_tabs.setMovable(True)
        self.panel_tabs.setGeometry(0, 0, self.panel_canvas.width(), self.panel_canvas.height())

        ###
        # Menu Bar
        ###
        # Create menu bar
        self.mainMenu = self.menuBar()
        # Create Menu Items
        self.trainMenu = self.mainMenu.addMenu('File')
        self.graphsMenu = self.mainMenu.addMenu('Graphs')
        self.helpMenu = self.mainMenu.addMenu('Help')

        ###Menu Bar: File###
        ###Train###
        self.train_dropButton = QAction('Train', self)
        self.train_dropButton.setShortcut('Ctrl+T')
        self.train_dropButton.setStatusTip('Train a model')
        self.train_dropButton.triggered.connect(self.train)
        self.trainMenu.addAction(self.train_dropButton)  # add test button to dropdown menu
        ###Import Dataset###
        self.customData_dropButton = QAction('Import Dataset', self)
        self.customData_dropButton.setShortcut('Ctrl+C')
        self.customData_dropButton.setStatusTip('Generate based on your own dataset')
        # custom_dropButton.triggered.openCustomizeDatasetWindow() <-- TODO create temporary window and enable dataset upload.
        self.trainMenu.addAction(self.customData_dropButton)  # add button to dropdown menu
        ###Exit###
        self.exit_dropButton = QAction('Exit', self)
        self.exit_dropButton.setShortcut('Alt+F4')
        self.exit_dropButton.setStatusTip('Exit Athena')
        self.exit_dropButton.triggered.connect(self.close)
        self.trainMenu.addAction(self.exit_dropButton)  # add button to dropdown menu

        ###Menu Bar: Graphs###
        ###Histogram###
        self.histogram_dropButton = QAction('Histogram', self)
        self.histogram_dropButton.setShortcut('Shift+H')
        self.histogram_dropButton.setStatusTip('Generate Histogram')
        # histogram_dropButton.triggered.openHistogramWindow() <-- TODO create window, enable histogram generation
        self.graphsMenu.addAction(self.histogram_dropButton)
        ###Scatterplot###
        self.scatterplot_dropButton = QAction('Scatterplot', self)
        self.scatterplot_dropButton.setShortcut('Shift+S')
        self.scatterplot_dropButton.setStatusTip('Generate Scatterplot')
        # scatterplot_dropButton.triggered.openScattplotWindow() <-- TODO create window, enable scatterplot generation
        self.graphsMenu.addAction(self.scatterplot_dropButton)
        ###Loss###
        self.lossGraph_dropButton = QAction('Loss', self)
        self.lossGraph_dropButton.setShortcut('Shift+L')
        self.lossGraph_dropButton.setStatusTip('Generate loss graph')
        # lossGraph_dropButton.triggered.openLossWindow() <-- TODO create window, enable loss generation.
        self.graphsMenu.addAction(self.lossGraph_dropButton)
        ###Elapsed Time###
        self.timeGraph_dropButton = QAction('Elapsed Time', self)
        self.timeGraph_dropButton.setShortcut('Shift+T')
        self.timeGraph_dropButton.setStatusTip('Generate loss graph')
        # timeGraph_dropButton.triggered.openLossWindow() <-- TODO create window, enable time elapsed graph.
        self.graphsMenu.addAction(self.timeGraph_dropButton)
        ###EEG###
        self.eegGraph_dropButton = QAction('Electroencephalography Graph (Yes, you can)', self)
        self.eegGraph_dropButton.setShortcut('Shift+E')
        self.eegGraph_dropButton.setStatusTip('Generate EEG graph')
        # eegGraph_dropButton.triggered.openEEGWindow() <-- TODO create window, enable EEG graph
        self.graphsMenu.addAction(self.eegGraph_dropButton)

        ###Menu Bar: Help###
        ###Help Center###
        self.helpCenter_dropButton = QAction(QIcon('Data/Help.png'), 'Help Center', self)
        self.helpCenter_dropButton.setShortcut('Ctrl+H')
        self.helpCenter_dropButton.setStatusTip('Generate loss graph')
        #self.helpCenter_dropButton.triggered.connect(Dialogues.helpcenter)
        self.helpMenu.addAction(self.helpCenter_dropButton)
        ###About Athena###
        self.aboutAthena_dropButton = QAction('About Athena', self)
        self.aboutAthena_dropButton.setShortcut('Ctrl+A')
        self.aboutAthena_dropButton.setStatusTip('Learn about Athena')
        # aboutAthena_dropButton.triggered.openHelpCenterWindow() <-- TODO create window, create about center.
        self.helpMenu.addAction(self.aboutAthena_dropButton)
        ###About Developers###
        self.aboutDevs_dropButton = QAction('Meet the Developers', self)
        self.aboutDevs_dropButton.setShortcut('Ctrl+M')
        self.aboutDevs_dropButton.setStatusTip('Learn about the developers! :)')
        self.aboutDevs_dropButton.triggered.connect(self.aboutDev)
        # aboutDevs_dropButton.triggered.openDevsWindow() <-- TODO create window, create aboutDevs Center, enable portfolio linking.
        self.helpMenu.addAction(self.aboutDevs_dropButton)

    ###
    #Tab Functions
    ###
    def train(self):
        self.trainTab = QTrainWidget(self.panel_tabs)
        self.trainTab.setStyleSheet(open('Data/CSS.cfg').read())
        self.panel_tabs.addTab(self.trainTab, "Model Trainer")

    def aboutDev(self):
        self.devTab = QDevWidget(self.panel_tabs)
        self.devTab.setStyleSheet(open('Data/CSS.cfg').read())
        self.panel_tabs.addTab(self.devTab, "Model Trainer")

    #Remove a tab
    def removeTab(self, index):
        widget = self.panel_tabs.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.panel_tabs.removeTab(index)

    ###
    #Window Scaling
    ###
    def resizeEvent(self, *args, **kwargs):
        self.panel_options.setGeometry(4, 20, self.width() * .2, self.height() - 24)
        self.panel_canvas.setGeometry(self.panel_options.width() + 8, 20, self.width() - (self.panel_options.width() + 12), self.panel_options.height())
        self.panel_tabs.setGeometry(0, 0, self.panel_canvas.width(), self.panel_canvas.height())


if __name__ == '__main__':
    #Multi-Resolution Support
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    #Set the style of the entire GUI
    app.setStyleSheet(open('Data/CSS.cfg').read())
    Athena = GUI()
    Athena.show()
    sys.exit(app.exec_())