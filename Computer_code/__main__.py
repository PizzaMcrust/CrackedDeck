import serial
from collections import deque
import time
import Functions.micCode as micCode
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust 'COM3' to your Arduino's port
audio_buffer = deque(maxlen=500)
time.sleep(2)  # Wait for Arduino reset after opening port

##Board mode selection

Mode = 0

if Mode == 0:
    print("MonoBoard mode selected")
else:
    print("NumBoard mode selected")


while True:
    
    tag_byte = ser.read(1)
    if not tag_byte:
        continue
    tag = tag_byte[0]

    # ---------- AUDIO ----------
    if tag == 0xAA:

        # Ignore mic when in NumBoard mode
        if Mode == 1:
            ser.read(1)   # discard audio byte
            continue

        audio_byte = ser.read(1)
        if not audio_byte:
            continue
        audio = audio_byte[0]

        # optional debug
        #print("Audio:", audio) if audio > 25 and audio < 40 else None  # or send to sound output

    # ---------- KEYS ----------
    elif tag == 0xBB:
        key_byte = ser.read(1)
        if not key_byte:
            continue
        key = key_byte[0]

        key_char = chr(key)

        if Mode == 0:
            import Comp_MonoBoard
            Comp_MonoBoard.MonoBoard(key)

        elif    Mode == 1:
            import Comp_NumBoard
            Comp_NumBoard.NumBoard(key)

