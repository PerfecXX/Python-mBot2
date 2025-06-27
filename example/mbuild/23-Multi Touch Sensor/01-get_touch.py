import cyberpi, mbuild
#                              sensitivity (1=Low,2=medium, 4=high)
mbuild.multi_touch.set_sensitivity(1, 1)

while True:
    #                     point (1-8), index 
    if mbuild.multi_touch.is_active(1, 1):
        cyberpi.led.on(208, 2, 27, "all")
    if mbuild.multi_touch.is_active(2, 1):
        cyberpi.led.on(1, 255, 35, "all")
    if mbuild.multi_touch.is_active(3, 1):
        cyberpi.led.on(1, 10, 255, "all")
