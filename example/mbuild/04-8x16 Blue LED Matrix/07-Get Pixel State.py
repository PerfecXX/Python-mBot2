import cyberpi, mbuild

mbuild.led_panel.set_pixel(0, 0, True, 1)
#                             x  y
if mbuild.led_panel.get_pixel(0, 0, 1):
    cyberpi.display.show_label("Pixel 0,0 is set", 12, 0, 0, index = 0)
else:
    cyberpi.display.show_label("Pixel 0,0 is not set", 12, 0, 0, index = 0)
