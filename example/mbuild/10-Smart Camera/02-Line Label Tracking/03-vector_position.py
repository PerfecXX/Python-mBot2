import cyberpi, mbuild

mbuild.smart_camera.set_mode("line", 1)
mbuild.smart_camera.set_line('black', 1)

while True:
    #                                  replace 1 with your label id
    x_start = mbuild.smart_camera.get_vector_start_x(1)
    y_start = mbuild.smart_camera.get_vector_start_y(1)
    x_end = mbuild.smart_camera.get_vector_end_x(1)
    y_end = mbuild.smart_camera.get_vector_end_y(1)

    cyberpi.display.show_label("X Start: {}".format(x_start), 12, 0, 0, index=0)
    cyberpi.display.show_label("Y Start: {}".format(y_start), 12, 0, 20, index=1)
    cyberpi.display.show_label("X End: {}".format(x_end), 12, 0, 40, index=2)
    cyberpi.display.show_label("Y End: {}".format(y_end), 12, 0, 60, index=3)
