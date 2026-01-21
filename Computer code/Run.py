import serial
import time
import Comp_MonoBoard
import Comp_DynaBoard

ser = serial.Serial('COM3', 9600, timeout=2)
time.sleep(2)  # Wait for Arduino reset after opening por
Mode = 0

def BoardMode(mode):
    if mode == 0:
        print("MonoBoard mode activated.")
    elif mode == 1:
        print("DynaBoard mode activated.")


while True:
    if ser.in_waiting > 0:
        key = ser.readline().decode('utf-8').strip()
        
        Comp_MonoBoard.MonoBoard(key)
