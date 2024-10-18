import cyberpi, mbot2
from time import sleep

cyberpi.display.show_label("mBot2 EM Power",16,0,0,0)

while not cyberpi.controller.is_press('a'):
        pass
        
mbot2.drive_power(100, -100)
sleep(1)
mbot2.drive_power(0, 0)
