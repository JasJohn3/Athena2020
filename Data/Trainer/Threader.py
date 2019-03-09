from multiprocessing import process
from Data.Trainer.Epoch import Trainer
import threading
import time
import pandas

###############################################   Text Thread   ###############################################
class Loss_Log_Thread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        while True:
            print("Start Thread", self.name)
            File_Loss_Reader()
            time.sleep(self.delay)

###############################################   CSV THREAD    ###############################################
class ATHENA_CSV_Thread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Start Thread", self.name)
        while True:
            self.File_ATHENA_CSV_Reader()
            time.sleep(self.delay)

    def File_ATHENA_CSV_Reader(self):
        df = pandas.read_csv('ATHENA.csv')
        print(df)
        return df

def File_Loss_Reader():
    with open('Neural Network Loss.txt', 'r') as loss:
        contents = loss.read()
        while contents != 0:
            print(contents)
            #QTrainWidget.outputLog_TextBox.textCursor().insertHtml('Test')
            time.sleep(4)
            loss.close()

def begin(epochs):
   GAN = Trainer()
   GAN.Train(epochs)


def createThread(epochs):
    t1 = Loss_Log_Thread("Thread 1", 12)
    t1.daemon=True
    t1.start()
    t2 = ATHENA_CSV_Thread("Thread 2", 12)
    t2.daemon=True
    t2.start()
    begin(epochs)