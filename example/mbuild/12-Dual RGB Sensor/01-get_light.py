import cyberpi, mbuild

while True:
  
  probe1_light = mbuild.dual_rgb_sensor.get_intensity('RGB1', 1)
  probe2_light = mbuild.dual_rgb_sensor.get_intensity('RGB2', 1)
  
  cyberpi.display.show_label("Probe1: {}"format(probe1_light), 12, 0, 0, index = 0)
  cyberpi.display.show_label("Probe2: {}"format(probe2_light), 12, 0, 16, index = 1)
