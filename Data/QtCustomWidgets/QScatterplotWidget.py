from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter

class QScatterplotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        #self.initUI()

    # def initUI(self):
    #     self.noDataLabel = QLabel(self)
    #     self.noDataLabel.setText("No data received...")
    #
    #     class QHistogramWidget(QWidget):
    #         def __init__(self, parent=None):
    #             super().__init__()
    #             self.setParent(parent)
    #             self.initUI()
    #
    #         def initUI(self):
    #             # Initialize instance to plot on.
    #             self.figure = plt.figure()
    #
    #             # Create a canvas for the plot to rest on.
    #             # This canvas takes the figure instance as a param to __init__
    #             self.canvas = FigureCanvas(self.figure)
    #
    #             # Create navigation widget.
    #             # Navigation widget takes the canvas widget and a parent to initialize
    #             self.toolbar = NavigationToolbar(self.canvas, self)
    #
    #             layout = QVBoxLayout()
    #             layout.addWidget(self.toolbar)
    #             layout.addWidget(self.canvas)
    #             self.setLayout(layout)
    #
    #             # self.introduction_Label = QLabel(self)
    #             # self.introduction_Label.setText("No training data received...")
    #             xVals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 6, 7, 5, 3, 0, 9]
    #             yVals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 0, 6, 0, 8, 4, 2]
    #
    #             self.figure.clear()
    #
    #             # create an axis
    #             ax = self.figure.add_subplot(111)
    #
    #             # plot data
    #             ax.plot(xVals, '*-')
    #
    #             # refresh
    #             self.canvas.draw()

                # plt.figure(figsize=(10,5))
                # plt.title("Histogram - Loss / Iterations")
                # plt.plot(xVals, label="G")
                # plt.plot(yVals, label="D")
                # plt.xlabel("Iterations")
                # plt.ylabel("Loss")

                # plt.legend()
                # plt.show()

    def setGeometry(self, *__args):
        super().setGeometry(*__args)

    def paintEvent(self, event):
        super(type(self), self).paintEvent(event)
        styleSheet = QStyleOption()
        styleSheet.initFrom(self)
        paint = QPainter(self)
        styling = self.style()
        styling.drawPrimitive(QStyle.PE_CustomBase, styleSheet, paint, self)