import cyberpi, mbuild

mbuild.led_panel.show("Hello", wait = True, index = 1)
mbuild.led_panel.clear(1)
mbuild.led_panel.show("World!", wait = True, index = 1)
