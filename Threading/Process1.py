import sys
import time

gParams = None;

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def ProcessDestructor():

    #clean up any subprocesses that could be running
    #such as zmq context or sockets
    print("Closing Process 1")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Test(Params, isMainAlive):

    global gParams;

    print("Entering Process 1")

    gParams = Params;

    while isMainAlive[0]:
        Work()

    ProcessDestructor()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Work():

    global gParams;
    print("process 1", gParams["Process1"])
    time.sleep(2)

