import cyberpi, mbuild

while True:
      #              volume level 0-100
      mbuild.speaker.set_volume(100, 1)
      #              note tempo
      mbuild.speaker.speed[1 - 1] = 60
      
      #                 Note Freq, Time, Index
      mbuild.speaker.play_tone(65, 0.25, 1)
      mbuild.speaker.play_tone(110, 0.25, 1)
      mbuild.speaker.play_tone(700, index=1)
