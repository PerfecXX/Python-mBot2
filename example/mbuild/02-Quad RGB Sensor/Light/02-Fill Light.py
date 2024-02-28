import cyberpi
import mbuild

color = ["black", "red", "yellow", "green", "cyan", "blue", "purple", "white"]
num_color = len(color)
cursor = 0

cyberpi.display.show_label("Up/Down:Turn On\nMiddle: Reset\n\nColor:", 16, 0, 0, index=0)

while True:
    if cyberpi.controller.is_press('up'):
        cursor = (cursor + 1) % num_color
    if cyberpi.controller.is_press('down'):
        cursor = (cursor - 1) % num_color
    
    if cyberpi.controller.is_press('middle'):
        cursor = 0
    
    if cursor < 0:
        cursor = num_color - 1

    current_color = color[cursor]
    cyberpi.display.show_label(current_color, 16, 50, 54, index=1)
    mbuild.quad_rgb_sensor.set_led(color=current_color)
