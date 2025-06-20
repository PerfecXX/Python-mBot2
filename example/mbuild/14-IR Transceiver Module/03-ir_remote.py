import cyberpi, mbuild

# Letter buttons
IR_CODE_A = 69
IR_CODE_B = 70
IR_CODE_C = 71
IR_CODE_D = 68
IR_CODE_E = 67
IR_CODE_F = 13

# Arrow and setting buttons
IR_CODE_ARROW_UP = 64
IR_CODE_ARROW_DOWN = 25
IR_CODE_ARROW_LEFT = 7
IR_CODE_ARROW_RIGHT = 9
IR_CODE_SETTING = 21

# Number buttons
IR_CODE_0 = 22
IR_CODE_1 = 12
IR_CODE_2 = 24
IR_CODE_3 = 94
IR_CODE_4 = 8
IR_CODE_5 = 28
IR_CODE_6 = 90
IR_CODE_7 = 66
IR_CODE_8 = 82
IR_CODE_9 = 74

while True:
  
    received_code = mbuild.ir_transceiver.receive_remote_code(1)
  
    if received_code:
        if received_code == [0, IR_CODE_A]:
            cyberpi.led.on(250, 0, 0, "all")
