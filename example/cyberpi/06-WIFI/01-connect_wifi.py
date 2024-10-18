import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"

cyberpi.led.on(255,0,0,id='all')
cyberpi.display.show_label("Status:",12,0,0,0)

if not cyberpi.wifi.is_connect():
    cyberpi.display.show_label("Status: No Connect",12,0,0,0)
    cyberpi.wifi.connect(ssid,pwd)
    while not cyberpi.wifi.is_connect():
        cyberpi.display.show_label("Connecting..",12,0,20,1)

cyberpi.display.clear()
cyberpi.display.show_label("Status: Connected!",12,0,0,0)
cyberpi.led.on(0,255,0,id='all')
