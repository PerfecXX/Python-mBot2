import network
import socket
import ujson as json
import os
import time

SSID = "PX_SYSTEM_2.4G"
PASSWORD = "PX123456789"
PORT = 12345  # port socket server

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected, IP:", wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

def list_all_files(path='/'):
    files = []
    try:
        for entry in os.listdir(path):
            full_path = path + '/' + entry if path != '/' else '/' + entry
            try:
                if (os.stat(full_path)[0] & 0x4000):  # directory
                    files.append(full_path + '/')
                    files.extend(list_all_files(full_path))
                else:
                    files.append(full_path)
            except Exception as e:
                print('Error accessing {}: {}'.format(full_path, e))
    except Exception as e:
        print('Error listing {}: {}'.format(path, e))
    return files

def recv_all(cl, size):
    data = b''
    while len(data) < size:
        packet = cl.recv(size - len(data))
        if not packet:
            break
        data += packet
    return data

def handle_command(cmd, cl):
    parts = cmd.split('|', 2)
    command = parts[0]
    try:
        if command == "LIST_FILES":
            files = list_all_files('/')
            json_data = json.dumps(files)
            send_all(cl, json_data.encode())
        elif command == "RENAME":
            if len(parts) != 3:
                cl.send(b"ERROR|Invalid RENAME format")
                return
            old_path, new_name = parts[1], parts[2]
            base_path = '/'.join(old_path.split('/')[:-1])
            new_path = base_path + '/' + new_name if base_path != '' else '/' + new_name
            os.rename(old_path, new_path)
            cl.send(b"OK|Renamed")
        elif command == "DELETE":
            if len(parts) != 2:
                cl.send(b"ERROR|Invalid DELETE format")
                return
            path = parts[1]
            stat = os.stat(path)[0]
            if stat & 0x4000:  # directory
                os.rmdir(path)
            else:
                os.remove(path)
            cl.send(b"OK|Deleted")
        elif command == "UPLOAD":
            # Format: UPLOAD|target_path|filesize
            if len(parts) != 3:
                cl.send(b"ERROR|Invalid UPLOAD header")
                return
            header_rest = parts[1] + '|' + parts[2]
            target_path, filesize_str = header_rest.split('|', 1)
            filesize = int(filesize_str)
            # รับไฟล์ไบต์ตามขนาด filesize
            cl.send(b"OK|Ready")
            file_data = recv_all(cl, filesize)
            # หาชื่อไฟล์จาก target_path (target_path ต้องมีชื่อไฟล์เต็ม เช่น /music/myfile.py)
            try:
                with open(target_path, 'wb') as f:
                    f.write(file_data)
                cl.send(b"OK|Uploaded")
            except Exception as e:
                cl.send(("ERROR|"+str(e)).encode())
        else:
            cl.send(b"ERROR|Unknown command")
    except Exception as e:
        cl.send(("ERROR|" + str(e)).encode())

def send_all(sock, data_bytes):
    chunk_size = 1024
    for i in range(0, len(data_bytes), chunk_size):
        sock.send(data_bytes[i:i+chunk_size])
        time.sleep(0.01)

def run_server():
    ip = connect_wifi()
    addr = socket.getaddrinfo('0.0.0.0', PORT)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)
    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        try:
            data = cl.recv(1024)
            if data:
                cmd = data.decode().strip()
                print('Received command:', cmd)
                handle_command(cmd, cl)
        except Exception as e:
            print("Socket error:", e)
        cl.close()

run_server()
