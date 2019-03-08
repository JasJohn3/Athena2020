from multiprocessing import process
from Data.Trainer.Epoch import Trainer
import threading
import time
import pandas
from data.QtCustomWidgets import QTrainWidget

###############################################   CSV FILE    ###############################################



###############################################   CSV READ FILE    ###############################################


###############################################   CSV READ FILE    ###############################################

    # with open('ATHENA.csv', 'r') as CSV:
    #     contents = []
    #     contents = CSV.read()
    #     while contents != 0:
    #         print(contents[-6])
    #         time.sleep(3)
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


###############################################   External Function   ###############################################
# def ATHENA_CSV_Reader(name_of_thread, delay):
#     time.sleep(delay)
#     File_ATHENA_CSV_Reader()
#     print(name_of_thread, "----------",time.time())
###############################################   External Function   ###############################################

###############################################   CSV THREAD    ###############################################


###############################################   CSV FILE    ###############################################


###############################################   Text FILE    ###############################################

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

###############################################   External Function   ###############################################
# def Loss_Log_Reader(name_of_thread, delay):
#     time.sleep(delay)
#     File_Loss_Reader()
#     print(name_of_thread, "----------",time.time())

###############################################   Text Thread   ###############################################
def File_Loss_Reader():
    with open('Neural Network Loss.txt', 'r') as loss:
        contents = loss.read()
        while contents != 0:
            print(contents)
            QTrainWidget.outputLog_TextBox.textCursor().insertHtml('Test')
            time.sleep(4)
            loss.close()


###############################################   Text FILE    ###############################################


###############################################   Multiprocess    ###############################################
def begin():
   GAN = Trainer()
   GAN.Train()
###############################################   Multiprocess    ###############################################

def createThread():
    t1 = Loss_Log_Thread("Thread 1", 12)
    t1.daemon=True
    t1.start()
    t2 = ATHENA_CSV_Thread("Thread 2", 12)
    t2.daemon=True
    t2.start()
    #p = process(Target =begin())







#import _thread
#import threading

# def print_epoch(name_of_thread, delay):
#         Trainer.Train()
#         time.sleep(delay)
#         print(name_of_thread, "----------",'Running')
# class MyThread():
#     def __init__(self, name, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#
#     def run(self):
#         print("Start Thread", self.name)
#         print_epoch(self.name,self.delay)
#         print("End Thread", self.name)