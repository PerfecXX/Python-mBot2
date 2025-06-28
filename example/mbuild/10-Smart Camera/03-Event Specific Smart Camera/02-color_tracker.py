import cyberpi, mbuild

mbuild.smart_camera.set_kp(0.5, 1)

while True:
  
    if mbuild.smart_camera.is_lock_sign(1, 'x', 100, 1)
        cyberpi.led.on(208, 2, 27, "all")

    if mbuild.smart_camera.is_lock_sign(1, 'y', 72, 1)
        cyberpi.led.on(255, 0, 135, "all")
