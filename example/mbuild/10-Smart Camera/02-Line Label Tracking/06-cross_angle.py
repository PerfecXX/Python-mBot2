import cyberpi, mbuild

mbuild.smart_camera.set_mode("line", 1)
mbuild.smart_camera.set_line('black', 1)

while True:
    cross_road = mbuild.smart_camera.get_cross_road(1)
    cross_angle = mbuild.smart_camera.get_cross_angle(1, 1)

    cyberpi.display.show_label(cross_road, 12, 0, 0, index=0)
    cyberpi.display.show_label(cross_angle, 12, 0, 20, index=1)
