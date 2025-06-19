import cyberpi, mbuild

while True:
    if mbuild.science.pir_is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
