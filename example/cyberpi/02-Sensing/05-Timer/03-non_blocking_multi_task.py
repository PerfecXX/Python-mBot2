import cyberpi

led_red_duration = 0.5
led_red_is_on = False
led_red_last_toggle_time = 0

led_green_duration = 1
led_green_is_on = False
led_green_last_toggle_time = 0

led_blue_duration = 2
led_blue_is_on = False
led_blue_last_toggle_time = 0

cyberpi.timer.reset()

while True:
    current_time = cyberpi.timer.get()

    if current_time - led_red_last_toggle_time >= led_red_duration:
        led_red_is_on = not led_red_is_on
        led_red_last_toggle_time = current_time
    if led_red_is_on:
        cyberpi.led.on(255, 0, 0, id=2)
    else:
        cyberpi.led.on(0, 0, 0, id=2)

    if current_time - led_green_last_toggle_time >= led_green_duration:
        led_green_is_on = not led_green_is_on
        led_green_last_toggle_time = current_time
    if led_green_is_on:
        cyberpi.led.on(0, 255, 0, id=3)
    else:
        cyberpi.led.on(0, 0, 0, id=3)

    if current_time - led_blue_last_toggle_time >= led_blue_duration:
        led_blue_is_on = not led_blue_is_on
        led_blue_last_toggle_time = current_time
    if led_blue_is_on:
        cyberpi.led.on(0, 0, 255, id=4)
    else:
        cyberpi.led.on(0, 0, 0, id=4)
            
    cyberpi.display.show_label(current_time, 12, 0, 0, index=0)
