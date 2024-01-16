from threading import Thread
import time
import sys

import Process1
import Process2

if sys.platform.startswith("win"):
    import msvcrt as getChar
if sys.platform.startswith("linux"):
    import getch as getChar


global gExampleThread1
global gExampleThread2
global gIsAlive

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Exitting():

    global gExampleThread1, gExampleThread2, gIsAlive

    print("bye")
    gIsAlive[0] = False #needs to be a modified value to work
    
    if gExampleThread1 is not None:
        gExampleThread1.join()
    
    if gExampleThread2 is not None:
        gExampleThread2.join()
    
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
    try:
        while True:
            c =  getChar.getch()
            if c == b'x' or c == b'Z':# or c == '^Z':
                break

    except KeyboardInterrupt:
        Exitting()


    Exitting()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    main(sys.argv[1:])

