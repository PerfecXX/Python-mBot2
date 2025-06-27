import cyberpi, mbuild

while True:
    
    if mbuild.mq2_gas_sensor.is_active('low', 1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
