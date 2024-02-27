import cyberpi,mbuild

cyberpi.display.show_label("Range:", 16, 0, 0, index = 0)

while True:
    range = mbuild.ultrasonic2.get(index = 1)
    cyberpi.display.show_label(range, 16, 50, 0, index = 1)
