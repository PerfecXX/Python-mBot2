import cyberpi
from time import sleep

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

while True:
    cyberpi.display.show_label("A:Start Recognize",12,0,20,1)
    cyberpi.led.on(0,0,0,id='all')

    if cyberpi.controller.is_press('a'):
        sleep(0.5)
        cyberpi.led.on(0,0,255,id='all')
        cyberpi.display.show_label("Recognizing...",12,0,40,2)
        cyberpi.cloud.listen(langauge_list[4], 5)
        cyberpi.display.show_label("Processing...",12,0,40,2)
        cyberpi.led.on(0,0,0,id='all')
        recog_result = cyberpi.cloud.listen_result()
        cyberpi.display.show_label("Recognition Result\n\n{}".format(recog_result),12,0,40,2)
