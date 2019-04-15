from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import Data.QtCustomWidgets.QTrainWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.colors import ListedColormap


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


        # self.introduction_Label = QLabel(self)
        # self.introduction_Label.setText("No training data received...")


        self.figure.clear()

        #create an axis
        ax = self.figure.add_subplot(111)

        #plot data
        ax.set_facecolor('black')
        ax.hist(self.GVals, bins='auto', color='cyan', alpha=0.7, rwidth=0.85)
        ax.hist(self.DVals, bins='auto', color='blue', alpha=None)
        ax.set_title("GAN Loss")
        ax.set_xlabel('Iterations')
        ax.set_ylabel('Loss')
        ax.legend()

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


