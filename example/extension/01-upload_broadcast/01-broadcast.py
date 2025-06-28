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

cyberpi.upload_broadcast.set(topic, message)
