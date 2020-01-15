# Abstract: Athena Launchpad GUI: generates UI for Athena texture generator
# Author: Zack Thompson
# last updates April 5th, 2019

# Version 0.85

# TODO Athena Neural network graph Owl Logo.

import sys
from PyQt5.QtWidgets import *
from Data.QtCustomWidgets import *
from PyQt5.QtGui import QIcon, QColor, QPalette
import PyQt5.QtCore as QtCore
import PyQt5
import time
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('Data/Athena_v1.ico'))
        self.setWindowTitle('A.N.N.I. Advanced Neural Network Interface')
        self.setMinimumSize(.5 * app.desktop().screenGeometry().width(), (5 / 9) * app.desktop().screenGeometry().height())

        # Center window
        window = self.frameGeometry()
        window.moveCenter(QDesktopWidget().availableGeometry().center())

        self.initUI()

    def initUI(self):
        # Panel Input
        self.panel_input = QWidget(self)
        self.panel_train = QTrainInputWidget(self.panel_input)
        self.panel_train.hide()

        # Panel Output
        self.panel_canvas = QWidget(self)
        self.panel_canvas.setStyleSheet("background-color: transparent; border: 0px;")

        self.panel_tabs = QTabWidget(self.panel_canvas)
        self.panel_tabs.setTabsClosable(True)
        self.panel_tabs.tabCloseRequested.connect(self.removeTab)
        self.panel_tabs.setMovable(True)

        # Menu Bar
        self.mainMenu = self.menuBar()

        # File Menu Item
        self.fileMenu = self.mainMenu.addMenu('File')
        # New Session Menu Item Button
        self.newSession_DropButton = QAction('New Session', self)
        self.newSession_DropButton.setShortcut('CTRL+N')
        self.fileMenu.addAction(self.newSession_DropButton)
        # Train Menu Item Button
        self.train_dropButton = QAction('Train', self)
        self.train_dropButton.setShortcut('Ctrl+T')
        self.train_dropButton.setStatusTip('Train a model')
        self.train_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs, QTrainOutputWidget, "Model Training"))
        self.train_dropButton.triggered.connect(self.panel_train.show)
        self.fileMenu.addAction(self.train_dropButton)
        # Import Dataset Menu Item Button
        self.customData_dropButton = QAction('Import Dataset', self)
        self.customData_dropButton.setShortcut('Ctrl+C')
        self.customData_dropButton.setStatusTip('Generate based on your own dataset')
        self.customData_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs, QImportWidget, "Import A Dataset"))
        self.fileMenu.addAction(self.customData_dropButton)
        # Exit Menu Item Button
        self.exit_dropButton = QAction('Exit', self)
        self.exit_dropButton.setShortcut('Alt+F4')
        self.exit_dropButton.setStatusTip('Exit Athena')
        self.exit_dropButton.triggered.connect(self.close)
        self.fileMenu.addAction(self.exit_dropButton)


        # View Menu Item
        self.viewMenu = self.mainMenu.addMenu('View')
        self.viewMenu.setEnabled(False)
        # Results Menu Item Button
        self.results_dropButton = QAction('Results', self)
        self.results_dropButton.setShortcut('Shift+V')
        self.results_dropButton.triggered.connect(lambda: self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.addTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QResultsWidget), "Results"))
        self.viewMenu.addAction(self.results_dropButton)
        #Histogram Menu Item Button
        self.histogram_dropButton = QAction('Histogram', self)
        self.histogram_dropButton.setShortcut('Shift+H')
        self.histogram_dropButton.setStatusTip('Generate Histogram')
        self.histogram_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs, QHistogramWidget, "Histogram") if not self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QHistogramWidget) else self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.addTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QHistogramWidget), "Histogram"))
        self.viewMenu.addAction(self.histogram_dropButton)
        # Scatterplot Menu Item Button
        self.scatterplot_dropButton = QAction('Scatterplot', self)
        self.scatterplot_dropButton.setShortcut('Shift+S')
        self.scatterplot_dropButton.setStatusTip('Generate Scatterplot')
        self.scatterplot_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs, QScatterplotWidget, "Scatterplot") if not self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QScatterplotWidget) else self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.addTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QScatterplotWidget), "Scatterplot"))
        self.viewMenu.addAction(self.scatterplot_dropButton)
        # Loss Menu Item Button
        self.lossGraph_dropButton = QAction('Loss', self)
        self.lossGraph_dropButton.setShortcut('Shift+L')
        self.lossGraph_dropButton.setStatusTip('Generate loss graph')
        self.lossGraph_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs, QLinearWidget, "Linear") if not self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QLinearWidget) else self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.addTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QLinearWidget), "Loss over time"))
        self.viewMenu.addAction(self.lossGraph_dropButton)
        # Elapsed Time Menu Item Button
        self.timeGraph_dropButton = QAction('Elapsed Time', self)
        self.timeGraph_dropButton.setShortcut('Shift+T')
        self.timeGraph_dropButton.setStatusTip('Generate loss graph')
        self.timeGraph_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs, QElapsedTimeWidget, "Epochs / Time") if not self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QElapsedTimeWidget) else self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.addTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QElapsedTimeWidget), "Elapsed Time"))
        self.viewMenu.addAction(self.timeGraph_dropButton)
        # EEG Menu Item Button
        self.eegGraph_dropButton = QAction('Electroencephalography Graph (Yes, you can)', self)
        self.eegGraph_dropButton.setShortcut('Shift+E')
        self.eegGraph_dropButton.setStatusTip('Generate EEG graph')
        self.eegGraph_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs, QEEGWidget, "Neural Network EEG") if not self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QEEGWidget) else self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.addTab(self.panel_tabs.findChild(QTrainOutputWidget).graph_tabs.findChild(QEEGWidget), "EEG"))
        self.viewMenu.addAction(self.eegGraph_dropButton)


        # Help Menu Item
        self.helpMenu = self.mainMenu.addMenu('Help')
        # Help Center Menu Item Button
        self.helpCenter_dropButton = QAction(QIcon('Data/Help.png'), 'Help Center', self)
        self.helpCenter_dropButton.setShortcut('Ctrl+H')
        self.helpCenter_dropButton.setStatusTip('Generate loss graph')
        self.helpCenter_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs,QHelpWidget, "Help Center"))
        #self.helpCenter_dropButton.triggered.connect(Athena_Help_Center)
        self.helpMenu.addAction(self.helpCenter_dropButton)


        # About Athena Menu Item Button
        self.aboutAthena_dropButton = QAction('About Athena', self)
        self.aboutAthena_dropButton.setShortcut('Ctrl+A')
        self.aboutAthena_dropButton.setStatusTip('Learn about Athena')
        self.helpMenu.addAction(self.aboutAthena_dropButton)
        self.aboutAthena_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs,QAboutWidget,"About Athena"))
        # About Developers Menu Item Button
        self.aboutDevs_dropButton = QAction('Meet the Developers', self)
        self.aboutDevs_dropButton.setShortcut('Ctrl+M')
        self.aboutDevs_dropButton.setStatusTip('Learn about the developers! :)')
        self.aboutDevs_dropButton.triggered.connect(lambda: self.createTab(self.panel_tabs, QDevWidget, "About Developers"))
        self.helpMenu.addAction(self.aboutDevs_dropButton)

    def createTab(self, root, widget, name):
        if not root.findChild(widget):
            tab = widget(root)
            tab.setStyleSheet(open('Data/CSS.cfg').read())
            root.addTab(tab, name)

        if self.panel_tabs.findChild(QTrainOutputWidget):
            self.viewMenu.setEnabled(True)

    def removeTab(self, index):
        widget = self.panel_tabs.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.panel_tabs.removeTab(index)

        if type(widget) == QTrainOutputWidget:
            self.viewMenu.setEnabled(False)
            self.panel_train.hide()

    def importDatasets(self):
        if self.panel_tabs.findChildren(QImportWidget) == []:
            self.importTab = QImportWidget(self.panel_tabs)
            self.panel_tabs.addTab(self.importTab, "Import A Dataset")

    def resizeEvent(self, *args, **kwargs):
        self.panel_input.setGeometry(4, 21, self.width() * .2, self.height() - 24)
        self.panel_train.setGeometry(0, 0, self.panel_input.width(), self.panel_input.height())
        self.panel_canvas.setGeometry(self.panel_input.width() + 8, 21, self.width() - (self.panel_input.width() + 12), self.panel_input.height())
        self.panel_tabs.setGeometry(0, 0, self.panel_canvas.width(), self.panel_canvas.height())

# def Athena_Help_Center():
#     url = 'https://overclockedthompson.wixsite.com/athena/basic-interaction'
#     browser = QWebEngineView()
#     browser.load(QUrl(url))
#     browser.show()

if __name__ == '__main__':
    # Multi-Resolution Support
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
