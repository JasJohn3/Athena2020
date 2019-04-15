from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class QSessionWindow(QDialog, ):

    def __init__(self):
        super().__init__()
        #Basic foundation parameters
        self.setWindowIcon(QIcon('Data/Athena_v1.ico'))
        self.setWindowTitle('Athena - Create New Session')
        self.setMinimumSize(640,400)

        #Set window to pop in center right of screen.
        window = self.frameGeometry()
        self.move(window.topRight())
        self.setParent(parent)

        self.initUI()

    def initUI(self):
        temp = QLabel(self)

