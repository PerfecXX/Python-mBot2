import cyberpi

cyberpi.audio.set_vol(100)
# str type eg. snare,bass-drum,side-stick,crash-cymbal,open-hi-hat,close-hi-hat,tambourine,hand-clap,claves 
# float beat > 0 (second)

cyberpi.audio.play_drum("snare",1)
cyberpi.audio.play_drum("snare",1)
cyberpi.audio.play_drum("side-stick",1)
cyberpi.audio.play_drum("tambourine",1)
