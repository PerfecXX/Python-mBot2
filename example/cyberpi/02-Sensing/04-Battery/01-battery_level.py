import cyberpi

cyberpi.display.show_label("Battery Level",16,10,0,index=0)
cyberpi.display.show_label("Builtin:",16,10,20,index=1)
cyberpi.display.show_label("Extra:",16,10,40,index=2)

while True:
    builtin_batt = cyberpi.get_battery()
    extra_batt = cyberpi.get_extra_battery()
    
    cyberpi.display.show_label(builtin_batt,16,80,20,index=3)
    cyberpi.display.show_label(extra_batt,16,80,40,index=4)
