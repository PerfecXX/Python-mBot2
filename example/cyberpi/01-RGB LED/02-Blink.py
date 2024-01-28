import cyberpi
from time import sleep

while True:
    #               R  G B Position
    cyberpi.led.on(255,0,0,id=1)
    cyberpi.led.on(255,255,0,id=2)
    cyberpi.led.on(255,255,255,id=3)
    cyberpi.led.on(0,255,0,id=4)
    cyberpi.led.on(0,255,255,id=5)
    sleep(1)
    #               Position 
    cyberpi.led.off(id='all')
    sleep(1)
