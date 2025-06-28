import cyberpi, mbot2, time

#     index = 1 to 32 or all ,port = all,S1 or S2
mbot2.led_on(255, 0, 0, 1, "S1")
time.sleep(3)
mbot2.led_on(0, 255, 0, "all", "S2")
time.sleep(3)
mbot2.led_off("all", "S1")
mbot2.led_off("all", "S2")
