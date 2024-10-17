import cyberpi

cyberpi.audio.set_vol(100)
# int note (0-132)
# float beat > 0 (second)
cyberpi.audio.play_music(note=53,beat=0.5)
cyberpi.audio.play_music(note=65,beat=0.5)
