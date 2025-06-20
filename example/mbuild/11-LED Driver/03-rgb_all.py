import time, cyberpi, mbuild

mbuild.led_strip.set_all(255, 0, 0, 1)
time.sleep(1)
mbuild.led_strip.set_all(0, 0, 0, 1)
time.sleep(1)
