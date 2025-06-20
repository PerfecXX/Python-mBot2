import cyberpi, mbuild, time 
from random import randint

while True:
  
    angle = randint(0,180)
  
    mbuild.servo_driver.set_angle(angle, 1)
  
    cyberpi.display.show_label(angle, 16, 50, 0, index = 1)
    time.sleep(1)
