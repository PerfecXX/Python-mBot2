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

max_temp = cyberpi.cloud.weather("max_temp",location_id)
min_temp = cyberpi.cloud.weather("max_temp",location_id)
weather = cyberpi.cloud.weather("weather",location_id)
humidity = cyberpi.cloud.weather("humidity",location_id)

cyberpi.display.show_label("Max Temperature: {} C".format(max_temp),12,0,20,1)
cyberpi.display.show_label("Min Temperature: {} C".format(min_temp),12,0,32,2)
cyberpi.display.show_label("Weather: {}".format(weather),12,0,42,3)
cyberpi.display.show_label("Humidity: {} %".format(humidity),12,0,52,4)
