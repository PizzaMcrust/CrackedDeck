import serial
from collections import deque
import time
import Comp_MonoBoard
import Comp_NumBoard
import Computer_code.Functions.micCode as micCode

ser = serial.Serial('COM3', 115200, timeout=2)  # Adjust 'COM3' to your Arduino's port
audio_buffer = deque(maxlen=500)
time.sleep(2)  # Wait for Arduino reset after opening port

##Board mode selection

Mode = 0

if Mode == 0:
    print("MonoBoard mode selected")
else:
    print("NumBoard mode selected")

while True:
    tag = ser.read(1)
    if not tag:
        continue
    tag = tag[0]

    if tag == 0xAA:
        audio = ser.read(1)[0]
        if audio > 25:
            print("Audio:", audio)  # or send to sound output
    elif tag == 0xBB:
        key = ser.read(1)[0]
        if Mode == 0:
            Comp_MonoBoard.MonoBoard(key)
        else:
            Comp_NumBoard.NumBoard(key)
        print(key)