import cyberpi

while True:
    
    current_vol = cyberpi.audio.get_vol()
    cyberpi.display.show_label("UP:Increase\nDown:Decrease\nMiddle:Test\nCurrent Volume",16,0,0,0)
    cyberpi.display.show_label("{}%".format(current_vol),24,40,80,1)
    
    if cyberpi.controller.is_press('up'):
        cyberpi.audio.add_vol(1)
    elif cyberpi.controller.is_press('down'):
        cyberpi.audio.add_vol(-1)
    
    elif cyberpi.controller.is_press('middle'):
        cyberpi.audio.play_until("hello")
