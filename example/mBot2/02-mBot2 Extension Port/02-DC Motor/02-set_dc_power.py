import cyberpi, mbot2
from time import sleep

cyberpi.display.show_label("mBot2 DC Motor ",16,0,0,0)

mbot2.motor_set(0,"all")

while True:
    m1_power = mbot2.motor_get("M1")
    cyberpi.display.show_label("current Power\nM1:{}".format(m1_power),16,0,20,1)

    if cyberpi.controller.is_press('up'):
       mbot2.motor_set(100,"all")
    
    elif cyberpi.controller.is_press('down'):
       mbot2.motor_set(-100,"all")
    
    elif cyberpi.controller.is_press('middle'):
        mbot2.motor_set(0,"all")
