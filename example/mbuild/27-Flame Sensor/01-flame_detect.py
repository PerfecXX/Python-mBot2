import cyberpi, mbuild

while:
    
    flame_size = mbuild.flame_sensor.get_value(1)
    
    cyberpi.display.show_label(flame_size, 12, int(0), int(0), index = 0)
    
    if mbuild.flame_sensor.is_active(1):
        
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
