from multiprocessing import process
from Debug.trainer_class import Trainer
import threading
import time

###############################################   CSV FILE    ###############################################



###############################################   CSV READ FILE    ###############################################
def File_ATHENA_CSV_Reader():
    with open('ATHENA.csv', 'r') as loss:
        read = 100
        contents = {}
        contents = loss.read()
        while contents != 0:
            print(contents)
            time.sleep(12)
###############################################   CSV READ FILE    ###############################################

###############################################   CSV THREAD    ###############################################
class ATHEN_CSV_Thread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Start Thread", self.name)
        ATHENA_CSV_Reader(self.name, self.delay)
        print("End Thread", self.name)

###############################################   External Function   ###############################################
def ATHENA_CSV_Reader(name_of_thread, delay):
    time.sleep(delay)
    File_ATHENA_CSV_Reader()
    print(name_of_thread, "----------", time.time())
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
        print("Start Thread", self.name)
        Loss_Log_Reader(self.name, self.delay)
        print("End Thread", self.name)
###############################################   External Function   ###############################################
def Loss_Log_Reader(name_of_thread, delay):
    time.sleep(delay)
    File_Loss_Reader()
    print(name_of_thread, "----------", time.time())

###############################################   Text Thread   ###############################################
def File_Loss_Reader():
    with open('Neural Network Loss.txt', 'r') as loss:
        contents = []
        contents = loss.read()
        while contents != 0:
            print(contents)
            contents = loss.read()
            time.sleep(12)


###############################################   Text FILE    ###############################################


###############################################   Multiprocess    ###############################################
def begin():
   GAN = Trainer()
   GAN.Train()
###############################################   Multiprocess    ###############################################

if __name__== '__main__':
    t1 = Loss_Log_Thread("Thread 1", 12)
    t1.start()
    t2 = ATHEN_CSV_Thread("Thread 2", 12)
    t2.start()
    p = process(Target =begin())
    t1.join()
    t2.join()







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