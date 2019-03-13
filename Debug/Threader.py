from multiprocessing import process
from Data.Trainer.Epoch import Trainer
from threading import Thread
import time
import pandas


def createThread(epochs):
    GAN = Trainer()
    Epochs_Thread = Thread(group=None, target=GAN.Train(epochs), name="Epochs Thread")
    Epochs_Thread.start()