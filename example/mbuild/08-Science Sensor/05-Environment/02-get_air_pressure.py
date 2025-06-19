import cyberpi, mbuild

while True:
    
    air_pressure = mbuild.science.atmos_get(1)
    
    cyberpi.display.show_label("AirPressure:{} Pa".format(air_pressure), 12, 0, 0, index = 0)
