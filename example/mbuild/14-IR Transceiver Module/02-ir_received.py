import cyberpi, mbuild

while True:
  
    ir_message = mbuild.ir_transceiver.receive(1)
  
    cyberpi.display.show_label("Received:{}".format(ir_message), 12, 0, 0, index = 0)
