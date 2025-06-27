import cyberpi, mbuild

while True:
    
    temp_cel = mbuild.temp_sensor.get_temperature("celsius", 1)
    temp_fah = mbuild.temp_sensor.get_temperature("fahrenheit", 1)
    
    cyberpi.display.show_label(temp_cel, 12, 0, 0, index = 0)
    cyberpi.display.show_label(temp_fah, 12, 0, 0, index = 1)


