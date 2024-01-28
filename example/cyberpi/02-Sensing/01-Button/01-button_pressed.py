import cyberpi

"""
Button Name List (str)

a , b 
up, down, left , right , middle
any_direction , any_button , any

"""
while True:
                             # button name
    if cyberpi.controller.is_press('a'):
        cyberpi.led.on(255,0,0,id='all')
        cyberpi.console.println("LED ON!")
    if cyberpi.controller.is_press('b'):
        cyberpi.led.on(0,0,0,id='all')
        cyberpi.console.println("LED OFF!")
