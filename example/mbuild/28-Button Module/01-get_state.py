import cyberpi, mbuild

mbuild.button.reset_count(1)
while True:
    
    counter = mbuild.button.get_count(1)
    cyberpi.display.show_label(counter, 12, 0, 0, index = 0)
    
    if mbuild.button.is_pressed(1):
        cyberpi.led.on(208, 2, 27, "all")
    
    else:
        cyberpi.led.off("all")
