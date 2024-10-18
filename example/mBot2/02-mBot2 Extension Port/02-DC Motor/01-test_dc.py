import cyberpi, mbot2
from time import sleep

cyberpi.display.show_label("mBot2 DC Motor ",16,0,0,0)

mbot2.motor_set(100,"all")
sleep(1)
mbot2.motor_set(0,"all")
