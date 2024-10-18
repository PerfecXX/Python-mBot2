import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"

langauge_list = ["chinese","chinese_taiwan","cantonese","japanese","english","french","german","spanish","portuguese","russian","korean","italian","Dutch"]
cyberpi.driver.cloud_translate.TTS_URL = "{TTSURL}"
cyberpi.driver.cloud_translate.set_token("{ACCESSTOKEN}")
cyberpi.speech.set_recognition_address(url = "{NAVIGATEURL}")
cyberpi.speech.set_access_token(token = "{ACCESSTOKEN}")
cyberpi.driver.cloud_translate.TRANS_URL = "{TRANSURL}"
cyberpi.driver.cloud_translate.set_token("{ACCESSTOKEN}")

cyberpi.led.on(255,0,0,id='all')
cyberpi.display.show_label("WiFi:",12,0,0,0)

if not cyberpi.wifi.is_connect():
    cyberpi.display.show_label("WiFi: No Connect",12,0,0,0)
    cyberpi.wifi.connect(ssid,pwd)
    while not cyberpi.wifi.is_connect():
        cyberpi.display.show_label("Connecting..",12,0,20,1)

cyberpi.display.clear()
cyberpi.display.show_label("WiFi: Connected!",12,0,0,0)
cyberpi.led.on(0,255,0,id='all')

text = "Good Morning!"
cyberpi.display.show_label("translate: \n{} to {}".format(text,langauge_list[3]),12,0,20,1)
translated_text = cyberpi.cloud.translate(langauge_list[3], text)
cyberpi.display.show_label("Result: \n{}".format(translated_text),12,0,80,2)


