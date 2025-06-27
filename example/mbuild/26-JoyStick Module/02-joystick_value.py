import cyberpi, mbuild

while:
    
    x = mbuild.joystick.get_value('x', 1)
    y = mbuild.joystick.get_value('y', 1)
    
    cyberpi.display.show_label(x, 12, 0, 0, index = 0)
    cyberpi.display.show_label(y, 12, 0, 16, index = 1)
