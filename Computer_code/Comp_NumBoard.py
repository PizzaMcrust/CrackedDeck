import subprocess
import winsound
import win32api, win32con
from Functions import AudioPlay # Ensure AudioPlay is imported to initialize pyaudio
from pynput import keyboard

# Open serial port (match baud rate 9600)
print("Listening for keypad presses...")

keyboard = keyboard.Controller()

def NumBoard(x):
    import __main__
    print("NumBoard Key Pressed:", x)    

    # Simulate key presses based on NumBoard input similar to a Numpad
    if x == 49:
        keyboard.press('1')
    elif x == 50:
        keyboard.press('2')
    elif x == 51:
        keyboard.press('3')
    elif x == 52:
        keyboard.press('4')
    elif x == 53:
        keyboard.press('5')
    elif x == 54:
        keyboard.press('6') 
    elif x == 55:
        keyboard.press('7')
    elif x == 56:
        keyboard.press('8')
    elif x == 57:
        keyboard.press('9')
    elif x == 48:
        keyboard.press('0')
    elif x == 65:
        keyboard.press('+')
    elif x == 66:
        keyboard.press('-')
    elif x == 67:
        keyboard.press('*')
    elif x == 68:
        keyboard.press('/')
    elif x == 35:
        x = win32api.MapVirtualKey(win32con.VK_RETURN,0) # Enter key
        win32api.keybd_event(win32con.VK_RETURN,x)
    elif x == 42:
        __main__.Mode = 0