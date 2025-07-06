"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0  
Date        : 2025-07-06   
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : Pygame GUI server for real-time display of JSON gamepad data from multiple CyberPi devices via UDP.
"""

import pygame
import socket
import threading
import json
import time
import queue

# === UDP Server Setup ===
UDP_IP = "0.0.0.0"
UDP_PORT = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)

# === Queue for safely passing UDP packets to main thread ===
data_queue = queue.Queue()

# === Start UDP Listener Thread ===
def receive_udp():
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            ip = addr[0]
            msg = data.decode("utf-8")
            data_queue.put((ip, msg))
        except BlockingIOError:
            continue

threading.Thread(target=receive_udp, daemon=True).start()

# === Pygame Initialization ===
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CyberPi Bluetooth Controller Monitor")
font_title = pygame.font.SysFont("Arial", 22, bold=True)
font_text = pygame.font.SysFont("Consolas", 18)

# === Colors ===
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOX_BG = (30, 30, 30)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# === Store device states ===
devices = {}

# === Main Loop ===
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # === Handle Events ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === Process new UDP data ===
    while not data_queue.empty():
        ip, raw = data_queue.get()
        try:
            parsed = json.loads(raw)
            devices[ip] = {
                'data': parsed,
                'time': time.time()
            }
        except json.JSONDecodeError:
            continue

    # === Draw device blocks ===
    keys = list(devices.keys())
    for i, ip in enumerate(keys):
        x = 20 + (i % 2) * (WIDTH // 2)
        y = 20 + (i // 2) * 180
        w = WIDTH // 2 - 40
        h = 160

        # Background and border
        pygame.draw.rect(screen, BOX_BG, (x, y, w, h), border_radius=8)
        border_color = GREEN if time.time() - devices[ip]['time'] < 1.5 else RED
        pygame.draw.rect(screen, border_color, (x, y, w, h), 2, border_radius=8)

        # Header
        screen.blit(font_title.render("IP: {}".format(ip), True, WHITE), (x + 10, y + 10))

        d = devices[ip]['data']
        buttons = d.get("buttons", [])
        js = d.get("joystick", {})

        # Content
        btn_str = ", ".join(buttons) if buttons else "None"
        screen.blit(font_text.render("Buttons: {}".format(btn_str), True, WHITE), (x + 20, y + 50))

        screen.blit(font_text.render("Lx: {:.2f}".format(js.get("Lx", 0.0)), True, WHITE), (x + 20, y + 80))
        screen.blit(font_text.render("Ly: {:.2f}".format(js.get("Ly", 0.0)), True, WHITE), (x + 200, y + 80))
        screen.blit(font_text.render("Rx: {:.2f}".format(js.get("Rx", 0.0)), True, WHITE), (x + 20, y + 110))
        screen.blit(font_text.render("Ry: {:.2f}".format(js.get("Ry", 0.0)), True, WHITE), (x + 200, y + 110))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
