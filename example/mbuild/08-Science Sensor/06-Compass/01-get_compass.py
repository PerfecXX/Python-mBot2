import cyberpi, mbuild

while True:
  
    compass_angle = mbuild.science.compass_get_angle(1)
   
    cyberpi.display.show_label("Angle:{} deg".format(compass_angle), 12, 0, 0, index = 0)
