import cyberpi,mbuild

cyberpi.display.show_label("L2:\nL1:\nR1:\nR2:", 16, 0, 0, index = 0)

while True:
    
    l2_color = mbuild.quad_rgb_sensor.get_color_sta("L2")
    l1_color = mbuild.quad_rgb_sensor.get_color_sta("L1")
    r1_color = mbuild.quad_rgb_sensor.get_color_sta("R1")
    r2_color = mbuild.quad_rgb_sensor.get_color_sta("R2")
    
    cyberpi.display.show_label(l2_color, 16, 36, 0, index = 1)
    cyberpi.display.show_label(l1_color, 16, 36, 18, index = 2)
    cyberpi.display.show_label(r1_color, 16, 36, 36, index = 3)
    cyberpi.display.show_label(r2_color, 16, 36, 54, index = 4)
