from threading import Thread
import time
import sys

import Source.NonBlockingKeyMonitor as KeyMonitor
import Source.Task as Task


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
    Params = {"Task1": {"DelayTime" : 5.0, "Data": 15, "Name": "Task1"},
              "Task2" : {"DelayTime" : 0.75, "Data": 12, "Name": "Task2"}}

    gExampleThread1 = Thread(target=Task.CreateThreadTask, args=(Params["Task1"], gIsAlive))
    gExampleThread2 = Thread(target=Task.CreateThreadTask, args=(Params["Task2"], gIsAlive))
    gExampleThread1.start()
    gExampleThread2.start()
    print("started")

    KeyMonitor.setupNonBlockingKeyboardExceptionMonitor()
    Exitting()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    main(sys.argv[1:])

