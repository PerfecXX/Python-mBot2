import cyberpi,mbuild

cyberpi.display.show_label("L2:\nL1:\nR1:\nR2:", 16, 0, 0, index = 0)

while True:
    
    l2 = mbuild.quad_rgb_sensor.get_color("L2")
    l1 = mbuild.quad_rgb_sensor.get_color("L1")
    r1 = mbuild.quad_rgb_sensor.get_color("R1")
    r2 = mbuild.quad_rgb_sensor.get_color("R2")
    
    cyberpi.display.show_label(l2, 16, 36, 0, index = 1)
    cyberpi.display.show_label(l1, 16, 36, 18, index = 2)
    cyberpi.display.show_label(r1, 16, 36, 36, index = 3)
    cyberpi.display.show_label(r2, 16, 36, 54, index = 4)
