import cyberpi, mbuild

while True:
    
    if cyberpi.controller.is_press('up'):
        mbuild.dc_motor_driver.set_power(100, 1)
    
    if cyberpi.controller.is_press('down'):
        mbuild.dc_motor_driver.set_power(-100, 1)
        
    if cyberpi.controller.is_press('middle'):
        mbuild.dc_motor_driver.set_power(0, 1)
