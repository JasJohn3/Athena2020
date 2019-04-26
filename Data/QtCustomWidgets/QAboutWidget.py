from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class QAboutWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        self.Athena_About_Browser = QWebEngineView(self)
        url = 'https://overclockedthompson.wixsite.com/athena'
        self.Athena_About_Browser.load(QUrl(url))
        self.Athena_About_Browser.show()

    def resizeEvent(self, QResizeEvent):
        self.Athena_About_Browser.setGeometry(0,0,self.width(),self.height())
    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)