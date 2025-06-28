import cyberpi, time

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"

topic = "example"
message = "Hello from CyberPi"

cyberpi.led.on(208, 2, 27, "all")
cyberpi.wifi.connect(ssid, pwd)

while not cyberpi.wifi.is_connect():
    pass

cyberpi.led.on(0, 255, 8, "all")
time.sleep(1)
cyberpi.led.on(0, 0, 0, "all")

@cyberpi.event.upload_broadcast(topic)
def handle_upload_broadcast():
    value = cyberpi.upload_broadcast.get(topic)
    cyberpi.display.show_label("Message: {}".format(value), 12, 0, 0, index=0)
