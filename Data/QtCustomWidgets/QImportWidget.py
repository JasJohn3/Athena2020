from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter

class QImportWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        ###
        #LABELS
        ###
        self.instruction_Label = QLabel(self)
        self.instruction_Label.setText("Import your dataset here. ")
        self.warning_Label = QLabel(self)
        self.warning_Label.setText("WARNING: cifar10, cifar100, mnist, stl10, lsun, and imagenet ONLY")
        self.warning_Label.move(0,25)

        ###
        #BUTTONS
        ###
        self.import_Button = QPushButton(self)
        self.import_Button.setText("Import Dataset")
        self.import_Button.setGeometry(285, 50, 100, 30)
        self.import_Button.clicked.connect(self.file_open)

        ###
        #OUTPUT LOG
        ###
        self.readFile_Data = QTextEdit(self)
        self.readFile_Data.setReadOnly(True)
        self.readFile_Data.setLineWrapMode(QTextEdit.NoWrap)
        self.readFile_Data.verticalScrollBar()
        self.readFile_Data.horizontalScrollBar()
        self.readFile_Data.setMinimumWidth(295)
        self.readFile_Data.setGeometry(0, 250, self.width() - (self.readFile_Data.x() + 4),
                                           self.height() - (self.readFile_Data.y() + 4))

    def file_open(self):
        name = QFileDialog()
        file = open(name.getOpenFileName(self, 'Import A Dataset'), 'r')

        self.GUI()

        with file:
            text = file.read()
            self.readFile_Data.setText(text)

        file.close()

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)



