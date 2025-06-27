import cyberpi, mbuild

while True:
    
    loudness = mbuild.sound_sensor.get_loudness(1)
    
    cyberpi.display.show_label(loudness, 12, 0, 0, index = 0)
