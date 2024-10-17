import cyberpi

cyberpi.display.show_label("Continuous motions\nA:Start",12,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass

while True:
    shake = cyberpi.is_shake()
    wave_up = cyberpi.is_waveup()
    wave_down = cyberpi.is_wavedown()
    wave_left = cyberpi.is_waveleft()
    wave_right = cyberpi.is_waveright()
    free_fall = cyberpi.is_freefall()
    cw = cyberpi.is_clockwise()
    ccw = cyberpi.is_anticlockwise()


    cyberpi.display.show_label("Shake:{}".format(shake),16,0,0,0)
    cyberpi.display.show_label("Wave UP:{}".format(wave_up),16,0,15,1)
    cyberpi.display.show_label("Wave Down:{}".format(wave_down),16,0,30,2)
    cyberpi.display.show_label("Left:{}".format(wave_left),16,0,45,3)
    cyberpi.display.show_label("Right:{}".format(wave_right),16,0,60,4)
    cyberpi.display.show_label("Free Fall:{}".format(free_fall),16,0,75,5)
    cyberpi.display.show_label("ClockWise:{}".format(cw),16,0,90,6)
    cyberpi.display.show_label("CClockWise:{}".format(ccw),16,0,105,7)


