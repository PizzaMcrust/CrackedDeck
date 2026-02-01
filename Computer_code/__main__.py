import serial
import time
import Comp_MonoBoard
import Comp_NumBoard

ser = serial.Serial('COM3', 9600, timeout=3)  # Adjust 'COM3' to your Arduino's port
time.sleep(1)  # Wait for Arduino reset after opening port

##Board mode selection

int Mode

if Mode == 0:
    print("MonoBoard mode selected")
else:
    print("NumBoard mode selected")

while True:
    if ser.in_waiting > 0:
        key = ser.readline().decode('utf-8').strip()
        if Mode == 0:
            Comp_MonoBoard.MonoBoard(key)
            print("Using MonoBoard")
        elif Mode == 1:
            Comp_NumBoard.NumBoard(key)
            print("Using NumBoard")