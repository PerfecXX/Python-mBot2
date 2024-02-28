import cyberpi,mbuild

cyberpi.display.show_label("A:Light On\nB:Light Off\nL2:\nL1:\nR1:\nR2:", 16, 0, 0, index = 0)

while True:
    
    l2 = mbuild.quad_rgb_sensor.get_light("L2")
    l1 = mbuild.quad_rgb_sensor.get_light("L1")
    r1 = mbuild.quad_rgb_sensor.get_light("R1")
    r2 = mbuild.quad_rgb_sensor.get_light("R2")
    
    if cyberpi.controller.is_press('a'):
        mbuild.quad_rgb_sensor.set_led(color = "white")
    if cyberpi.controller.is_press('b'):
        mbuild.quad_rgb_sensor.off_led()
    
    cyberpi.display.show_label(l2, 16, 36, 36, index = 1)
    cyberpi.display.show_label(l1, 16, 36, 54, index = 2)
    cyberpi.display.show_label(r1, 16, 36, 72, index = 3)
    cyberpi.display.show_label(r2, 16, 36, 90, index = 4)
