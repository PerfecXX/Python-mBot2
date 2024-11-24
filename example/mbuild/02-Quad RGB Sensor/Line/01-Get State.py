import cyberpi,mbuild

cyberpi.display.show_label("LINE:\nBG:", 16, 0, 0, index = 0)

while True:
  
    line_state = mbuild.quad_rgb_sensor.get_line_sta("all", 1)
    bg_state = mbuild.quad_rgb_sensor.get_ground_sta("all", 1)
  
    cyberpi.display.show_label(line_state, 16, 50, 0, index = 1)
    cyberpi.display.show_label(bg_state, 16, 50, 15, index = 2)
