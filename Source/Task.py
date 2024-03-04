from multiprocessing import shared_memory

import signal
import sys
import time

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
class TaskObject:
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def __init__(self, params):
        self.name = params["Name"]
        self.delayTime = params["DelayTime"]
        self.data = params["Data"]
        print("initialized: " + str(self.name))

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def __del__(self):
        print("destructor final cleanup")

    # ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------
    def work(self):
        print("task data: ", str(self.data))
        time.sleep(self.delayTime)
    
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def taskEndCleanup(self):
        #clean up any subprocesses/subthreads that could be running
        #such as zmq context or sockets
        print("final cleanup task for: ", str(self.name))
    


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def CreateThreadTask(Params, isMainAlive):

    task = TaskObject(Params)

    while isMainAlive[0]:
        task.work()

    task.taskEndCleanup()
    del task

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def CreateProcessTask(Params):
    
    task = TaskObject(Params)

    #current process needs to be shutdown by main process ignore sigints
    signal.signal(signal.SIGINT, lambda x, y: None)

    shm = shared_memory.SharedMemory("isAlive")
    while shm.buf[0]:
        print("alive: ", shm.buf[0])
        task.work()

    task.taskEndCleanup()
    del task