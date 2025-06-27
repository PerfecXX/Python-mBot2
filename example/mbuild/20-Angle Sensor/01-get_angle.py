import cyberpi, mbuild

mbuild.angle_sensor.set_report_mode(2, 100, 1)
mbuild.angle_sensor.reset_angle(1)

while True:
    
    angle = mbuild.angle_sensor.get_angle(1)
    angle_speed = mbuild.angle_sensor.get_angle_speed(1)
    
    cyberpi.display.show_label(angle, 12, 0, 0, index = 0)
    cyberpi.display.show_label(angle_speed, 12, 0, 0, index = 1)
    
    if mbuild.angle_sensor.is_rotating_clockwise(1):
        cyberpi.led.on(208, 2, 27, "all")

    if mbuild.angle_sensor.is_rotating_anticlockwise(1):
        cyberpi.led.on(1, 208, 56, "all")
