"""
Display basic CyberPi information.
To view each piece of information, press the 'A' (Square button).
"""
import cyberpi

while True:
    mac_addr = cyberpi.get_mac_address()
    cyberpi.console.println("MAC Address")
    cyberpi.console.println(mac_addr)
    
    while not cyberpi.controller.is_press('A'):
        pass
    
    cyberpi.console.clear()
    
    firmware_ver = cyberpi.get_firmware_version()
    cyberpi.console.println("Firmware Ver")
    cyberpi.console.println(firmware_ver)
    
    while not cyberpi.controller.is_press('A'):
        pass
    
    cyberpi.console.clear()
    
    ble_name = cyberpi.get_ble()
    cyberpi.console.println("BLE Name")
    cyberpi.console.println(ble_name)
    
    while not cyberpi.controller.is_press('A'):
        pass
    
    cyberpi.console.clear()
    
    cyberpi_name = cyberpi.get_name()
    cyberpi.console.println("Board Name")
    cyberpi.console.println(cyberpi_name)
    
    while not cyberpi.controller.is_press('A'):
        pass
    
    cyberpi.console.clear()
    
    sys_lang = cyberpi.get_language()
    cyberpi.console.println("Language")
    cyberpi.console.println(sys_lang)
    
    while not cyberpi.controller.is_press('A'):
        pass
    
    cyberpi.console.clear()
    
