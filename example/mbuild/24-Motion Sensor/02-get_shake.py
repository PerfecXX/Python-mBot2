import cyberpi, mbuild

while True:
    
    if mbuild.motion_sensor.is_shaked('light', 1):
        cyberpi.led.on(208, 2, 27, "all")

    if mbuild.motion_sensor.is_shaked('usual', 1):
        cyberpi.led.on(208, 153, 1, "all")

    if mbuild.motion_sensor.is_shaked('strong', 1):
        cyberpi.led.on(255, 221, 2, "all")  
