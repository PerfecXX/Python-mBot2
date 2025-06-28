import cyberpi, mbot2

while True:
  
    if mbot2.read_digital("S1"):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
