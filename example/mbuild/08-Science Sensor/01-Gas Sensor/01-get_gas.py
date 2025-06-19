import cyberpi, mbuild

# Set sensitivity (0.1 to 1.0)
mbuild.science.mq2_on(0.5,1)

while True:
  
    gas_val = mbuild.science.mq2_get(1)
    cyberpi.display.show_label("Gas Value: {}".format(gas_val), 12, int(0), int(0), index = 0)
    
    if mbuild.science.mq2_is_active(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
