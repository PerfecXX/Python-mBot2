import cyberpi

cyberpi.display.show_label("YAW PITCH ROLL\nA:Start",16,0,0,0)

while not cyberpi.controller.is_press('a'):
    pass
while True:
    pitch = cyberpi.get_pitch()
    roll = cyberpi.get_roll()
    yaw = cyberpi.get_yaw()

    cyberpi.display.show_label("Yaw\n\nPitch\n\nRoll\n\n",16,0,0,0)
    cyberpi.display.show_label("{}\n\n{}\n\n{}".format(pitch,roll,yaw),16,50,0,1)
