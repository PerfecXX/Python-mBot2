import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"
auth_key = "replace_with_mBlock5_cloud_auth_code"
location_id = "1609348" # Bangkok

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

sunrise_time = cyberpi.cloud.time("sunrise_time",location_id)
sunrise_hour = cyberpi.cloud.time("sunrise_hour",location_id)
sunrise_minute = cyberpi.cloud.time("sunrise_minute",location_id)
sunset_time = cyberpi.cloud.time("sunrise_set",location_id)
sunset_hour = cyberpi.cloud.time("sunset_hour",location_id)
sunset_minute = cyberpi.cloud.time("sunset_minute",location_id)

cyberpi.display.show_label("Sunrise Time: {}".format(sunrise_time),12,0,20,1)
cyberpi.display.show_label("Sunrise Hour: {}".format(sunrise_hour),12,0,32,2)
cyberpi.display.show_label("Sunrise Minute: {}".format(sunrise_minute),12,0,46,3)
cyberpi.display.show_label("Sunset Time: {}".format(sunset_time),12,0,58,4)
cyberpi.display.show_label("Sunset Hour: {}".format(sunset_hour),12,0,70,5)
cyberpi.display.show_label("Sunset Minute: {}".format(sunset_minute),12,0,82,6)
