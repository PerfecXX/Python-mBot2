import cyberpi

cyberpi.display.show_label("Wave Value\nA:Start",16,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass

while True:
    wave_angle = cyberpi.get_wave_angle()
    wave_speed = cyberpi.get_wave_speed()

    cyberpi.display.show_label("Wave Angle",16,20,0,0)
    cyberpi.display.show_label("{}".format(wave_angle),24,40,30,1)
    cyberpi.display.show_label("Wave Speed",16,20,60,2)
    cyberpi.display.show_label("{}".format(wave_speed),24,40,80,3)

