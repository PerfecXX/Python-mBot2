import cyberpi, mbuild

#                                 axis = x,y,z,all
mbuild.motion_sensor.reset_rotation('all', 1)

while:

    pitch = mbuild.motion_sensor.get_pitch(1)
    roll =  mbuild.motion_sensor.get_roll(1)
    
    cyberpi.display.show_label(pitch, 12, 0,0, index = 0)
    cyberpi.display.show_label(roll, 12, 0,20, index = 1)
