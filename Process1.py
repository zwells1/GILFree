from multiprocessing import shared_memory

import signal
import time

gParams = None
shm = None
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def ProcessDestructor():
    global shm
    #clean up any subprocesses that could be running
    #such as zmq context or sockets
    shm.close()
    print("Closing Process 1")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Test(Params):
    global gParams
    global shm

    print("Entering Process 1")

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
    print("Process 1 working, Parameter value: ", gParams["Process1"])
    time.sleep(3)

