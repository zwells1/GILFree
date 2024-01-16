import sys
import time

gParams = None;

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def ProcessDestructor():

    #clean up any subprocesses that could be running
    #such as zmq context or sockets
    print("Closing Process 2")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Test(Params, isMainAlive):

    global gParams

    print("Entering Process 2")

    gParams = Params

    while isMainAlive[0]:
        Work()

    ProcessDestructor()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Work():

    global gParams;
    print("process 2", gParams["Process2"])
    time.sleep(0.75)

