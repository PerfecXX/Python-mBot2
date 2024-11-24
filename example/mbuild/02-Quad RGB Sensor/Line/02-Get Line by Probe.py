import cyberpi,mbuild

cyberpi.display.show_label("RGB PROBE STATE\nL2:\nL1:\nR1:\nR2:\n", 16, 0, 0, index = 0)

while True:
    l2_line_state = mbuild.quad_rgb_sensor.is_line("L2",1)
    l1_line_state = mbuild.quad_rgb_sensor.is_line("L1",1)
    r1_line_state = mbuild.quad_rgb_sensor.is_line("R1",1)
    r2_line_state = mbuild.quad_rgb_sensor.is_line("R2",1)

    cyberpi.display.show_label(l2_line_state, 16, 30, 18, index = 1)
    cyberpi.display.show_label(l1_line_state, 16, 30, 36, index = 2)
    cyberpi.display.show_label(r1_line_state, 16, 30, 54, index = 3)
    cyberpi.display.show_label(r2_line_state, 16, 30, 72, index = 4)


    
