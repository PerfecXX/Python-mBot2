import cyberpi, mbuild

while:
    
    light = mbuild.light_sensor.get_value(1)
    
    cyberpi.display.show_label(light, 12, 0,0, index = 1)
