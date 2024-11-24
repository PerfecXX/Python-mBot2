import cyberpi, mbuild
cyberpi.display.show_label("Slider Value ", 16, 0, 0, index = 0)

while True:
    slider_val = mbuild.slider.get_value(1)
    cyberpi.display.show_label(slider_val, 16, 100, 0, index = 1)

