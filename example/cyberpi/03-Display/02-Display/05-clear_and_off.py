import cyberpi

cyberpi.display.on()

cyberpi.display.show_label("A:Clear the Sceen",12,0,0,0)
cyberpi.display.show_label("B:Close the screen",12,0,24,1)

while True:
    if cyberpi.controller.is_press('a'):
        cyberpi.display.clear()
    elif cyberpi.controller.is_press('b'):
        cyberpi.display.off()
