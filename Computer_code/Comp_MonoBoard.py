import subprocess
import winsound
import win32api, win32con
#from Computer_code.Functions import AudioPlay # Ensure AudioPlay is imported to initialize pyaudio

# Open serial port (match baud rate 9600)
print("Listening for keypad presses...")

def MonoBoard(x):
    print(f"Key pressed: {x}")        
    if x == '1':
        subprocess.Popen(['notepad.exe'])  # Opens Notepad
    elif x == '2':
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)  # Plays Windows ding sound
    elif x == '3':
        #AudioPlay.play_sound("alert.wav")  # Plays a custom sound file
        pass
    elif x == 'A':
        x = win32api.MapVirtualKey(win32con.VK_MEDIA_PREV_TRACK,0) # Previous track
        win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK,x)
    elif x == 'B':
        x = win32api.MapVirtualKey(win32con.VK_MEDIA_PLAY_PAUSE,0) # Play/Pause
        win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE,x)
    elif x == 'C':
        x = win32api.MapVirtualKey(win32con.VK_VOLUME_MUTE,0) # Mute/Unmute
        win32api.keybd_event(win32con.VK_VOLUME_MUTE,x)
    elif x == 'D':
        x = win32api.MapVirtualKey(win32con.VK_MEDIA_NEXT_TRACK,0) # Next track
        win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK,x)
    elif x == '#':
        x = win32api.MapVirtualKey(win32con.VK_UP,0) # Next track
        win32api.keybd_event(win32con.VK_UP,x)
    elif x == '*':
        x = win32api.MapVirtualKey(win32con.VK_DOWN,0) # Next track
        win32api.keybd_event(win32con.VK_DOWN,x)