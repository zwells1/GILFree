import time
import sys
import select
import tty
import termios

def isKeyboardPressed():
        x = select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
        print(x)
        return x

old_settings = termios.tcgetattr(sys.stdin)

try:
    tty.setcbreak(sys.stdin.fileno())

    i = 0
    while 1:
        time.sleep(0.3)
        print(i)
        i += 1

        if isKeyboardPressed():
            c = sys.stdin.read(1)
            if c == '\x1b':         # x1b is ESC
                break
    print("end of try cleanup")
finally:
    print("finally cleanup")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

