import cyberpi

BLINK_DURATION = 3 
is_led_on = False
last_state_change_time = 0

cyberpi.timer.reset()

while True:
    
    current_time = cyberpi.timer.get()

    if current_time - last_state_change_time >= BLINK_DURATION:
        is_led_on = not is_led_on 
        last_state_change_time = current_time 
        
    if is_led_on:
        cyberpi.led.on(255, 0, 0, id="all")
    else:
        cyberpi.led.on(0, 0, 0, id="all")
        
    cyberpi.display.show_label(current_time, 12, 0, 0, index=0)
