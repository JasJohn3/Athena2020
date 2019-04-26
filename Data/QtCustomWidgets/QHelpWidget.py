from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class QHelpWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        # self.Athena_Help_Browser = QWebEngineView()
        # url = 'https://overclockedthompson.wixsite.com/athena/basic-interaction'
        # self.Athena_Help_Browser.load(QUrl(url))
        # self.Athena_Help_Browser.show()
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

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)