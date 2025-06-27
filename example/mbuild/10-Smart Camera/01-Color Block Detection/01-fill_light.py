import cyberpi, mbuild

mbuild.smart_camera.set_mode("color", 1)

while True:
  
    if cyberpi.controller.is_press('a'):
        mbuild.smart_camera.open_light(1)

    if cyberpi.controller.is_press('b'):
        mbuild.smart_camera.close_light(1)
