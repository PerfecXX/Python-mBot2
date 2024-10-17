import cyberpi

cyberpi.display.show_label("Get Tilteds\nA:Start",24,0,0,0)
while not cyberpi.controller.is_press('a'):
    pass

while True:
    tilted_forward = cyberpi.is_tiltforward()
    tilted_backward = cyberpi.is_tiltback()
    tilted_left = cyberpi.is_tiltleft()
    tilted_right = cyberpi.is_tiltright()

    face_up = cyberpi.is_faceup()
    face_down = cyberpi.is_facedown()
    stand = cyberpi.is_stand()
    hand_stand = cyberpi.is_handstand()

    cyberpi.display.show_label("Forward:{}".format(tilted_forward),16,0,0,0)
    cyberpi.display.show_label("Backward:{}".format(tilted_backward),16,0,15,1)
    cyberpi.display.show_label("Left:{}".format(tilted_left),16,0,30,2)
    cyberpi.display.show_label("Right:{}".format(tilted_right),16,0,45,3)
    cyberpi.display.show_label("Face Up:{}".format(face_up),16,0,60,4)
    cyberpi.display.show_label("Face Down:{}".format(face_down),16,0,75,5)
    cyberpi.display.show_label("Stand:{}".format(stand),16,0,90,6)
    cyberpi.display.show_label("Hand Stand:{}".format(hand_stand),16,0,105,7)
