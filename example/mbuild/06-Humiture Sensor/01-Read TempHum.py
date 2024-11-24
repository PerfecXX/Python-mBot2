import cyberpi, mbuild
cyberpi.display.show_label("Humiture Sensor\nTemp(C):\nTemp(F):\nHum(%)", 16, 0, 0, index = 0)

while True:
    temp_c = mbuild.humiture_sensor.get_temperature("celsius", 1)
    temp_f = mbuild.humiture_sensor.get_temperature("fahrenheit", 1)
    humidity = mbuild.humiture_sensor.get_relative_humidity(1)

    cyberpi.display.show_label(temp_c, 16, 70, 18, index = 1)
    cyberpi.display.show_label(temp_f, 16, 70, 36, index = 2)
    cyberpi.display.show_label(humidity, 16, 70, 54, index = 3)

