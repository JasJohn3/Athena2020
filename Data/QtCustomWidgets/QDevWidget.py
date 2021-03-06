from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices, QPainter
from PyQt5.QtCore import QUrl

class QDevWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    # Allows for linking to personal websites of developers.
    def link(self, linkstr):
        QDesktopServices.openUrl(QUrl(linkstr))

    def initUI(self):
        greetingLabel = QLabel(self)
        greetingLabel.setGeometry(170, 50, 300, 50)
        greetingLabel.setText(
            "<font color = white>About the developers: Click a link to visit their portfolio sites!</font>")

        JasonLink = QLabel(self)
        JasonLink.linkActivated.connect(self.link)
        JasonLink.setText('<a href="https://www.linkedin.com/in/jason-johnson-32a37354/">Jason Johnson</a>')
        JasonLink.move(50,50)

        TrevorLink = QLabel(self)
        TrevorLink.linkActivated.connect(self.link)
        TrevorLink.setText('<a href="https://trekinar.wixsite.com/portfolio">Trevor Kinard</a>')
        TrevorLink.move(50, 100)

        ZackLink = QLabel(self)
        ZackLink.linkActivated.connect(self.link)
        ZackLink.setText('<a href="https://www.linkedin.com/in/zack-thompson-24095b183/">Zack Thompson</a>')
        ZackLink.move(50, 150)

        WyattLink = QLabel(self)
        WyattLink.linkActivated.connect(self.link)
        WyattLink.setText('<a href ="https://www.linkedin.com/in/wyatt-dooley-8a4896156/"> Wyatt Dooley</a>')
        WyattLink.move(50,200)

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)