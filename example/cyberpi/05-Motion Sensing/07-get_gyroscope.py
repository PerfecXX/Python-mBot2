import cyberpi

cyberpi.reset_rotation(axis='all')
cyberpi.display.show_label("Gyroscope\nA:Start",16,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass
    
while True:
    x_gyro = cyberpi.get_gyro('x')
    y_gyro = cyberpi.get_gyro('y')
    z_gyro = cyberpi.get_gyro('z')

    cyberpi.display.show_label("X\n\nY\n\nZ\n\n",16,0,0,0)
    cyberpi.display.show_label("{}\n\n{}\n\n{}".format(x_gyro,y_gyro,z_gyro),16,50,0,1)
