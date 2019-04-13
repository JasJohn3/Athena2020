from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets


class QHelpWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.welcomeHelp_Label = QLabel(self)
        self.welcomeHelp_Label.setText("ATHENA Help")

        ###
        #WELCOME TEXT BOX
        ###
        self.welcome_Textbox = QTextEdit(self)
        self.welcome_Textbox.setReadOnly(True)
        self.welcome_Textbox.setLineWrapMode(QTextEdit.NoWrap)
        self.welcome_Textbox.verticalScrollBar()
        self.welcome_Textbox.horizontalScrollBar()
        self.welcome_Textbox.setGeometry(0, 50, self.width() - (self.welcome_Textbox.x() + 4),
                                           self.height() - (self.welcome_Textbox.y() + 4))

    def resizeEvent(self,*args, **kwargs):
        self.welcome_Textbox.setGeometry(4, 21, self.width() * .5, self.height() - 24)