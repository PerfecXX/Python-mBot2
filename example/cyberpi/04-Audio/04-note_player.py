import cyberpi

notes_dict = {
    0: "C-1", 1: "C#-1", 2: "D-1", 3: "D#-1", 4: "E-1", 5: "F-1", 6: "F#-1",
    7: "G-1", 8: "G#-1", 9: "A-1", 10: "A#-1", 11: "B-1", 12: "C0", 13: "C#0",
    14: "D0", 15: "D#0", 16: "E0", 17: "F0", 18: "F#0", 19: "G0", 20: "G#0",
    21: "A0", 22: "A#0", 23: "B0", 24: "C1", 25: "C#1", 26: "D1", 27: "D#1",
    28: "E1", 29: "F1", 30: "F#1", 31: "G1", 32: "G#1", 33: "A1", 34: "A#1",
    35: "B1", 36: "C2", 37: "C#2", 38: "D2", 39: "D#2", 40: "E2", 41: "F2",
    42: "F#2", 43: "G2", 44: "G#2", 45: "A2", 46: "A#2", 47: "B2", 48: "C3",
    49: "C#3", 50: "D3", 51: "D#3", 52: "E3", 53: "F3", 54: "F#3", 55: "G3",
    56: "G#3", 57: "A3", 58: "A#3", 59: "B3", 60: "C4", 61: "C#4", 62: "D4",
    63: "D#4", 64: "E4", 65: "F4", 66: "F#4", 67: "G4", 68: "G#4", 69: "A4",
    70: "A#4", 71: "B4", 72: "C5", 73: "C#5", 74: "D5", 75: "D#5", 76: "E5",
    77: "F5", 78: "F#5", 79: "G5", 80: "G#5", 81: "A5", 82: "A#5", 83: "B5",
    84: "C6", 85: "C#6", 86: "D6", 87: "D#6", 88: "E6", 89: "F6", 90: "F#6",
    91: "G6", 92: "G#6", 93: "A6", 94: "A#6", 95: "B6", 96: "C7", 97: "C#7",
    98: "D7", 99: "D#7", 100: "E7", 101: "F7", 102: "F#7", 103: "G7", 104: "G#7",
    105: "A7", 106: "A#7", 107: "B7", 108: "C8", 109: "C#8", 110: "D8", 111: "D#8",
    112: "E8", 113: "F8", 114: "F#8", 115: "G8", 116: "G#8", 117: "A8", 118: "A#8",
    119: "B8", 120: "C9", 121: "C#9", 122: "D9", 123: "D#9", 124: "E9", 125: "F9",
    126: "F#9", 127: "G9", 128: "G#9", 129: "A9", 130: "A#9", 131: "B9",
}

notes = list(notes_dict.keys())

cyberpi.display.show_label('UP  :GO   UP\nDOWN:GO   DOWN\nMID :PLAY NOTE', 16, 0, 0, 0)
cyberpi.display.show_label('SELECT:\nNote:', 16, 0, 60, 1)

selected = 0
min_note = 0
max_note = len(notes) - 1

while True:
    if cyberpi.controller.is_press('up'):
        if selected < max_note:
            selected += 1
        else:
            selected = min_note
    elif cyberpi.controller.is_press('down'):
        if selected > min_note:
            selected -= 1
        else:
            selected = max_note
    elif cyberpi.controller.is_press('middle'):
        cyberpi.led.on(255, 0, 0, id="all")
      
        cyberpi.audio.play_music(note=notes[selected], beat=1, type="piano")
        cyberpi.led.on(0, 0, 0, id="all")


    cyberpi.display.show_label('{}'.format(selected), 16, 60, 60, 2)
    cyberpi.display.show_label('Note: {}'.format(notes_dict[notes[selected]]), 12, 52, 80, 3)
