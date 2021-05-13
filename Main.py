from multiprocessing import Process, freeze_support

import Process1
import Process2

import sys

gExampleProcess1 = None
gExampleProcess2 = None

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def Exitting():

    global gExampleProcess1
    global gExampleProcess2

    print("bye")
    gExampleProcess1.join()
    gExampleProcess2.join()
    sys.exit()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    global gExampleProcess1
    global gExampleProcess2

    Params = {"Process1": 15, "Process2" : 12};

    gExampleProcess1 = Process(target=Process1.Test, args=(Params,))
    gExampleProcess2 = Process(target=Process2.Test, args=(Params,))

    gExampleProcess1.start()
    gExampleProcess2.start()

    try:
        while True:
            c = input() #read one bye at a time
            if c == 'x' or c == '^Z':
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

