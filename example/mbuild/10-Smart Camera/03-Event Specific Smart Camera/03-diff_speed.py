import cyberpi, mbuild

mbuild.smart_camera.set_kp(0.5, 1)

while True:
    sign_speed = mbuild.smart_camera.get_sign_diff_speed(1, 'x', 100, 1)
    label_speed = mbuild.smart_camera.get_label_diff_speed(1, 'x', 100, 1)
    vector_speed = mbuild.smart_camera.get_follow_vector_diff_speed(1)

    cyberpi.display.show_label("Sign Speed: {}".format(sign_speed), 12, 0, 0, index=0)
    cyberpi.display.show_label("Label Speed: {}".format(label_speed), 12, 0, 20, index=1)
    cyberpi.display.show_label("Vector Speed: {}".format(vector_speed), 12, 0, 40, index=2)
