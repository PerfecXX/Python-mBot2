import cyberpi, mbuild

# 16 digits = every 2 digit is 1 line in hexdecimal format. 
# Each hexdecimal represents 4 bits of data in each line.
mbuild.led_panel.show_image("00003c7e7e3c000000003c7e7e3c0000", time_s = 5, index = 1)

