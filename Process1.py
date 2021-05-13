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
def Test(Params):

    global gParams;

    print("Entering Process 1")

    gParams = Params;

    try:
        while True:
            Work()

    except KeyboardInterrupt:
        ProcessDestructor()

    ProcessDestructor()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Work():

    global gParams;

    print("Process 1 working, Parameter value: " + str(gParams["Process1"]))
    time.sleep(1)

