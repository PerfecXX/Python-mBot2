import cyberpi, mbot2

cyberpi.display.show_label("mBot2 Straight",16,0,0,0)
cyberpi.display.show_label("A:Start Moving!",16,0,20,1)

while True:
    
    while not cyberpi.controller.is_press('a'):
        pass

    cyberpi.display.show_label("Forward 100 cm",12,0,40,2)
    mbot2.straight(100)
    cyberpi.display.show_label("Backward 100 cm",12,0,40,2)
    mbot2.straight(-100)
    cyberpi.display.show_label("Finished!",12,0,40,2)

