import cyberpi, mbuild

# Set Color           r   g  b index
mbuild.rgb_led.show(239, 22, 37, 1)
# Close           index
mbuild.rgb_led.off(1)

# Get Color          index
red = mbuild.rgb_led.get_red(1)
green = mbuild.rgb_led.get_green(1)
blue = mbuild.rgb_led.get_blue(1)

cyberpi.display.show_label(red, 12, 0, 0, index = 0)
cyberpi.display.show_label(green, 12, 0, 20, index = 1)
cyberpi.display.show_label(blue, 12, 0, 40, index = 2)


