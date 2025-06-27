import cyberpi, mbuild

mbuild.smart_camera.set_mode("color", 1)
mbuild.smart_camera.open_light(1)
mbuild.smart_camera.learn(1, "until_button", 1)

while True:
    if mbuild.smart_camera.detect_sign_location(1, 'middle', 1):
        cyberpi.display.show_label("Center", 12, 30, 30, index=0)
    elif mbuild.smart_camera.detect_sign_location(1, 'up', 1):
        cyberpi.display.show_label("Upper", 12, 30, 30, index=0)
    elif mbuild.smart_camera.detect_sign_location(1, 'down', 1):
        cyberpi.display.show_label("Bottom", 12, 30, 30, index=0)
    elif mbuild.smart_camera.detect_sign_location(1, 'left', 1):
        cyberpi.display.show_label("Left", 12, 30, 30, index=0)
    elif mbuild.smart_camera.detect_sign_location(1, 'right', 1):
        cyberpi.display.show_label("Right", 12, 30, 30, index=0)
    else:
        cyberpi.display.show_label("Not Found", 12, 30, 30, index=0)
