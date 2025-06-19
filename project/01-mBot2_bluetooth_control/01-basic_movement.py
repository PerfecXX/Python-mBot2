"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0  
Date        : 2025-06-19  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : Movement control for mBot2 using the Makeblock Bluetooth Joystick Controller.
"""

import cyberpi, gamepad, mbot2

# Initialize motor speeds. These variables will store the target RPM (Revolutions Per Minute)
# for the left and right wheels, respectively.
v_left = 0
v_right = 0

# Main loop for continuous robot control.
# This loop constantly reads joystick input and updates the mBot2's movement.
while True:
    # Calculate the target RPM for the left wheel.
    # 'Ly' (left joystick Y-axis) contributes to forward/backward movement.
    # 'Rx' (right joystick X-axis) contributes to turning.
    # By adding these, pushing the left stick forward and the right stick right
    # would generally increase the left wheel's speed (for a right turn).
    v_left = (gamepad.get_joystick('Ly') + gamepad.get_joystick('Rx'))
    
    # Calculate the target RPM for the right wheel.
    # 'Rx' (right joystick X-axis) contributes to turning.
    # 'Ly' (left joystick Y-axis) contributes to forward/backward movement.
    # Subtracting 'Ly' from 'Rx' (instead of adding like v_left) creates
    # differential steering:
    # - If Ly is positive (forward), v_left increases, v_right decreases (turning right)
    # - If Ly is negative (backward), v_left decreases, v_right increases (turning left)
    # This logic allows for intuitive control like tank steering.
    v_right = (gamepad.get_joystick('Rx') - gamepad.get_joystick('Ly'))
    
    # Command the mBot2 to drive. The `drive_speed` function uses the calculated
    # 'v_left' and 'v_right' values as target RPMs for the respective wheels.
    # The mBot2's built-in encoder motors will work to maintain these speeds.
    mbot2.drive_speed(v_left, v_right)
