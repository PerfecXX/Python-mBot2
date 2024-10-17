import cyberpi
from time import sleep

cyberpi.audio.set_vol(100)

cyberpi.display.show_label("A:Start Recording\nB:Play Recording",12,0,0,0)

while True:
    cyberpi.display.show_label("Waiting.",16,0,40,1)
    if cyberpi.controller.is_press('a'):
        cyberpi.led.on(0,255,0,id="all")
        cyberpi.display.show_label("Listening..",16,0,40,1)
        cyberpi.audio.record()
        sleep(5)
        cyberpi.display.show_label("Finished..",16,0,40,1)
        cyberpi.audio.stop_record()

    elif cyberpi.controller.is_press('b'):
        cyberpi.led.on(0,0,255,id="all")
        cyberpi.display.show_label("Playing..",16,0,40,1)
        cyberpi.audio.play_record_until()
        cyberpi.display.show_label("Finished..",16,0,40,1)

    cyberpi.display.show_label("Waiting...",16,0,40,1)
    cyberpi.led.on(0,0,0,id="all")
    
