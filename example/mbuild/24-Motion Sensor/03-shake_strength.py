import cyberpi, mbuild

#                                 axis = x,y,z,all
mbuild.motion_sensor.reset_rotation('all', 1)

while:

    shake_strength = mbuild.motion_sensor.get_shake_strength(1)
    
    cyberpi.display.show_label(shake_strength, 12, 0,0, index = 1)
