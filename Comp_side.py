import serial
import subprocess
import winsound
import time
import os

# Open serial port (match baud rate 9600)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino reset after opening port
print("Listening for keypad presses...")

while True:
    if ser.in_waiting > 0:
        key = ser.readline().decode('utf-8').strip()
        print(f"Key pressed: {key}")
        
        if key == '1':
            subprocess.Popen(['notepad.exe'])  # Opens Notepad
        elif key == '2':
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)  # Plays Windows ding sound
        elif key == 'C':
            os.system("shutdown /s /t 5")  # Example: Shutdown in 5s (use cautiously!)
        elif key == 'A':
            subprocess.Popen(r'C:\Path\To\YourApp.exe')  # Custom app
        # Add more: elif key == '5': play_mp3() etc.