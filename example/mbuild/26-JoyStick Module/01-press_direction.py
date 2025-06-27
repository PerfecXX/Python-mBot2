import cyberpi, mbuild

while:
    
    if mbuild.joystick.is_active('up', 1):
        cyberpi.led.on(208, 2, 27, "all")
        
    if mbuild.joystick.is_active('down', 1):
        cyberpi.led.on(255, 221, 0, "all")

    if mbuild.joystick.is_active('left', 1):
        cyberpi.led.on(2, 255, 10, "all")
        
    if mbuild.joystick.is_active('right', 1):
        cyberpi.led.on(29, 0, 255, "all")
