"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0.0  
Date        : 2025-07-12  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : 
    Connects CyberPi to WiFi, recursively lists all files in root directory,
    and sends each file to a server via TCP socket with handshake confirmation.
"""

import network       # Module to manage network interfaces (WiFi)
import socket        # Module for socket programming (TCP/IP)
import os            # Module to interact with the file system
import time          # Module for delay and timing functions

# WiFi credentials and server info (replace these with your own settings)
SSID = 'replace_with_your_SSID'
PASSWORD = 'replace_with_your_password'
SERVER_IP = 'replace_with_your_server_ip'
SERVER_PORT = 12345  # Replace with your server port if different

def connect_wifi(ssid, password):
    """
    Connect to the specified WiFi network using given SSID and password.
    Returns True if connected successfully, False otherwise.
    """
    wlan = network.WLAN(network.STA_IF)  # Create station interface
    wlan.active(True)                     # Activate the interface
    if not wlan.isconnected():            # If not connected yet
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)      # Start connection
        timeout = 15                      # Timeout in seconds
        start = time.time()
        while not wlan.isconnected():
            if time.time() - start > timeout:
                print('Failed to connect to WiFi')
                return False
            time.sleep(1)                 # Wait 1 second before checking again
    ip = wlan.ifconfig()[0]               # Get assigned IP address
    print('Connected, IP address:', ip)
    return True

def list_files_recursive(path='/'):
    """
    Recursively list all files starting from 'path'.
    Returns a list of file paths.
    """
    files = []
    try:
        entries = os.listdir(path)         # List directory contents
        for entry in entries:
            # Construct full path (handle root '/')
            full_path = path + '/' + entry if path != '/' else '/' + entry
            # Check if entry is a directory
            if os.stat(full_path)[0] & 0x4000:
                files.extend(list_files_recursive(full_path))  # Recurse into directory
            else:
                files.append(full_path)   # Add file path to list
    except Exception as e:
        print('Error listing files:', e)
    return files

def send_file(sock, filepath):
    """
    Send a single file to the server through socket 'sock'.
    Protocol:
        1. Send the filepath (utf-8 encoded + newline).
        2. Wait for 'READY' response from server.
        3. Send file data in chunks.
        4. Send 'EOF' marker.
        5. Wait for 'OK' response from server.
    Returns True if file sent successfully, False otherwise.
    """
    print('Sending file:', filepath)
    sock.send(filepath.encode('utf-8') + b'\n')  # Send filename
    ack = sock.recv(64)                           # Receive server acknowledgment
    if ack.strip() != b'READY':
        print('No READY from server, skip file')
        return False
    try:
        with open(filepath, 'rb') as f:           # Open file in binary mode
            while True:
                data = f.read(1024)                # Read file in 1KB chunks
                if not data:
                    break
                sock.send(data)                    # Send chunk to server
        time.sleep(0.1)                            # Short delay before EOF
        sock.send(b'EOF\n')                        # Send EOF marker
        ack2 = sock.recv(64)                       # Receive final server response
        if ack2.strip() == b'OK':
            print('File sent:', filepath)
            return True
        else:
            print('No OK after sending file')
            return False
    except Exception as e:
        print('Error sending file:', e)
        return False

# Main process starts here
if connect_wifi(SSID, PASSWORD):
    files = list_files_recursive('/')             # Get all files from root recursively
    print('Files to send:', files)
    try:
        sock = socket.socket()                     # Create TCP socket
        sock.connect((SERVER_IP, SERVER_PORT))    # Connect to server
        print('Connected to server', SERVER_IP, SERVER_PORT)
        for f in files:
            if not send_file(sock, f):
                print('Failed sending:', f)
        sock.close()                               # Close socket after all files sent
        print('All done.')
    except Exception as e:
        print('Socket connect failed:', e)
else:
    print('WiFi connection failed.')
