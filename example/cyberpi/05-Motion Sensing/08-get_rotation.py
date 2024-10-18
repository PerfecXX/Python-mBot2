import cyberpi

cyberpi.reset_rotation(axis='all')
cyberpi.display.show_label("Rotation\nA:Start",16,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass
    
while True:
    x_rotate = cyberpi.get_rotation('x')
    y_rotate = cyberpi.get_rotation('y')
    z_rotate = cyberpi.get_rotation('z')

    cyberpi.display.show_label("X\n\nY\n\nZ\n\n",16,0,0,0)
    cyberpi.display.show_label("{}\n\n{}\n\n{}".format(x_rotate,y_rotate,z_rotate),16,50,0,1)
