import cyberpi

sound_effect = ["hello","hi","bye","yeah","wow","laugh","hum","sad","sigh","annoyed","angry","surprised","yummy","curious","embarrassed","ready","sprint","sleepy","meow","start","switch","beeps","buzzing","explosion","jump","laser","level-up","low-energy","prompt-tone","right","wrong","ring","score","wake","warning","metal-clash","shot","glass-clink","inflator","running water","clockwork","click","current","switch","wood-hit","iron","drop","bubble","wave","magic","spitfire","heartbeat","load"]

cyberpi.display.show_label('UP  :GO   UP\nDOWN:GO   DOWN\nMID :PLAY EFFECT', 16, 0, 0, 0)
cyberpi.display.show_label('SELECT:\nName:', 16, 0, 60, 1)

selected = 0
min_effect = 0
max_effect = len(sound_effect) - 1

while True:
    if cyberpi.controller.is_press('up'):
        if selected < max_effect:
            selected += 1
        else:
            selected = min_effect
    elif cyberpi.controller.is_press('down'):
        if selected > min_effect:
            selected -= 1
        else:
            selected = max_effect
    elif cyberpi.controller.is_press('middle'):
        cyberpi.led.on(255,0,0,id="all")
        cyberpi.audio.play_until(sound_effect[selected])
        cyberpi.led.on(0,0,0,id="all")

    cyberpi.display.show_label('{}'.format(selected), 16, 60, 60, 2)
    cyberpi.display.show_label('{}'.format(sound_effect[selected]), 12, 52, 80, 3)
