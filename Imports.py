from __future__ import print_function

#     ==========FRONTEND IMPORTS==========
# ===== USED IN ATHENA_GUI =====
def getFrontEndImports():
    # =====USED IN DIALOGUES.py=====
    from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QComboBox, QSpinBox, QAction, QApplication
    from PyQt5.QtGui import QIcon, QDesktopServices, QColor
    from PyQt5.QtCore import QUrl
    import sys
    import Training

    # =====USED IN ATHENA_GUI.py=====
    import sys
    from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QComboBox, QSpinBox, QAction, QApplication
    from PyQt5.QtGui import QIcon, QColor, QPalette
    import PyQt5.QtCore as QtCore
    import Dialogues as DialoguesRail
    import PyQt5


#     ==========BACKEND IMPORTS==========
''' ===== USED IN: GENERATOR, DISCRIMINATOR, TRAINING===== '''
def getBackendImports():

    import torch
    import torch.nn as nn
    import torch.nn.parallel
    import torch.optim as optim
    import torch.utils.data
    import torchvision.datasets as dset
    import torchvision.transforms as transforms
    import torchvision.utils as vutils
    from torch.autograd import Variable
    import os
    import Generator
    import Discriminator




