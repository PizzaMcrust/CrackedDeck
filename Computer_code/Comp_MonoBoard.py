import subprocess
import winsound
import win32api, win32con
from Functions import AudioPlay # Ensure AudioPlay is imported to initialize pyaudio
# Open serial port (match baud rate 9600)
print("Listening for keypad presses...")

def MonoBoard(x):
    import __main__
    print("MonoBoard Key Pressed:", x)
    if x == 48: # '0' key
        pass # Placeholder for future functionality
    elif x == 49:# '1' key
        subprocess.Popen(['C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'])  # Opens Brave Browser
    elif x == 50: # '2' key
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)  # Plays Windows ding sound
    elif x == 51: # '3' key
        AudioPlay.playsound('Media\\AHH.mp3') # Plays a custom sound file
    elif x == 52: # '4' key
        pass # Placeholder for future functionality
    elif x == 53: # '5' key
        pass # Placeholder for future functionality
    elif x == 54: # '6' key
        x = win32api.MapVirtualKey(win32con.VK_VOLUME_UP,0) # Volume Up
        win32api.keybd_event(win32con.VK_VOLUME_UP,x)
    elif x == 55: # '7' key
        pass # Placeholder for future functionality
    elif x == 56: # '8' key
        pass # Placeholder for future functionality
    elif x == 57: # '9' key
        x = win32api.MapVirtualKey(win32con.VK_VOLUME_DOWN,0) # Volume Down
        win32api.keybd_event(win32con.VK_VOLUME_DOWN,x)
    elif x == 65: # 'A' key
        x = win32api.MapVirtualKey(win32con.VK_MEDIA_PREV_TRACK,0) # Previous track
        win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK,x)
    elif x == 66: # 'B' key
        x = win32api.MapVirtualKey(win32con.VK_MEDIA_PLAY_PAUSE,0) # Play/Pause
        win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE,x)
    elif x == 67: # 'C' key
        x = win32api.MapVirtualKey(win32con.VK_VOLUME_MUTE,0) # Mute/Unmute
        win32api.keybd_event(win32con.VK_VOLUME_MUTE,x)
    elif x == 68: # 'D' key
        x = win32api.MapVirtualKey(win32con.VK_MEDIA_NEXT_TRACK,0) # Next track
        win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK,x)
    elif x == 35:
        # Alt + F4
        win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)      # Press Alt
        win32api.keybd_event(win32con.VK_F4, 0, 0, 0)        # Press F4
        win32api.keybd_event(win32con.VK_F4, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release F4
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0) # Release Alt
    elif x == 42:  # ASCII for '*'
        __main__.Mode = 1
        # Switch to NumBoard mode