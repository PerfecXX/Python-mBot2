import cyberpi, mbot2

angle = 90

cyberpi.display.show_label("mBot2 Servo ",16,0,0,0)
#            s1,s2,s3,s4,all
mbot2.servo_set(angle,"all")

while True:
    cyberpi.display.show_label("Current Angle:\nS1:{}".format(angle),16,0,36,1)
    if cyberpi.controller.is_press('up'):
        if angle < 180:
            angle += 1
        else:
            angle = angle
    elif cyberpi.controller.is_press('down'):
        if angle > 0:
            angle -= 1
        else:
            angle = angle
    elif cyberpi.controller.is_press('middle'):
        angle = 90
    
    mbot2.servo_set(angle,"s1")
    
