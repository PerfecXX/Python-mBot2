import cyberpi, mbuild

while True:
    
    soil_moiture = mbuild.science.soil_get(1)
    soil_kohm = mbuild.science.soil_get_resistance(1)
    
    cyberpi.display.show_label("SoilMoiture:{}".format(soil_moiture), 12, 0, 0, index = 0)
    cyberpi.display.show_label("SoilRes:{}".format(soil_kohm), 12, 0, 16, index = 1)
    
    if mbuild.science.soil_is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
