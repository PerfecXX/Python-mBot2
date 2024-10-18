import cyberpi

cyberpi.reset_rotation(axis='all')
cyberpi.display.show_label("Accelerometer\nA:Start",16,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass
    
while True:
    x_accel = cyberpi.get_acc('x')
    y_accel = cyberpi.get_acc('y')
    z_accel = cyberpi.get_acc('z')

    cyberpi.display.show_label("X\n\nY\n\nZ\n\n",16,0,0,0)
    cyberpi.display.show_label("{}\n\n{}\n\n{}".format(x_accel,y_accel,z_accel),16,50,0,1)
