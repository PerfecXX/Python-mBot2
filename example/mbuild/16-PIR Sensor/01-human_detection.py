import cyberpi, mbuild

while True:
  
    count = mbuild.pir_sensor.get_count(1)
  
    cyberpi.display.show_label(count, 12,0,0,index = 0)
  
    if mbuild.pir_sensor.is_activated(1):
        cyberpi.led.on(208, 2, 27, "all")
    else:
        cyberpi.led.off("all")
        mbuild.pir_sensor.reset_count(1)

