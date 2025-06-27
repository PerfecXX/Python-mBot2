import cyberpi, mbuild

mbuild.smart_camera.set_mode("line", 1)
#                            black or white
mbuild.smart_camera.set_line('black', 1)

while True:
    
    if mbuild.smart_camera.detect_label(1, 1):
        cyberpi.display.show_label("({}) {}".format(1, "Forward"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(2, 1):
        cyberpi.display.show_label("({}) {}".format(2, "Backward"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(3, 1):
        cyberpi.display.show_label("({}) {}".format(3, "Turn Left"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(4, 1):
        cyberpi.display.show_label("({}) {}".format(4, "Turn Right"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(5, 1):
        cyberpi.display.show_label("({}) {}".format(5, "Stop"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(6, 1):
        cyberpi.display.show_label("({}) {}".format(6, "Plus"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(7, 1):
        cyberpi.display.show_label("({}) {}".format(7, "Minus"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(8, 1):
        cyberpi.display.show_label("({}) {}".format(8, "Question Mark"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(9, 1):
        cyberpi.display.show_label("({}) {}".format(9, "Heart"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(10, 1):
        cyberpi.display.show_label("({}) {}".format(10, "A"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(11, 1):
        cyberpi.display.show_label("({}) {}".format(11, "B"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(12, 1):
        cyberpi.display.show_label("({}) {}".format(12, "C"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(13, 1):
        cyberpi.display.show_label("({}) {}".format(13, "1"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(14, 1):
        cyberpi.display.show_label("({}) {}".format(14, "2"), 12, 0, 0, index=0)
    elif mbuild.smart_camera.detect_label(15, 1):
        cyberpi.display.show_label("({}) {}".format(15, "3"), 12, 0, 0, index=0)
    else:
        cyberpi.display.clear()
