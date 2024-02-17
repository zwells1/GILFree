from multiprocessing import freeze_support, Process, shared_memory
import time
import sys
import Process1
import Process2

if sys.platform.startswith("win"):
    import msvcrt as getChar
if sys.platform.startswith("linux"):
    import getch as getChar


gExampleProcess1 = None
gExampleProcess2 = None
try:
    shm = shared_memory.SharedMemory("isAlive", create=True, size=1)
except FileExistsError:#is false in case program crashed out last time
    shm = shared_memory.SharedMemory("isAlive")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Exitting():

    global gExampleProcess1
    global gExampleProcess2
    global shm

    print("bye")
    shm.buf[0] = False
    gExampleProcess1.join()
    gExampleProcess2.join()
    shm.close()
    shm.unlink()
    sys.exit()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    global gExampleProcess1
    global gExampleProcess2
    global shm

    Params = {"Process1": 15, "Process2" : 12};    
    shm.buf[0] = True


    gExampleProcess1 = Process(target=Process1.Test, args=(Params,))
    gExampleProcess2 = Process(target=Process2.Test, args=(Params,))
    print("starting process")
    gExampleProcess1.start()
    gExampleProcess2.start()
    print("started")
    try:
        while True:
            c =  getChar.getch()
            if c == b'\x03':
                break

    except KeyboardInterrupt:
        Exitting()


    Exitting()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    if sys.platform.startswith('win'):
        # On Windows is needed to handle Processes
        freeze_support()

    main(sys.argv[1:])

