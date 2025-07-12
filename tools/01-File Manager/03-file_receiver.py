"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0.0  
Date        : 2025-07-12  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : 
    A TCP socket server that listens for incoming file transfers,
    receives files sent line-by-line with EOF delimiter,
    and saves them safely to a local directory.
"""

import socket
import os

HOST = '0.0.0.0'      # Listen on all interfaces
PORT = 12345          # TCP port to listen on

SAVE_DIR = 'received_files'   # Directory to save received files
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)      # Create directory if it doesn't exist

def recv_line(conn):
    """
    Receive bytes from socket until a newline character (\n) is found.
    Return the decoded string without trailing newline.
    """
    line = b''
    while True:
        c = conn.recv(1)     # Receive one byte
        if not c:
            break           # Connection closed or no data
        if c == b'\n':      # End of line detected
            break
        line += c
    return line.decode('utf-8').strip()

def handle_client(conn, addr):
    """
    Handle a connected client.
    Repeatedly receive a filename, send READY,
    receive file data until EOF marker,
    then send OK.
    """
    print(f'Connected by {addr}')
    try:
        while True:
            filename = recv_line(conn)   # Receive filename
            if not filename:
                print('No filename received, closing connection')
                break

            print('Receiving file:', filename)
            conn.sendall(b'READY\n')    # Signal ready to receive file

            # Sanitize filename to avoid path traversal attacks
            safe_filename = filename.replace('/', '_').lstrip('_')
            filepath = os.path.join(SAVE_DIR, safe_filename)

            with open(filepath, 'wb') as f:
                while True:
                    data = conn.recv(1024)  # Receive file data chunk
                    if not data:
                        print('Connection closed by client')
                        return
                    # Check for EOF marker in data
                    if b'EOF\n' in data:
                        eof_index = data.find(b'EOF\n')
                        f.write(data[:eof_index])  # Write up to EOF
                        break
                    f.write(data)

            conn.sendall(b'OK\n')    # Confirm file received successfully
            print('File saved:', filepath)
    except Exception as e:
        print('Error:', e)
    finally:
        conn.close()
        print(f'Disconnected from {addr}')

def run_server():
    """
    Start the TCP server to listen and accept incoming connections.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f'Server listening on {HOST}:{PORT}')
        while True:
            conn, addr = s.accept()  # Accept client connection
            handle_client(conn, addr)  # Handle client communication

if __name__ == '__main__':
    run_server()
