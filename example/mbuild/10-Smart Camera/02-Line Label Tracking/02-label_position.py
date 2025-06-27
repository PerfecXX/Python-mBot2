import cyberpi, mbuild

mbuild.smart_camera.set_mode("line", 1)
mbuild.smart_camera.set_line('black', 1)

while True:
    
    x1 = mbuild.smart_camera.get_label_x(1, 1)
    y1 = mbuild.smart_camera.get_label_y(1, 1)

    cyberpi.display.show_label("X: {}".format(x1), 12, 0, 0, index=0)
    cyberpi.display.show_label("Y: {}".format(y1), 12, 0, 20, index=1)
