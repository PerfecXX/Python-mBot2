import cyberpi, mbuild

#                                 axis = x,y,z,all
mbuild.motion_sensor.reset_rotation('all', 1)

while:
    
    x = mbuild.motion_sensor.get_rotation('x', 1)
    y = mbuild.motion_sensor.get_rotation('y', 1)
    z = mbuild.motion_sensor.get_rotation('z', 1)

    cyberpi.display.show_label(x, 12, 0,0, index = 0)
    cyberpi.display.show_label(y, 12, 0,20, index = 1)
    cyberpi.display.show_label(z, 12, 0,40, index = 2)
