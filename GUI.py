# Abstract: Athena Launchpad GUI: generates UI for Athena texture generator
# Author: Zack Thompson
# last updates February 1, 2019

# Version 0.01

# TODO Athena Neural network graph Owl Logo.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor, QPalette
from PyQt5.QtCore import *
import GUI_Init as init


class AthenaLaunchpad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Athena Launchpad'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        # self.initUI()

        # def initUI() <--DANGER THIS WILL BREAK THE ENTIRE GUI
        # set background color palette
        self.setAutoFillBackground(True)
        athenaMainMenu_BackgroundColor = self.palette()
        athenaMainMenu_BackgroundColor.setColor(self.backgroundRole(),
                                                QColor(28, 28, 28))  # set background color to black.
        self.setPalette(athenaMainMenu_BackgroundColor)

        self.testWindowButton = init.Greeting()
        #TODO on startup throw gui at 0,0 on screen.
        #TODO add the panel behind the spinboxes.

        # ==========================================INITIALIZE UI=========================================
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #         ==GREETING LABEL==
        greeting_Label = QLabel("<font color = white>Welcome to Athena!</font>", self)
        greeting_Label.move(0, 20)

        # =====MUTABLE CENTRAL OUTPUT PROMPT WIDGET=====
        mutableCentral = QWidget()
        self.setCentralWidget(mutableCentral)
        mutableCentral.move(320, 200)
        # =====INSTRUCTIONS POP UP WINDOW=====
            #TODO make external help pop up script.

        # ========================TEXTURE TYPE COMBO BOX============================================
        #         ==COMBO BOX LABEL==
        textureType_Label = QLabel("<font color = white font size = 5>Texture Type</font>", self)
        textureType_Label.move(0, 50)
        #         ==DROP DOWN MENU==
        texture_DropDownMenu = QComboBox(self)
        texture_DropDownMenu.addItems(["<Select Texture>", "Stone", "Sand", "Grass", "Wooden", "Metallic"])
        texture_DropDownMenu.setToolTip('Select a texture to generate.')
        texture_DropDownMenu.resize(150, 32)
        texture_DropDownMenu.move(0, 80)

        # ========================IMAGE SIZE SPIN BOXES=============================================
        #         ==IMAGE SIZE LABEL==
        imageSize_Label = QLabel("<font color = white font size = 5>Image Size</font>", self)
        imageSize_Label.move(0, 120)

        #         ==WIDTH SPINBOX==
        widthSB_Label = QLabel("<font color = white font size = 4>Width:</font", self)
        widthSB_Label.move(0, 150)
        width_SpinBox = QSpinBox(self)
        width_SpinBox.setToolTip('WARNING: LARGER SIZES = LONGER GENERATION TIMES')
        width_SpinBox.move(75, 150)

        #         ==HEIGHT SPINBOX==
        heightSB_Label = QLabel("<font color = white font size = 4>Height:</font", self)
        heightSB_Label.move(0, 190)
        height_SpinBox = QSpinBox(self)
        height_SpinBox.setToolTip('WARNING: LARGER SIZES = LONGER GENERATION TIMES')
        height_SpinBox.move(75, 190)


        # ========================BUTTONS UNDER TRAIN MENU BAR=============================================
        #         ==INITIALIZATIONS==
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet(
            """QMenuBar { background-color: rgb(45, 45, 48); }""")  # set the background color of menu bar
        trainMenu = mainMenu.addMenu("Train")
        trainMenu.setStyleSheet("""QMenuBar::item { background: rgb(240, 240, 240); color: red; }""")
        graphsMenu = mainMenu.addMenu('Graphs')
        helpMenu = mainMenu.addMenu('Help')

        # ===========================================TRAIN MENU===========================================

        #         ==Train Button==
        train_dropButton = QAction('Train', self)
        train_dropButton.setShortcut('Ctrl+T')
        train_dropButton.setStatusTip('Train a model')
        train_dropButton.triggered.connect(self.testWindowButton.show)
        trainMenu.addAction(train_dropButton)  # add test button to dropdown menu

        #         ==Custom Dataset Button==
        customData_dropButton = QAction('Import Dataset', self)
        customData_dropButton.setShortcut('Ctrl+C')
        customData_dropButton.setStatusTip('Generate based on your own dataset')
        # custom_dropButton.triggered.openCustomizeDatasetWindow() <-- TODO create temporary window and enable dataset upload.
        trainMenu.addAction(customData_dropButton)  # add button to dropdown menu

        # ==Exit Button==
        exit_dropButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_dropButton.setShortcut('Ctrl+Q')
        exit_dropButton.setStatusTip('Exit Athena')
        exit_dropButton.triggered.connect(self.close)
        trainMenu.addAction(exit_dropButton)  # add button to dropdown menu

        # ===========================================GRAPHS MENU===========================================
        #       ===Historgram button===
        histogram_dropButton = QAction('Histogram', self)
        histogram_dropButton.setShortcut('Shift+H')
        histogram_dropButton.setStatusTip('Generate Histogram')
        # histogram_dropButton.triggered.openHistogramWindow() <-- TODO create window, enable histogram generation
        graphsMenu.addAction(histogram_dropButton)

        #       ===Scatterplot button===
        scatterplot_dropButton = QAction('Scatterplot', self)
        scatterplot_dropButton.setShortcut('Shift+S')
        scatterplot_dropButton.setStatusTip('Generate Scatterplot')
        # scatterplot_dropButton.triggered.openScattplotWindow() <-- TODO create window, enable scatterplot generation
        graphsMenu.addAction(scatterplot_dropButton)

        #       ===Loss Button===
        #           |       |  |
        #
        #           | |     | _
        #
        lossGraph_dropButton = QAction('Loss', self)
        lossGraph_dropButton.setShortcut('Shift+L')
        lossGraph_dropButton.setStatusTip('Generate loss graph')
        # lossGraph_dropButton.triggered.openLossWindow() <-- TODO create window, enable loss generation.
        graphsMenu.addAction(lossGraph_dropButton)

        #       ===Time Elapsed Button===
        timeGraph_dropButton = QAction('Elapsed Time', self)
        timeGraph_dropButton.setShortcut('Shift+T')
        timeGraph_dropButton.setStatusTip('Generate loss graph')
        # timeGraph_dropButton.triggered.openLossWindow() <-- TODO create window, enable time elapsed graph.
        graphsMenu.addAction(timeGraph_dropButton)

        #       ===EEG Button===
        eegGraph_dropButton = QAction('Electroencephalography Graph (Yes, you can)', self)
        eegGraph_dropButton.setShortcut('Shift+E')
        eegGraph_dropButton.setStatusTip('Generate EEG graph')
        # eegGraph_dropButton.triggered.openEEGWindow() <-- TODO create window, enable EEG graph
        graphsMenu.addAction(eegGraph_dropButton)

        # ===========================================HELP MENU===========================================

        #       ===Help Center Button===
        helpCenter_dropButton = QAction('Help Center', self)
        helpCenter_dropButton.setShortcut('Ctrl+H')
        helpCenter_dropButton.setStatusTip('Generate loss graph')
        # helpCenter_dropButton.triggered.openHelpCenterWindow() <-- TODO create window, Create help center.
        helpMenu.addAction(helpCenter_dropButton)

        #       ===About Athena Button===
        aboutAthena_dropButton = QAction('About Athena', self)
        aboutAthena_dropButton.setShortcut('Ctrl+A')
        aboutAthena_dropButton.setStatusTip('Learn about Athena')
        # aboutAthena_dropButton.triggered.openHelpCenterWindow() <-- TODO create window, create about center.
        helpMenu.addAction(aboutAthena_dropButton)

        #       ===About Developers===
        aboutDevs_dropButton = QAction('Meet the Developers', self)
        aboutDevs_dropButton.setShortcut('Ctrl+M')
        aboutDevs_dropButton.setStatusTip('Learn about the developers! :)')
        # aboutDevs_dropButton.triggered.openDevsWindow() <-- TODO create window, create aboutDevs Center, enable portfolio linking.
        helpMenu.addAction(aboutDevs_dropButton)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AthenaLaunchpad()
    sys.exit(app.exec_())