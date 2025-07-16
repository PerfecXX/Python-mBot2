"""
Author      : Teeraphat Kullanankanjana
Version     : 1.0.0
Date        : 2025-07-17
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.
Description : This script runs a TCP server on CyberPi to allow remote file management
              (listing, uploading, downloading, renaming, deleting files and folders)
              over Wi-Fi using a custom protocol. It's designed to interact with a
              companion GUI client application.
"""

import network
import socket
import ujson as json
import os
import time

# --- Wi-Fi Configuration ---
SSID = "replace_with_your_ssid"
PASSWORD = "replace_with_your_password"
PORT = 12345 # Port for the TCP server

def connect_wifi():
    """
    Connects the CyberPi to the specified Wi-Fi network.
    Waits for a connection or times out after 20 seconds.
    Returns the assigned IP address if successful, otherwise None.
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Connecting to WiFi...")
    try:
        wlan.connect(SSID, PASSWORD)
        timeout_seconds = 20
        start_time = time.time()
        # Wait for the connection to be established or timeout
        while not wlan.isconnected() and (time.time() - start_time) < timeout_seconds:
            time.sleep(1)
        
        if wlan.isconnected():
            ip_address = wlan.ifconfig()[0]
            print("Connected, IP:", ip_address)
            return ip_address
        else:
            print("Failed to connect to WiFi within timeout.")
            return None
    except Exception as e:
        print("Error during WiFi connection: {}".format(e))
        return None

def list_all_files(path='/'):
    """
    Recursively lists all files and directories starting from the given path.
    Returns a list of dictionaries, where each dictionary contains 'path' and 'type' (file/dir).
    """
    items = []
    try:
        # Iterate through all entries in the current directory
        for entry in os.listdir(path):
            # Construct the full path, handling the root directory correctly
            if path == '/':
                full_path = '/' + entry
            else:
                full_path = path + '/' + entry

            try:
                # Get file/directory mode using os.stat()
                mode = os.stat(full_path)[0]
                # Check if it's a directory (MicroPython mode for directory often has 0x4000 bit set)
                if (mode & 0x4000) != 0: 
                    items.append({"path": full_path, "type": "dir"})
                    # If it's a directory, recursively list its contents
                    items.extend(list_all_files(full_path)) 
                else:
                    # Otherwise, it's a file
                    items.append({"path": full_path, "type": "file"})
            except OSError as e:
                print('Error accessing {}: {}'.format(full_path, e))
    except OSError as e:
        print('Error listing {}: {}'.format(path, e))
    return items

def recv_all(cl, size):
    """
    Receives all expected bytes from a socket until the specified size is reached.
    Handles potential partial reads.
    """
    data = b''
    while len(data) < size:
        # Read data in chunks, up to 4096 bytes or remaining size
        packet = cl.recv(min(size - len(data), 4096))
        if not packet: # Connection closed or no more data
            break
        data += packet
    return data

def send_all(sock, data_bytes):
    """
    Sends all bytes over a socket in chunks to prevent buffer overflows,
    especially important for large data on embedded devices.
    """
    chunk_size = 1024 # Define a suitable chunk size
    for i in range(0, len(data_bytes), chunk_size):
        sock.send(data_bytes[i:i+chunk_size])
        time.sleep(0.01) # Small delay to prevent overwhelming the receiver/sender buffer

def handle_command(cmd, cl):
    """
    Parses and executes commands received from the client.
    Supported commands: LIST_FILES, RENAME, DELETE, UPLOAD, DOWNLOAD.
    """
    parts = cmd.split('|', 2) # Split command into parts, max 2 splits
    command = parts[0]
    print("Executing command: {}".format(command))

    try:
        if command == "LIST_FILES":
            # Get list of all files and folders in JSON format
            files = list_all_files('/') 
            json_data = json.dumps(files)
            send_all(cl, json_data.encode())
            print("Sent {} bytes of file list.".format(len(json_data)))

        elif command == "RENAME":
            # RENAME|old_path|new_name
            if len(parts) != 3:
                cl.send(b"ERROR|Invalid RENAME format")
                print("Error: Invalid RENAME format.")
                return
            old_path, new_name = parts[1], parts[2]
            
            # Construct the new path correctly based on the old path's directory
            base_path = os.dirname(old_path)
            if base_path == '.' and old_path.startswith('/'): # Handle root directory case
                base_path = '/'
            elif base_path == '.': # If it's a file in the current directory (shouldn't happen with full paths)
                 base_path = ''

            if base_path == '/': # If old_path was directly in root
                new_path = '/' + new_name
            elif base_path == '': # Should ideally not occur with full paths
                new_path = new_name
            else: # If old_path was in a subdirectory
                new_path = base_path + '/' + new_name
            
            os.rename(old_path, new_path)
            cl.send(b"OK|Renamed")
            print("Renamed '{}' to '{}'".format(old_path, new_path))

        elif command == "DELETE":
            # DELETE|path
            if len(parts) != 2:
                cl.send(b"ERROR|Invalid DELETE format")
                print("Error: Invalid DELETE format.")
                return
            path = parts[1]
            try:
                # Check if it's a directory or a file before attempting deletion
                mode = os.stat(path)[0]
                if (mode & 0x4000) != 0: # It's a directory
                    os.rmdir(path) # Use rmdir for directories
                else: # It's a file
                    os.remove(path) # Use remove for files
                cl.send(b"OK|Deleted")
                print("Deleted '{}'".format(path))
            except OSError as e:
                cl.send(("ERROR|File operation error: " + str(e)).encode())
                print("Error deleting '{}': {}".format(path, e))

        elif command == "UPLOAD":
            # UPLOAD|target_path|filesize
            if len(parts) != 3:
                cl.send(b"ERROR|Invalid UPLOAD header")
                print("Error: Invalid UPLOAD header.")
                return
            target_path, filesize_str = parts[1], parts[2]
            filesize = int(filesize_str)
            
            cl.send(b"OK|Ready") # Acknowledge readiness to receive file data
            print("Ready to receive {} bytes for '{}'".format(filesize, target_path))
            
            # Receive the entire file data
            file_data = recv_all(cl, filesize)
            
            if len(file_data) != filesize:
                cl.send(b"ERROR|Partial data received")
                print("Error: Partial data received for '{}'. Expected {}, got {}.".format(target_path, filesize, len(file_data)))
                return

            try:
                # Write the received data to the specified file
                with open(target_path, 'wb') as f:
                    f.write(file_data)
                cl.send(b"OK|Uploaded")
                print("Uploaded '{}' successfully.".format(target_path))
            except Exception as e:
                cl.send(("ERROR|" + str(e)).encode())
                print("Error writing uploaded file '{}': {}".format(target_path, e))

        elif command == "DOWNLOAD":
            # DOWNLOAD|filepath
            if len(parts) != 2:
                cl.send(b"ERROR|Invalid DOWNLOAD format")
                print("Error: Invalid DOWNLOAD format.")
                return
            filepath = parts[1]
            try:
                # Get file size and send it as a header
                filesize = os.stat(filepath)[6] # Index 6 usually contains file size on MicroPython
                cl.send(("SIZE|" + str(filesize)).encode())
                print("Sent SIZE header for '{}': {} bytes.".format(filepath, filesize))
                
                # Wait for client's acknowledgment before sending file content
                ack = cl.recv(1024)
                if ack != b"OK":
                    print("Client did not acknowledge size. Received: {}".format(ack))
                    return

                # Send file content in chunks
                with open(filepath, 'rb') as f:
                    while True:
                        chunk = f.read(1024)
                        if not chunk: # End of file
                            break
                        cl.send(chunk)
                print("Sent file '{}' completely.".format(filepath))
            except OSError as e:
                cl.send(("ERROR|File error: " + str(e)).encode())
                print("Error accessing file '{}' for download: {}".format(filepath, e))
            except Exception as e:
                cl.send(("ERROR|" + str(e)).encode())
                print("General error during download of '{}': {}".format(filepath, e))

        else:
            cl.send(b"ERROR|Unknown command")
            print("Error: Unknown command received: {}".format(command))
            
    except Exception as e:
        cl.send(("ERROR|" + str(e)).encode())
        print("Unhandled error in handle_command for '{}': {}".format(command, e))

def run_server():
    """
    Initializes and runs the TCP server.
    Connects to Wi-Fi, binds a socket, listens for incoming client connections,
    and handles commands for each connected client.
    """
    ip = connect_wifi()
    if not ip:
        print("Could not connect to WiFi. Server will not start.")
        return

    # Get address information for the server socket
    addr = socket.getaddrinfo('0.0.0.0', PORT)[0][-1]
    s = socket.socket()
    s.bind(addr) # Bind the socket to the address
    s.listen(1) # Listen for one incoming connection
    print('Listening on {}'.format(addr))

    while True:
        cl, addr = s.accept() # Accept a new client connection
        print('Client connected from {}'.format(addr))
        try:
            cl.settimeout(30) # Set a timeout for client communication
            data = cl.recv(1024) # Receive the command
            if data:
                cmd = data.decode().strip()
                print('Received command: "{}"'.format(cmd))
                handle_command(cmd, cl) # Handle the received command
            else:
                print("Received empty data from client.")
        except OSError as e:
            print("Socket error with client {}: {}".format(addr, e))
        except Exception as e:
            print("Unexpected error with client {}: {}".format(addr, e))
        finally:
            cl.close() # Always close the client socket
            print("Client {} disconnected.".format(addr))

# --- Main entry point ---
run_server()
