import cyberpi, mbuild

# Color = white, red, yellow, green, cyan, blue, purple, black

while True:
    
      if mbuild.dual_rgb_sensor.is_color('RGB1', 'red', 1):
        cyberpi.led.on(208, 2, 27, 1)
      else:
        cyberpi.led.off("all")

      if mbuild.dual_rgb_sensor.is_color('RGB2', 'red', 1):
        cyberpi.led.on(208, 2, 27, 5)

      else:
        cyberpi.led.off("all")
