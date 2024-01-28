import cyberpi
from time import sleep

cyberpi.led.on(255,0,0,id=1)
while True:
    # shift all the colors 1 step to the right.
    # (If it is negative, it will be left shifting.)
    cyberpi.led.move(1)
    sleep(1)
