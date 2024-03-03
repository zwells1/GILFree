import sys
import time

if sys.platform.startswith("win"):
    import msvcrt as getChar
if sys.platform.startswith("linux"):
    import select
    import tty
    import termios

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def setupNonBlockingKeyboardExceptionMonitor():

    if sys.platform.startswith("win"):
        nonBlockingWindowsMonitor()
    elif sys.platform.startswith("linux"):
        nonBlockingLinuxMonitor()
    else:
        print("OS not accounted for test and implement keyboard exception monitor")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def confirmShutdown():
    #add later
    # press Y to proceed or any other key to ignore.
    print("To Be implemented")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def isLinuxKeyPressed():
    x = select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    print(x)
    return x


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def nonBlockingLinuxMonitor():

    old_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setcbreak(sys.stdin.fileno())

        while 1:
            time.sleep(0.3)

            if isLinuxKeyPressed():
                c = sys.stdin.read(1)
                if c == b'\x03':
                    break
        print("nonblock thread issue arose")

    except KeyboardInterrupt:
        print("keyboard interrupt safely shutdown")

    finally:
        print("main thread cleanup")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        return True


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def nonBlockingWindowsMonitor():

    try:
        while True:
            c =  getChar.getch()
            if c == b'\x03':
                break

    except KeyboardInterrupt:
        print("system beginning cleanup")
        return True

    return True

