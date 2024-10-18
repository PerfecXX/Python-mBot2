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

aqi = cyberpi.cloud.air("aqi",location_id)
pm25 = cyberpi.cloud.air("pm2.5",location_id)
pm10 = cyberpi.cloud.air("pm10",location_id)
co = cyberpi.cloud.air("co",location_id)
so2 = cyberpi.cloud.air("so2",location_id)
no2 = cyberpi.cloud.air("no2",location_id)

cyberpi.display.show_label("AQI: {}".format(aqi),12,0,20,1)
cyberpi.display.show_label("PM2.5: {}".format(pm25),12,0,32,2)
cyberpi.display.show_label("PM10: {}".format(pm10),12,0,46,3)
cyberpi.display.show_label("CO: {}".format(co),12,0,58,4)
cyberpi.display.show_label("SO2: {}".format(so2),12,0,70,5)
cyberpi.display.show_label("NO2: {}".format(no2),12,0,82,6)
