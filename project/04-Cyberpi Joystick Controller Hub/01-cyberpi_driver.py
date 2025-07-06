"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0  
Date        : 2025-07-06   
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : CyberPi blueooth controller UDP JSON sender script.
"""

import cyberpi
import gamepad
import socket
import time
import json

# Wi-Fi SSID and password to connect
ssid = "replace_with_your_ssid"
pwd = "replace_with_your_password"

# IP address and port of the receiving PC/server
PC_IP = "replace_with_your_server_ip"
PORT = "replace_with_your_server_port"

# Turn on red LED to indicate start status
cyberpi.led.on(255, 0, 0, id='all')

# Show status label on CyberPi display
cyberpi.display.show_label("Status:", 12, 0, 0, 0)

# Check Wi-Fi connection status; connect if not connected
if not cyberpi.wifi.is_connect():
    cyberpi.display.show_label("Status: No Connect", 12, 0, 0, 0)
    cyberpi.wifi.connect(ssid, pwd)
    # Wait until Wi-Fi is connected
    while not cyberpi.wifi.is_connect():
        cyberpi.display.show_label("Connecting..", 12, 0, 20, 1)

# Clear display and show connected status
cyberpi.display.clear()
cyberpi.display.show_label("Status: Connected!", 12, 0, 0, 0)

# Turn on green LED to indicate successful connection
cyberpi.led.on(0, 255, 0, id='all')

# Create UDP socket for sending data
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop to continuously send button and joystick data
while True:
    data = {}

    # Check which buttons are pressed and add them to the list
    buttons = []
    for key in ['Up', 'Down', 'Left', 'Right',
                'N1', 'N2', 'N3', 'N4',
                'L1', 'L2', 'R1', 'R2',
                'L_Thumb', 'R_Thumb',
                'Start', 'Select']:
        if gamepad.is_key_pressed(key):
            buttons.append(key)
    data['buttons'] = buttons  # Store button data in dictionary

    # Store joystick axis positions for left and right sticks
    data['joystick'] = {
        'Lx': gamepad.get_joystick('Lx'),
        'Ly': gamepad.get_joystick('Ly'),
        'Rx': gamepad.get_joystick('Rx'),
        'Ry': gamepad.get_joystick('Ry'),
    }

    # Convert data dictionary to JSON string
    message = json.dumps(data)
    # Send JSON data via UDP to specified IP and port
    sock.sendto(message.encode(), (PC_IP, PORT))
