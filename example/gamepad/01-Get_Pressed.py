import cyberpi,gamepad

while True:
    cyberpi.display.show_label("Direction:\nNumpad:\nL/R:\nMiddle:\n+:\n=:",16,0,0,index=0)
    
    if gamepad.is_key_pressed('Up'):
        cyberpi.display.show_label("Up",16,90,0,index=1)
    if gamepad.is_key_pressed('Down'):
        cyberpi.display.show_label("Down",16,90,0,index=1)
    if gamepad.is_key_pressed('Left'):
        cyberpi.display.show_label("Left",16,90,0,index=1)
    if gamepad.is_key_pressed('Right'):
        cyberpi.display.show_label("Right",16,90,0,index=1)
    
    if gamepad.is_key_pressed('N1'):
        cyberpi.display.show_label("N1",16,90,15,index=2)
    if gamepad.is_key_pressed('N2'):
        cyberpi.display.show_label("N2",16,90,15,index=2)
    if gamepad.is_key_pressed('N3'):
        cyberpi.display.show_label("N3",16,90,15,index=2)
    if gamepad.is_key_pressed('N4'):
        cyberpi.display.show_label("N4",16,90,15,index=2)
    
    if gamepad.is_key_pressed('L1'):
        cyberpi.display.show_label("L1",16,90,35,index=3)
    if gamepad.is_key_pressed('L2'):
        cyberpi.display.show_label("L2",16,90,35,index=3)
    if gamepad.is_key_pressed('R1'):
        cyberpi.display.show_label("R1",16,90,35,index=3)
    if gamepad.is_key_pressed('R2'):
        cyberpi.display.show_label("R2",16,90,35,index=3)
    
    if gamepad.is_key_pressed('L_Thumb'):
        cyberpi.display.show_label("Left",16,90,55,index=4)
    if gamepad.is_key_pressed('R_Thumb'):
        cyberpi.display.show_label("Right",16,90,55,index=4)
    
    if gamepad.is_key_pressed('Start'):
        cyberpi.display.show_label("Pressed!",16,50,73,index=5)
    else:
        cyberpi.display.show_label("Not Press",16,50,73,index=5)
    if gamepad.is_key_pressed('Select'):
        cyberpi.display.show_label("Pressed!",16,50,90,index=6)
    else:
        cyberpi.display.show_label("Not Press",16,50,90,index=6)
    
