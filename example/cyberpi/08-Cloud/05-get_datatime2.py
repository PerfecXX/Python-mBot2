import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"
auth_key = "replace_with_mBlock5_cloud_auth_code"
time_zone = "UTC+7" # Bangkok Time Zone
cyberpi.led.on(255,0,0,id='all')
cyberpi.display.show_label("WiFi:",12,0,0,0)

if not cyberpi.wifi.is_connect():
    cyberpi.display.show_label("WiFi: No Connect",12,0,0,0)
    cyberpi.wifi.connect(ssid,pwd)
    while not cyberpi.wifi.is_connect():
        cyberpi.display.show_label("Connecting..",12,0,20,1)

cyberpi.display.clear()
cyberpi.display.show_label("Status: Connected!",12,0,0,0)
cyberpi.led.on(0,255,0,id='all')


cyberpi.cloud.setkey(auth_key)

time_data = cyberpi.cloud.time_data(time_zone)
date = time_data[0]
day_name = time_data[1]
time = time_data[2]

cyberpi.display.show_label("Date: {}".format(date),12,0,20,1)
cyberpi.display.show_label("DayName: {}".format(day_name),12,0,32,2)
cyberpi.display.show_label("Time: {}".format(time),12,0,46,3)
