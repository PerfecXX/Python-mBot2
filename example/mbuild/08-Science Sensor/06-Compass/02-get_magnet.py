import cyberpi, mbuild

while True:
    
    magnet_x = mbuild.science.compass_get('x',1)
    magnet_y = mbuild.science.compass_get('y',1)
    magnet_z = mbuild.science.compass_get('z',1)
   
    cyberpi.display.show_label("X:{}".format(magnet_x), 12, 0, 0, index = 0)
    cyberpi.display.show_label("Y:{}".format(magnet_y), 12, 0, 12, index = 1)
    cyberpi.display.show_label("Z:{}".format(magnet_z), 12, 0, 24, index = 2)
    
    if mbuild.science.compass_is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
