import cyberpi

cyberpi.display.show_label("Light:",16,10,10,index=1)

while True:
    light_value = cyberpi.get_brightness()
    cyberpi.display.show_label(light_value,16,60,10,index=2)
