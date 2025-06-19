import cyberpi, mbuild

while True:
    
    altitude = mbuild.science.atmos_get_altitude(1)
    
    cyberpi.display.show_label("Altitude:{} m".format(altitude), 12, 0, 0, index = 0)
