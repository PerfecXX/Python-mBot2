import cyberpi, mbot2

cyberpi.display.show_label("mBot2 Servo ",16,0,0,0)

#            s1,s2,s3,s4,all
mbot2.servo_set(90,"all")

while True:

    s1_angle = mbot2.servo_get("s1")
    cyberpi.display.show_label("current angle\nS1:{}".format(s1_angle),16,0,20,1)

    if cyberpi.controller.is_press('up'):
        mbot2.servo_set(180,"s1")
    
    elif cyberpi.controller.is_press('down'):
        mbot2.servo_set(0,"s1")
    
    elif cyberpi.controller.is_press('middle'):
        mbot2.servo_set(90,"s1")
    
