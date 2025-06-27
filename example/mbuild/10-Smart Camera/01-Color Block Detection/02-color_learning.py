import cyberpi, mbuild

mbuild.smart_camera.set_mode("color", 1)
mbuild.smart_camera.open_light(1)
mbuild.smart_camera.learn(1, "until_button", 1)

while True:
    
    if mbuild.smart_camera.detect_sign(1, 1):
        cyberpi.led.on(208, 2, 27, "all")

    else:
        cyberpi.led.off("all")
