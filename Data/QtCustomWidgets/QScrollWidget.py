from PyQt5.QtWidgets import *

class QScrollWidet(QScrollBar):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)