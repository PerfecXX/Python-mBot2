import cyberpi

cyberpi.timer.reset()

while True:
    current_timer = cyberpi.timer.get()
    cyberpi.display.show_label(current_timer, 12, int(0), int(0), index = 0)
