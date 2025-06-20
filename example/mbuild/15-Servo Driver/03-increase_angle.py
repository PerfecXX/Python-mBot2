import cyberpi, mbuild, time 

mbuild.servo_driver.set_angle(0, 1)
time.sleep(1)
mbuild.servo_driver.change_angle(20, 1)
time.sleep(1)
mbuild.servo_driver.change_angle(70, 1)
time.sleep(1)
mbuild.servo_driver.set_angle(0, 1)
