import cyberpi, mbot2, time

mbot2.write_digital(1, "S1")
mbot2.write_digital(1, "S2")
time.sleep(3)
mbot2.write_digital(0, "all")
