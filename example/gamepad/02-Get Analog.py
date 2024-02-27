import cyberpi,gamepad

while True:
    lx = gamepad.get_joystick('Lx')
    ly = gamepad.get_joystick('Ly')
    rx = gamepad.get_joystick('Rx')
    ry = gamepad.get_joystick('Ry')
    cyberpi.display.show_label("LX:\nLY:\nRX:\nRY:",16,0,0,index=0)
    cyberpi.display.show_label(lx,16,30,0,index=1)
    cyberpi.display.show_label(ly,16,30,15,index=2)
    cyberpi.display.show_label(rx,16,30,35,index=3)
    cyberpi.display.show_label(ry,16,30,55,index=4)
