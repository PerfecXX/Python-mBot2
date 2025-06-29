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
client_id = 'cyberpi_subscribe'
topic_sub = b'test/topic'

def on_message(topic, msg):
    cyberpi.console.println('Received: {} => {}'.format(topic.decode(), msg.decode()))

client = MQTTClient(client_id, mqtt_server)
client.set_callback(on_message)
client.connect()
client.subscribe(topic_sub)
cyberpi.console.println('Connected and subscribed to {}'.format(topic_sub.decode()))

while True:
    client.check_msg()
    time.sleep(1)
