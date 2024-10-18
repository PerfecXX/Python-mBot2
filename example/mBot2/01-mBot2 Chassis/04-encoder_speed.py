import cyberpi, mbot2
from time import sleep

cyberpi.display.show_label("mBot2 EM Speed",16,0,0,0)
cyberpi.display.show_label("A:Start Moving!",16,0,20,1)

while not cyberpi.controller.is_press('a'):
        pass
#                 EM1  EM2
mbot2.drive_speed(60, -60)
sleep(1)
mbot2.drive_speed(0,0)

#                 EM1  EM2
mbot2.drive_speed(-60, 60)
sleep(1)
mbot2.drive_speed(0,0)

#                 EM1  EM2
mbot2.drive_speed(-60, -60)
sleep(1)
mbot2.drive_speed(0,0)

#                 EM1  EM2
mbot2.drive_speed(60, 60)
sleep(1)
mbot2.drive_speed(0,0)
        
