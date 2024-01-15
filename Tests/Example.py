
"""
Use Case
--------
End-user has a program that runs forever.
The end-user terminates the program by using ctl-c.
Goal
----
Demonstrate that even though a child process is properly terminated,
have to capture the KeyboardInterrupt exception to avoid littering
the screen output with its traceback.
Output in file ctl_c_KeyboardInterrupt_captured_output.txt.
"""

from multiprocessing import Process
from signal import signal, SIGINT
from time import sleep
import sys

DEBUG = False


def some_fcn():

    """
    Loop waiting for ctl-c
    """

    try:

        print("---")

        while True:
            print("Waiting for ctl-c")
            sleep(1)

    except KeyboardInterrupt:
        # Expected exception.
        # Can ignroe it.
        print("keyboard inter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        pass
    print("ready to leave!!!!!!!!!!!!!!!!!")


def terminate_proc(signal_received, frame):

    """
    Explicitly terminate some child process prior to exiting program.
    """

    print("---")
    print("SIGINT or CTRL-C detected. Exiting gracefully")

    if DEBUG:
        print("---")
        print("Signal Received: ", signal_received)
        print("Frame: ", frame)

    print("---")
    print("Terminating some child process - PID: ", some_child_process.pid)
    some_child_process.terminate()
    some_child_process.join()
    print("---")

    #sys.exit(0)


if __name__ == "__main__":

    signal(SIGINT, terminate_proc)

    # Create child process
    some_child_process = Process(target=some_fcn, name="some_child_process")
    some_child_process.start()

    print("---")
    print("Press ctrl-c to terminate processing.")

