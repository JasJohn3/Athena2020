from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#from matplotlib.colors import ListedColormap


class QHistogramWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setParent(parent)
        self.GVals = []
        self.DVals = []
        self.initUI()


    def initUI(self):
        #Initialize instance to plot on.
        self.figure = plt.figure()

        #Create a canvas for the plot to rest on.
        #This canvas takes the figure instance as a param to __init__
        self.canvas = FigureCanvas(self.figure)

        #Create navigation widget.
        #Navigation widget takes the canvas widget and a parent to initialize
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.figure.clear()

        #create an axis
        self.ax = self.figure.add_subplot(111)

        #plot data
        self.ax.set_facecolor('black')
        #self.ax.hist(self.GVals, bins='auto', color='cyan', alpha=0.7)
        self.ax.plot(self.GVals)
        #self.ax.hist(self.DVals, bins='auto', color='blue', alpha=None)
        self.ax.plot(self.DVals)
        self.ax.set_title("GAN Loss")
        self.ax.set_xlabel('Iterations')
        self.ax.set_ylabel('Loss')
        self.ax.legend()

        #refresh
        self.canvas.draw()

        #plt.figure(figsize=(10,5))
        #plt.title("Histogram - Loss / Iterations")
        #plt.plot(xVals, label="G")
        #plt.plot(yVals, label="D")
        #plt.xlabel("Iterations")
        #plt.ylabel("Loss")

        #plt.legend()
        #plt.show()
    # def set_GVals(self, value ):
    #     self.GVals.append(value)
    #     print(self.GVals)
    #     self.ax.hist(self.GVals, bins='auto', color='cyan', alpha=0.7, rwidth=0.85)
    #
    # def set_DVals(self, value):
    #     self.DVals.append(value)
    #     print(self.DVals)
    #     self.ax.hist(self.DVals, bins='auto', color='blue', alpha=None)
        # , current, training
        # self.GVals[0] * training
        # self.GVals[current] = value
    def updateGraph(self, ValG = None, ValD = None, total_training = None, current_Training = None):

        #self.GVals.append(ValG)
        #self.DVals.append(ValD)
        self.GVals.append(ValG)
        self.DVals.append(ValD)
        self.ax.clear()
        self.ax.set_facecolor('black')
        #self.ax.hist(self.GVals, bins=total_training, color='cyan', alpha=0.7)
        self.ax.plot(self.GVals, label='Generator')
        #self.ax.hist(self.DVals, bins=total_training, color='blue', alpha=None)
        self.ax.plot(self.DVals, label='Discriminator')
        self.ax.set_title("GAN Loss")
        self.ax.set_xlabel('Iterations')
        self.ax.set_ylabel('Loss')
        self.ax.legend()
        self.canvas.draw()
        #self.parent().parent().parent().parent().parent().repaint()

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)
        # self.introduction_Label = QLabel(self)
        # self.introduction_Label.setText("No training data received...")
