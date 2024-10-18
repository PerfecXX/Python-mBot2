import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"

cyberpi.led.on(255,0,0,id='all')
if not cyberpi.wifi.is_connect():
    cyberpi.wifi.connect(ssid,pwd)
    while not cyberpi.wifi.is_connect():
        pass

cyberpi.led.on(0,255,0,id='all')
