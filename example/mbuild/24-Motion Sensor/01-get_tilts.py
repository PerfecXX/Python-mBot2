import cyberpi, mbuild

while True:
    
    if mbuild.motion_sensor.is_tilted_left(1):
        cyberpi.led.on(208, 2, 27, "all")
        
    if mbuild.motion_sensor.is_tilted_right(1):
        cyberpi.led.on(208, 153, 1, "all")

    if mbuild.motion_sensor.is_tilted_forward(1):
        cyberpi.led.on(255, 221, 2, "all")

    if mbuild.motion_sensor.is_tilted_backward(1):
        cyberpi.led.on(2, 255, 23, "all")

    if mbuild.motion_sensor.is_face_up(1):
        cyberpi.led.on(1, 208, 187, "all")

    if mbuild.motion_sensor.is_face_down(1):
        cyberpi.led.on(31, 2, 255, "all")

    if mbuild.motion_sensor.is_upright(1):
        cyberpi.led.on(255, 0, 208, "all")

        
