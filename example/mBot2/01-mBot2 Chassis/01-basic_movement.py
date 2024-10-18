import cyberpi, mbot2

cyberpi.display.show_label("mBot2 Movement",16,0,0,0)
cyberpi.display.show_label("A:Start Moving!",16,0,20,1)

while True:
    
    while not cyberpi.controller.is_press('a'):
        pass

    cyberpi.display.show_label("Forward 60 RMP 1 Sec",12,0,40,2)
    mbot2.forward(60,1)
    cyberpi.display.show_label("Backward 60 RMP 1 Sec",12,0,40,2)
    mbot2.backward(60,1)
    cyberpi.display.show_label("Turn Left 60 RMP 1 Sec",12,0,40,2)
    mbot2.turn_left(60,1)
    cyberpi.display.show_label("Turn Right 60 RMP 1 Sec",12,0,40,2)
    mbot2.turn_right(60,1)
    cyberpi.display.show_label("Finished!",12,0,40,2)
