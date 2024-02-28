import cyberpi,mbuild

def convert_rgb(hex_color):
    # Remove the leading '0x' if present and convert the hex string to integers
    hex_color = hex_color.lstrip('0x')
    # Split the hex string into three parts representing R, G, and B values
    r_hex = hex_color[0:2]
    g_hex = hex_color[2:4]
    b_hex = hex_color[4:6]
    # Convert each part from hexadecimal to integer
    r = int(r_hex,16)
    g = int(g_hex,16)
    b = int(b_hex,16)
    # Return the RGB values as a tuple
    return (r,g,b)
    
cyberpi.display.show_label("L2:\nL1:\nR1:\nR2:", 16, 0, 0, index = 0)

while True:
    
    l2 = mbuild.quad_rgb_sensor.get_color("L2")
    l1 = mbuild.quad_rgb_sensor.get_color("L1")
    r1 = mbuild.quad_rgb_sensor.get_color("R1")
    r2 = mbuild.quad_rgb_sensor.get_color("R2")
    
    cyberpi.display.show_label(convert_rgb(l2), 12, 36, 0, index = 1)
    cyberpi.display.show_label(convert_rgb(l1), 12, 36, 18, index = 2)
    cyberpi.display.show_label(convert_rgb(r1), 12, 36, 36, index = 3)
    cyberpi.display.show_label(convert_rgb(r2), 12, 36, 54, index = 4)
