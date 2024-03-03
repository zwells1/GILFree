from multiprocessing import shared_memory

import signal
import time

global gParams

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def ProcessDestructor():

    #clean up any subprocesses that could be running
    #such as zmq context or sockets
    print("Closing Process 2")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Test(Params):

    global gParams;

    print("Entering Process 2")

    #current process needs to be shutdown by main process ignore sigints
    signal.signal(signal.SIGINT, lambda x, y: None)

    gParams = Params
    shm = shared_memory.SharedMemory("isAlive")

    while shm.buf[0]:
        print("alive: ", shm.buf[0])
        Work()

    ProcessDestructor()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Work():

    global gParams

    print("Process 2 working, Parameter value: ", gParams["Process2"])
    #longer process needs to be closed without interrupting current process
    time.sleep(2.0)

