import serial
import subprocess
import winsound
import time
import win32api, win32con

# Open serial port (match baud rate 9600)
ser = serial.Serial('COM3', 9600, timeout=2)
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
        elif key == 'A':
            x = win32api.MapVirtualKey(win32con.VK_MEDIA_PREV_TRACK,0) # Previous track
            win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK,x)
        elif key == 'B':
            x = win32api.MapVirtualKey(win32con.VK_MEDIA_PLAY_PAUSE,0) # Play/Pause
            win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE,x)
        elif key == 'C':
            x = win32api.MapVirtualKey(win32con.VK_VOLUME_MUTE,0) # Mute/Unmute
            win32api.keybd_event(win32con.VK_VOLUME_MUTE,x)
        elif key == 'D':
            x = win32api.MapVirtualKey(win32con.VK_MEDIA_NEXT_TRACK,0) # Next track
            win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK,x)
