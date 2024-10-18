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

cloud_year = cyberpi.cloud.time('year',time_zone)
cloud_month = cyberpi.cloud.time('month',time_zone)
cloud_day = cyberpi.cloud.time('day',time_zone)
cloud_week = cyberpi.cloud.time("week",time_zone)
cloud_hour = cyberpi.cloud.time("hour",time_zone)
cloud_minute = cyberpi.cloud.time("minute",time_zone)
cloud_second = cyberpi.cloud.time("second",time_zone)

cyberpi.display.show_label("Year: {}".format(cloud_year),12,0,20,1)
cyberpi.display.show_label("Month: {}".format(cloud_month),12,0,32,2)
cyberpi.display.show_label("Day: {}".format(cloud_day),12,0,46,3)
cyberpi.display.show_label("Week: {}".format(cloud_week),12,0,58,4)
cyberpi.display.show_label("Hour: {}".format(cloud_hour),12,0,70,5)
cyberpi.display.show_label("Minute: {}".format(cloud_minute),12,0,82,6)
cyberpi.display.show_label("Second: {}".format(cloud_second),12,0,94,7)
