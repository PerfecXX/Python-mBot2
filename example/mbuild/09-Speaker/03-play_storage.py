import cyberpi, mbuild

mbuild.speaker.set_volume(100, 1)

# your file name in speaker storage must be 4 digit
mbuild.speaker.play_melody("0001", 1)
# your file name in speaker storage must be 4 digit
mbuild.speaker.play_melody_until_done('0002', 1)

mbuild.speaker.stop_sounds(1)
