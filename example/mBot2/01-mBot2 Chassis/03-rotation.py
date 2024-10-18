import cyberpi, mbot2

cyberpi.display.show_label("mBot2 Rotation",16,0,0,0)
cyberpi.display.show_label("A:Rotate Left\nB:Rotate Right",16,0,20,1)

while True:
    
    if cyberpi.controller.is_press('a'):
        cyberpi.display.show_label("Turn Left 90",12,0,60,2)
        mbot2.turn(-90)
    elif cyberpi.controller.is_press('b'):
        cyberpi.display.show_label("Turn Right 90",12,0,60,2)
        mbot2.turn(90)
