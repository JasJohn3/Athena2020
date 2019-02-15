from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


# note to self PYQT5 function .move(xCord, yCord) sets the exact location of the widget.
class Greeting(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Model Training'
        self.left = 520
        self.top = 280
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        super().__init__()
        self.title = 'Model Training'
        self.left = 520
        self.top = 280
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        greetingLabel = QLabel(self)
        greetingLabel.setGeometry(170, 200, 300, 50)
        greetingLabel.setText("Model training GUI and execution COMING SOON!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Greeting()
    ex.show()
    sys.exit(app.exec_())