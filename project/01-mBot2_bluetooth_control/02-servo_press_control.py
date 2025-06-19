"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0  
Date        : 2025-06-19  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : mBot2 servo motor control with MakeBlock bluetooth controller for grab a small object
"""

import cyberpi, gamepad, mbot2

# Initialize motor speeds to zero. These variables will represent the target RPM
# for the left and right wheels.
v_left = 0
v_right = 0

# --- Servo Motor Initialization ---
# Set the servo connected to port 3 to an initial angle of 90 degrees.
# This might be its "neutral" or "open" position if controlling a gripper.
mbot2.servo_set(90, 3)

# --- Main Control Loop ---
# This loop continuously reads input from the gamepad and controls both
# the mBot2's movement and its servo motor.
while True:
    # --- Drive Motor Control (Tank Steering) ---
    # Calculate the target RPM for the left wheel.
    # 'Ly' (left joystick Y-axis) controls forward/backward movement.
    # 'Rx' (right joystick X-axis) controls turning.
    # Adding them together allows for combined movement and turning.
    v_left = (gamepad.get_joystick('Ly') + gamepad.get_joystick('Rx'))
    
    # Calculate the target RPM for the right wheel.
    # 'Rx' (right joystick X-axis) controls turning.
    # 'Ly' (left joystick Y-axis) controls forward/backward movement.
    # Subtracting 'Ly' from 'Rx' (differential steering) enables the robot
    # to turn by varying the speeds of the two wheels.
    v_right = (gamepad.get_joystick('Rx') - gamepad.get_joystick('Ly'))
    
    # --- Servo Motor Control (Gripper Action) ---
    # Check if the 'L1' button on the gamepad is pressed.
    # If pressed, set the servo to 180 degrees. This could be the "closed"
    # position for a gripper to grab an object.
    if gamepad.is_key_pressed('L1'):
        mbot2.servo_set(180, 3)
        
    # Check if the 'R1' button on the gamepad is pressed.
    # If pressed, set the servo back to 90 degrees. This could be the "open"
    # position for the gripper to release an object or return to neutral.
    if gamepad.is_key_pressed('R1'):
        mbot2.servo_set(90, 3)
    
    # --- Apply Drive Motor Speeds ---
    # Command the mBot2 to drive using the calculated RPMs for the left and right wheels.
    # The `drive_speed` function uses the mBot2's encoder motors to maintain these speeds.
    mbot2.drive_speed(v_left, v_right)
