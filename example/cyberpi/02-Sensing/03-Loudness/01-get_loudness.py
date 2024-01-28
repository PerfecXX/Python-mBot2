import cyberpi

cyberpi.display.show_label("Loudness:",16,10,10,index=1)

while True:
    loudness_value = cyberpi.get_loudness()
    cyberpi.display.show_label(loudness_value,16,80,10,index=2)
