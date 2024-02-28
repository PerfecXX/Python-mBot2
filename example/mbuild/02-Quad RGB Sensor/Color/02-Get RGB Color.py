import cyberpi,mbuild

cyberpi.display.show_label("  L2 L1 R1 R2\nR:\nG:\nB:", 16, 0, 0, index = 0)

while True:
    
    l2_r = mbuild.quad_rgb_sensor.get_red("L2")
    l2_g = mbuild.quad_rgb_sensor.get_green("L2")
    l2_b = mbuild.quad_rgb_sensor.get_blue("L2")
    
    l1_r = mbuild.quad_rgb_sensor.get_red("L1")
    l1_g = mbuild.quad_rgb_sensor.get_green("L1")
    l1_b = mbuild.quad_rgb_sensor.get_blue("L1")
    
    r1_r = mbuild.quad_rgb_sensor.get_red("R1")
    r1_g = mbuild.quad_rgb_sensor.get_green("R1")
    r1_b = mbuild.quad_rgb_sensor.get_blue("R1")
    
    r2_r = mbuild.quad_rgb_sensor.get_red("R2")
    r2_g = mbuild.quad_rgb_sensor.get_green("R2")
    r2_b = mbuild.quad_rgb_sensor.get_blue("R2")
    

    cyberpi.display.show_label("%d %d %d %d"%(l2_r,l1_r,r1_r,r2_r), 12, 18, 18, index = 1)
    cyberpi.display.show_label("%d %d %d %d"%(l2_g,l1_g,r1_g,r2_g), 12, 18, 36, index = 2)
    cyberpi.display.show_label("%d %d %d %d"%(l2_b,l1_b,r1_b,r2_b), 12, 18, 54, index = 3)
