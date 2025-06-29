import cyberpi
import time
from mqtt import MQTTClient

cyberpi.console.set_font(12)

ssid = 'replace_with_your_ssid'
password = 'replace_with_your_password'

def wifi_connect():
    cyberpi.wifi.connect(ssid, password)
    cyberpi.console.println("Connecting to WiFi...")
    while not cyberpi.wifi.is_connected():
        time.sleep(0.5)
    cyberpi.console.println("WiFi connected!")

wifi_connect()

mqtt_server = 'test.mosquitto.org'
client_id = 'cyberpi_publish'
topic_pub = b'test/topic'

client = MQTTClient(client_id, mqtt_server)
client.connect()
cyberpi.console.println('Connected to MQTT broker')

while True:
    client.publish(topic_pub, 'Hello from CyberPi Publisher')
    cyberpi.console.println('Published message')
    time.sleep(5)
