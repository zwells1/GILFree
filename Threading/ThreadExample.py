from threading import Thread
import time
import sys

import NonBlockingKeyMonitor as KeyMonitor
import Process1
import Process2


global gExampleThread1
global gExampleThread2
global gIsAlive

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Exitting():

    global gExampleThread1, gExampleThread2, gIsAlive

    print("shutdown all threads")
    gIsAlive[0] = False #needs to be a modified value to work

    if gExampleThread1 is not None:
        gExampleThread1.join()

    if gExampleThread2 is not None:
        gExampleThread2.join()

    print("complete")
    sys.exit()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def globalSetup():

    global gExampleThread1, gExampleThread2, gIsAlive

    gIsAlive = [True] #needs to be mutable
    gExampleThread1 = None
    gExampleThread2 = None

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    global gExampleThread1, gExampleThread2, gIsAlive

    globalSetup()
    Params = {"Process1": 15, "Process2" : 12};

    gExampleThread1 = Thread(target=Process1.Test, args=(Params, gIsAlive))
    gExampleThread2 = Thread(target=Process2.Test, args=(Params,gIsAlive))
    gExampleThread1.start()
    gExampleThread2.start()
    print("started")

    KeyMonitor.setupNonBlockingKeyboardExceptionMonitor()
    Exitting()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    main(sys.argv[1:])

