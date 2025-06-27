import cyberpi, mbuild

mbuild.smart_camera.set_mode("color", 1)
mbuild.smart_camera.open_light(1)
mbuild.smart_camera.learn(1, "until_button", 1)

while True:
    x = mbuild.smart_camera.get_sign_x(1, 1)
    y = mbuild.smart_camera.get_sign_y(1, 1)
    height = mbuild.smart_camera.get_sign_hight(1, 1)
    width = mbuild.smart_camera.get_sign_wide(1, 1)

    cyberpi.display.show_label("x: {}".format(x), 12, 0, 0, index=0)
    cyberpi.display.show_label("y: {}".format(y), 12, 0, 20, index=1)
    cyberpi.display.show_label("height: {}".format(height), 12, 0, 40, index=2)
    cyberpi.display.show_label("width: {}".format(width), 12, 0, 60, index=3)
