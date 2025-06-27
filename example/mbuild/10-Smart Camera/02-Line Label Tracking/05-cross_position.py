import cyberpi, mbuild

mbuild.smart_camera.set_mode("line", 1)
mbuild.smart_camera.set_line('black', 1)

while True:
    x_cross = mbuild.smart_camera.get_cross_x(1)
    y_cross = mbuild.smart_camera.get_cross_y(1)

    cyberpi.display.show_label(x_cross, 12, 0, 0, index=0)
    cyberpi.display.show_label(y_cross, 12, 0, 20, index=1)
