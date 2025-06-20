import cyberpi, mbuild

mbuild.magnetic_sensor.reset_count(1)

while True:
    
    magnet_counter = mbuild.magnetic_sensor.get_count(1)
    
    cyberpi.display.show_label("Number of Magnet: {}".format(magnet_counter), 12, 0, 0, index = 0)
    
    if mbuild.magnetic_sensor.is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
