import cyberpi,mbuild

cyberpi.display.show_label("Range:", 16, 0, 0, index = 0)

while True:
    distance = mbuild.ranging_sensor.get_distance(1)
    cyberpi.display.show_label(distance, 16, 50, 0, index = 1)
