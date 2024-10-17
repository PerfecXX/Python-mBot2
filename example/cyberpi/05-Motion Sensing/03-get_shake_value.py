import cyberpi

cyberpi.display.show_label("Shake Value\nA:Start",16,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass

while True:
    shake_value = cyberpi.get_shakeval()
    cyberpi.display.show_label("Shake Value",16,20,0,0)
    cyberpi.display.show_label("{}%".format(shake_value),24,40,50,1)
