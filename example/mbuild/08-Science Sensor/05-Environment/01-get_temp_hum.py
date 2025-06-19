import cyberpi, mbuild

while True:
    
    temperature = mbuild.science.humiture_get_temp(1)
    humidity = mbuild.science.humiture_get_humidity(1)
    
    cyberpi.display.show_label("Temperature:{} c".format(temperature), 12, 0, 0, index = 0)
    cyberpi.display.show_label("Humidity:{} %".format(humidity), 12, 0, 16, index = 1)
