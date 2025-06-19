import cyberpi
#                              (a,b or any_button)
cyberpi.controller.reset_count('any_button')

while True:
    btn_a_count = cyberpi.controller.get_count('a')
    btn_b_count = cyberpi.controller.get_count('b')
    
    cyberpi.display.show_label("Button A : {}".format(btn_a_count),12,0,0,index=0)
    cyberpi.display.show_label("Button B : {}".format(btn_b_count),12,0,16,index=1)
    
    if cyberpi.controller.is_press("middle"):
        cyberpi.controller.reset_count('any_button')
