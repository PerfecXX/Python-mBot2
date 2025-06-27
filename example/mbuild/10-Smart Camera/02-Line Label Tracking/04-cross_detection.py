import cyberpi, mbuild

mbuild.smart_camera.set_mode("line", 1)
mbuild.smart_camera.set_line('black', 1)

while True:
  
    if mbuild.smart_camera.detect_cross(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
