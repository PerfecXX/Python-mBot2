import cyberpi, mbuild
cyberpi.display.show_label("Soil:", 16, 0, 0, index = 0)

while True:
    humidity = mbuild.soil_moisture.get_humidity(1)
    cyberpi.display.show_label(humidity, 16, 50, 0, index = 1)

