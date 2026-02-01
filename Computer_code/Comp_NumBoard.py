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
    print(f"Key pressed: {x}")       

    # Simulate key presses based on NumBoard input similar to a Numpad
    if x == '1':
        keyboard.press('1')
    elif x == '2':
        keyboard.press('2')
    elif x == '3':
        keyboard.press('3')
    elif x == '4':
        keyboard.press('4')
    elif x == '5':
        keyboard.press('5')
    elif x == '6':
        keyboard.press('6') 
    elif x == '7':
        keyboard.press('7')
    elif x == '8':
        keyboard.press('8')
    elif x == '9':
        keyboard.press('9')
    elif x == '0':
        keyboard.press('0')
    elif x == 'A':
        keyboard.press('+')
    elif x == 'B':
        keyboard.press('-')
    elif x == 'C':
        keyboard.press('*')
    elif x == 'D':
        keyboard.press('/')
    elif x == '#':
        x = win32api.MapVirtualKey(win32con.VK_RETURN,0) # Enter key
        win32api.keybd_event(win32con.VK_RETURN,x)
    elif x == '*':
        __main__.Mode = 0