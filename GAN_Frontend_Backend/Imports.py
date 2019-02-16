from __future__ import print_function
#===== PYTHON STDLIB IMPORTS =====
import sys

#===== PYTORCH IMPORTS =====
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.autograd import Variable

#===== PYQT5 IMPORTS =====
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor, QPalette
from PyQt5.QtCore import *
import Dialogues as hi
import Training as Trainer


