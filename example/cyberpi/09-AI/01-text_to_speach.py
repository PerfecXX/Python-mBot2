import cyberpi

ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"

cyberpi.driver.cloud_translate.TTS_URL = "{TTSURL}"
cyberpi.driver.cloud_translate.set_token("{ACCESSTOKEN}")
cyberpi.driver.cloud_translate.TRANS_URL = "{TRANSURL}"
cyberpi.driver.cloud_translate.set_token("{ACCESSTOKEN}")
cyberpi.speech.set_recognition_address(url = "{NAVIGATEURL}")
cyberpi.speech.set_access_token(token = "{ACCESSTOKEN}")

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

cyberpi.display.show_label("Wait...",12,0,20,1)
cyberpi.led.on(0,0,255,id='all')
cyberpi.cloud.tts("en","Welcome to CyberPi, How can I help you?")
cyberpi.led.on(0,0,0,id='all')
cyberpi.display.show_label("Finished!",12,0,20,1)
