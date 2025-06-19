import cyberpi, mbuild

while True:
    
    flame_val = mbuild.science.flame_get(1)
    cyberpi.display.show_label("Flame Value:{}".format(flame_val), 12, 0, 0, index = 0)
    
    if mbuild.science.flame_is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
