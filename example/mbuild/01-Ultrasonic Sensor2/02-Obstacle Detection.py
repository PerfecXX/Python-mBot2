import cyberpi,mbuild

cyberpi.display.show_label("Range:", 16, 20, 0, index = 0)

while True:
    range = mbuild.ultrasonic2.get(index = 1)
    cyberpi.display.show_label(range, 16, 70, 0, index = 1)
    
    if range < 10:
        cyberpi.led.on(255,0,0,id="all")
        cyberpi.display.show_label("Obstacle!", 16, 0, 20, index = 2)
    else:
        cyberpi.led.on(0,255,0,id="all")
        cyberpi.display.show_label("No Obstacle", 16, 0, 20, index = 2)
