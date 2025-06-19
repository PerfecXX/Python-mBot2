import cyberpi, mbuild

mbuild.speaker.set_volume(20, 1)

# !101 to !120 is emotional sound effect
mbuild.speaker.play_melody_until_done('!101', 1)
# !201 to !223 is electronic sound effect
mbuild.speaker.play_melody_until_done('!201', 1)
# !301 to !329 is physical sound effect
mbuild.speaker.play_melody_until_done('!301', 1)
# !401 to !437 is Number and English alphabet
mbuild.speaker.play_melody_until_done('!401', 1)
# !501 to !545 is English word
mbuild.speaker.play_melody_until_done('!501', 1)
# !601 to !611 is Animal sound effect
mbuild.speaker.play_melody_until_done('!601', 1)
# !701 to !711 is transportation sound effect
mbuild.speaker.play_melody_until_done('!701', 1)
