"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0  
Date        : 2025-06-28  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : Color detection using mBuild Smart Camera with mBot2.  
              Learns and detects 4 preset colors and displays the result on screen and LEDs.
"""

import cyberpi, mbuild, time

# Initialize smart camera in color recognition mode and turn on its light
cyberpi.console.clear()
mbuild.smart_camera.set_mode("color", 1)
mbuild.smart_camera.open_light(1)

# Display initial title
cyberpi.display.show_label("Smart Camera Test", 12, 10, 0, index=0)

# ----------- Learn Color 1: RED -----------
cyberpi.display.set_brush(255, 0, 0)
cyberpi.display.show_label("Color1 : RED", 12, 10, 20, index=1)
cyberpi.display.set_brush(255, 255, 255)
cyberpi.display.show_label("Press \"Learn\" button to Continue", 12, 5, 40, index=2)
mbuild.smart_camera.learn(1, "until_button", 1)

# ----------- Learn Color 2: GREEN -----------
cyberpi.display.set_brush(0, 255, 0)
cyberpi.display.show_label("Color2 : Green", 12, 10, 20, index=1)
cyberpi.display.set_brush(255, 255, 255)
cyberpi.display.show_label("Press \"Learn\" button to Continue", 12, 5, 40, index=2)
mbuild.smart_camera.learn(2, "until_button", 1)

# ----------- Learn Color 3: BLUE -----------
cyberpi.display.set_brush(0, 0, 255)
cyberpi.display.show_label("Color3 : Blue", 12, 10, 20, index=1)
cyberpi.display.set_brush(255, 255, 255)
cyberpi.display.show_label("Press \"Learn\" button to Continue", 12, 5, 40, index=2)
mbuild.smart_camera.learn(3, "until_button", 1)

# ----------- Learn Color 4: YELLOW -----------
cyberpi.display.set_brush(255, 255, 0)
cyberpi.display.show_label("Color4 : Yellow", 12, 10, 20, index=1)
cyberpi.display.set_brush(255, 255, 255)
cyberpi.display.show_label("Press \"Learn\" button to Continue", 12, 5, 40, index=2)
mbuild.smart_camera.learn(4, "until_button", 1)

# Clear the console before entering detection loop
cyberpi.console.clear()

# ----------- Color Detection Loop -----------
while True:
    # Detect Color 1: RED
    if mbuild.smart_camera.detect_sign(1, 1):
        cyberpi.led.on(208, 2, 27, "all")
        cyberpi.display.show_label("Detected: RED", 12, 5, 60, index=3)

    # Detect Color 2: GREEN
    elif mbuild.smart_camera.detect_sign(2, 1):
        cyberpi.led.on(124, 255, 2, "all")
        cyberpi.display.show_label("Detected: GREEN", 12, 5, 60, index=3)

    # Detect Color 3: BLUE
    elif mbuild.smart_camera.detect_sign(3, 1):
        cyberpi.led.on(40, 2, 255, "all")
        cyberpi.display.show_label("Detected: BLUE", 12, 5, 60, index=3)

    # Detect Color 4: YELLOW
    elif mbuild.smart_camera.detect_sign(4, 1):
        cyberpi.led.on(255, 208, 1, "all")
        cyberpi.display.show_label("Detected: YELLOW", 12, 5, 60, index=3)

    # No color detected
    else:
        cyberpi.led.off("all")
        cyberpi.display.show_label("Detected: None", 12, 5, 60, index=3)

    time.sleep(0.1)
