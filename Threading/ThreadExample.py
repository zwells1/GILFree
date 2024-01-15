from threading import Thread
import time
import sys

import Process1
import Process2

if sys.platform.startswith("win"):
    import msvcrt as getChar
if sys.platform.startswith("linux"):
    import getch as getChar


gExampleThread1 = None
gExampleThread2 = None
gIsAlive = [True] #need to be mutable class

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Exitting():

    global gExampleThread1
    global gExampleThread2
    global gIsAlive

    print("bye")
    gIsAlive = [False]
    print("alive val ", gIsAlive)
    gExampleThread1.join()
    gExampleThread2.join()
    print("joined")
    sys.exit()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    global gExampleThread1
    global gExampleThread2
    global gIsAlive

    Params = {"Process1": 15, "Process2" : 12};    


    gExampleThread1 = Thread(target=Process1.Test, args=(Params, gIsAlive,))
    gExampleThread2 = Thread(target=Process2.Test, args=(Params,gIsAlive,))
    print("starting process")
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

