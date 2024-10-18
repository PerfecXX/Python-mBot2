import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"
topic = "/test_room"

cyberpi.led.on(255,0,0,id='all')
cyberpi.display.show_label("WiFi:",12,0,0,0)

if not cyberpi.wifi.is_connect():
    cyberpi.display.show_label("WiFi: No Connect",12,0,0,0)
    cyberpi.wifi.connect(ssid,pwd)
    while not cyberpi.wifi.is_connect():
        cyberpi.display.show_label("Connecting..",12,0,20,1)

cyberpi.display.clear()
cyberpi.display.show_label("WiFi: Connected!\nA/B:Send Message",12,0,0,0)
cyberpi.led.on(0,255,0,id='all')

while True:
    if cyberpi.controller.is_press('a'):
        cyberpi.wifi_broadcast.set(topic,"Hello from CyberPi2")
    elif cyberpi.controller.is_press('b'):
        cyberpi.wifi_broadcast.set(topic,"Test message!")
    
