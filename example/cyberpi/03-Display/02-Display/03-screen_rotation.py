import cyberpi

cyberpi.display.show_label("A:Rotate",24,12,50,0)

while True:
    while not cyberpi.controller.is_press('a'):
        pass
    cyberpi.display.rotate_to(90)
    cyberpi.display.show_label("R90",24,50,50,0)
    
    while not cyberpi.controller.is_press('a'):
        pass
    cyberpi.display.rotate_to(180)
    cyberpi.display.show_label("R180",24,50,50,0)
    
    while not cyberpi.controller.is_press('a'):
        pass
    cyberpi.display.rotate_to(-90)
    cyberpi.display.show_label("R-90",24,50,50,0)
    
    while not cyberpi.controller.is_press('a'):
        pass
    cyberpi.display.rotate_to(0)
    cyberpi.display.show_label("R0",24,50,50,0)
