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

cyberpi.display.show_label("WiFi: Connected!\n",12,0,0,0)
cyberpi.display.show_label("Waiting Message...",12,0,20,1)
cyberpi.led.on(0,255,0,id='all')

while True:
    message = cyberpi.wifi_broadcast.get(topic)
    cyberpi.display.show_label("{}".format(message),12,0,20,1)
