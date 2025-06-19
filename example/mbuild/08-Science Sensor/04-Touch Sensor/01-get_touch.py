import cyberpi, mbuild

while True:
    touch_kohm = mbuild.science.touch_get_resistance(1)
    cyberpi.display.show_label("Touch Value:{}".format(touch_kohm), 12, int(0), int(0), index = 0)
    if mbuild.science.touch_is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
