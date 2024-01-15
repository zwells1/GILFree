from multiprocessing import shared_memory
import sys
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
def Test(Params, isMainAlive):
    global gParams
    global shm

    print("Entering Process 1")

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

    #print("Process 1 working, Parameter value: " + str(gParams["Process1"]))
    print("erer")
    time.sleep(3)

