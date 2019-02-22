# Abstract: Athena Launchpad GUI: generates UI for Athena texture generator
# Author: Zack Thompson
# last updates February 1, 2019

# Version 0.01

# TODO Athena Neural network graph Owl Logo.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor, QPalette
import PyQt5.QtCore as QtCore
import Dialogues as DialoguesRail
import PyQt5


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class AthenaLaunchpad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('Athena_v1.ico'))
        self.setWindowTitle('Athena')
        self.resize(640, 400)

        # self.initUI()
        # def initUI() <--DANGER THIS WILL BREAK THE ENTIRE GUI

        self.TrainWindow = DialoguesRail.TrainingDialogue()
        self.AboutDevsWindow = DialoguesRail.AboutDevs()
        #TODO on startup throw gui at 0,0 on screen.
        #TODO add the panel behind the spinboxes.

        '''
        Menu Bar
        '''
        #Create menu bar
        mainMenu = self.menuBar()
        #Create Menu Items
        trainMenu = mainMenu.addMenu("Train")
        graphsMenu = mainMenu.addMenu('Graphs')
        helpMenu = mainMenu.addMenu('Help')

        '''Menu Bar: Train'''
        '''Train'''
        train_dropButton = QAction('Train', self)
        train_dropButton.setShortcut('Ctrl+T')
        train_dropButton.setStatusTip('Train a model')
        train_dropButton.triggered.connect(self.TrainWindow.show)
        trainMenu.addAction(train_dropButton)  # add test button to dropdown menu
        '''Import Dataset'''
        customData_dropButton = QAction('Import Dataset', self)
        customData_dropButton.setShortcut('Ctrl+C')
        customData_dropButton.setStatusTip('Generate based on your own dataset')
        # custom_dropButton.triggered.openCustomizeDatasetWindow() <-- TODO create temporary window and enable dataset upload.
        trainMenu.addAction(customData_dropButton)  # add button to dropdown menu
        '''Exit'''
        exit_dropButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_dropButton.setShortcut('Ctrl+Q')
        exit_dropButton.setStatusTip('Exit Athena')
        exit_dropButton.triggered.connect(self.close)
        trainMenu.addAction(exit_dropButton)  # add button to dropdown menu

        '''Menu Bar: Graphs'''
        '''Histogram'''
        histogram_dropButton = QAction('Histogram', self)
        histogram_dropButton.setShortcut('Shift+H')
        histogram_dropButton.setStatusTip('Generate Histogram')
        # histogram_dropButton.triggered.openHistogramWindow() <-- TODO create window, enable histogram generation
        graphsMenu.addAction(histogram_dropButton)
        '''Scatterplot'''
        scatterplot_dropButton = QAction('Scatterplot', self)
        scatterplot_dropButton.setShortcut('Shift+S')
        scatterplot_dropButton.setStatusTip('Generate Scatterplot')
        # scatterplot_dropButton.triggered.openScattplotWindow() <-- TODO create window, enable scatterplot generation
        graphsMenu.addAction(scatterplot_dropButton)
        '''Loss'''
        lossGraph_dropButton = QAction('Loss', self)
        lossGraph_dropButton.setShortcut('Shift+L')
        lossGraph_dropButton.setStatusTip('Generate loss graph')
        # lossGraph_dropButton.triggered.openLossWindow() <-- TODO create window, enable loss generation.
        graphsMenu.addAction(lossGraph_dropButton)
        '''Elapsed Time'''
        timeGraph_dropButton = QAction('Elapsed Time', self)
        timeGraph_dropButton.setShortcut('Shift+T')
        timeGraph_dropButton.setStatusTip('Generate loss graph')
        # timeGraph_dropButton.triggered.openLossWindow() <-- TODO create window, enable time elapsed graph.
        graphsMenu.addAction(timeGraph_dropButton)
        '''EEG'''
        eegGraph_dropButton = QAction('Electroencephalography Graph (Yes, you can)', self)
        eegGraph_dropButton.setShortcut('Shift+E')
        eegGraph_dropButton.setStatusTip('Generate EEG graph')
        # eegGraph_dropButton.triggered.openEEGWindow() <-- TODO create window, enable EEG graph
        graphsMenu.addAction(eegGraph_dropButton)

        '''Menu Bar: Help'''
        '''Help Center'''
        helpCenter_dropButton = QAction('Help Center', self)
        helpCenter_dropButton.setShortcut('Ctrl+H')
        helpCenter_dropButton.setStatusTip('Generate loss graph')
        # helpCenter_dropButton.triggered.openHelpCenterWindow() <-- TODO create window, Create help center.
        helpMenu.addAction(helpCenter_dropButton)
        '''About Athena'''
        aboutAthena_dropButton = QAction('About Athena', self)
        aboutAthena_dropButton.setShortcut('Ctrl+A')
        aboutAthena_dropButton.setStatusTip('Learn about Athena')
        # aboutAthena_dropButton.triggered.openHelpCenterWindow() <-- TODO create window, create about center.
        helpMenu.addAction(aboutAthena_dropButton)
        '''About Developers'''
        aboutDevs_dropButton = QAction('Meet the Developers', self)
        aboutDevs_dropButton.setShortcut('Ctrl+M')
        aboutDevs_dropButton.setStatusTip('Learn about the developers! :)')
        aboutDevs_dropButton.triggered.connect(self.AboutDevsWindow.show)
        # aboutDevs_dropButton.triggered.openDevsWindow() <-- TODO create window, create aboutDevs Center, enable portfolio linking.
        helpMenu.addAction(aboutDevs_dropButton)

        '''
        Panel options
        '''
        #panel_options = self.dockWidgetArea()

        '''
        Panel Canvas
        '''
        #panel_canvas = self.dockWidgetArea()

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #Set the style of the entire GUI
    app.setStyleSheet(open('CSS.cfg').read())
    ex = AthenaLaunchpad()
    sys.exit(app.exec_())