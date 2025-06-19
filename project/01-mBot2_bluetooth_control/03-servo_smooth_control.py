"""
Author      : Teeraphat Kullanankanjana  
Version     : 1.0  
Date        : 2025-06-19  
Copyright   : © 2025 Teeraphat Kullanankanjana. All rights reserved.  
Description : mBot2 servo motor control with MakeBlock bluetooth controller for grab a small object.
              Features incremental servo movement for smooth gripping and releasing.
"""

import cyberpi, gamepad, mbot2

# Initialize motor speeds to zero. These variables will represent the target RPM
# for the left and right wheels.
v_left = 0
v_right = 0

# Define servo motor port
SERVO_PORT = 3

# Define target angles for gripper
GRIP_OPEN_ANGLE = 90  # Angle for the gripper to be fully open
GRIP_CLOSED_ANGLE = 180 # Angle for the gripper to be fully closed (or holding)

# Define the step size for servo movement (how many degrees to move per loop cycle)
# A smaller step (e.g., 1) makes movement smoother but slower.
# A larger step (e.g., 5) makes movement faster but less smooth.
SERVO_STEP_SIZE = 1

# Initial servo position: Set the gripper to its open position at the start.
mbot2.servo_set(GRIP_OPEN_ANGLE, SERVO_PORT)
# Keep track of the servo's current position. This is crucial for incremental control.
current_servo_angle = GRIP_OPEN_ANGLE

# --- Main Control Loop ---
# This loop continuously reads input from the gamepad and controls both
# the mBot2's movement and its servo motor.
while True:
    # --- Drive Motor Control (Tank Steering) ---
    # Calculate the target RPM for the left wheel based on joystick inputs.
    # 'Ly' (left joystick Y-axis) controls forward/backward movement.
    # 'Rx' (right joystick X-axis) controls turning.
    v_left = (gamepad.get_joystick('Ly') + gamepad.get_joystick('Rx'))
    
    # Calculate the target RPM for the right wheel based on joystick inputs.
    # 'Rx' (right joystick X-axis) controls turning.
    # 'Ly' (left joystick Y-axis) controls forward/backward movement.
    v_right = (gamepad.get_joystick('Rx') - gamepad.get_joystick('Ly'))
    
    # --- Servo Motor Control (Incremental Gripper Action) ---
    # Check if the 'L1' button is pressed to start closing the gripper.
    # Only move if the current angle is less than the target closed angle.
    if gamepad.is_key_pressed('L1'):
        if current_servo_angle < GRIP_CLOSED_ANGLE:
            # Increment the angle, but don't go past the closed angle
            current_servo_angle = min(current_servo_angle + SERVO_STEP_SIZE, GRIP_CLOSED_ANGLE)
            
    # Check if the 'R1' button is pressed to start opening the gripper.
    # Only move if the current angle is greater than the target open angle.
    elif gamepad.is_key_pressed('R1'):
        if current_servo_angle > GRIP_OPEN_ANGLE:
            # Decrement the angle, but don't go below the open angle
            current_servo_angle = max(current_servo_angle - SERVO_STEP_SIZE, GRIP_OPEN_ANGLE)
            
    # Update the servo's position to the new calculated current_servo_angle.
    # This command is called in every loop cycle, causing the servo to move
    # continuously as long as the button is held and limit is not reached.
    mbot2.servo_set(current_servo_angle, SERVO_PORT)
    
    # --- Apply Drive Motor Speeds ---
    # Command the mBot2 to drive using the calculated RPMs for the left and right wheels.
    mbot2.drive_speed(v_left, v_right)
