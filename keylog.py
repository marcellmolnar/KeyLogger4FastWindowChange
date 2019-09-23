# -*- coding: cp1250 -*-
import pynput.keyboard as kb
from pynput.keyboard import Key, Listener, Key
from datetime import datetime
import win32gui

muteSound = True

windowToOpen = "MATLAB R2018b - academic use"
windowToOpen = "Gyorshívó - Opera"
windowToOpen = "*new 1 - Notepad++"

keyboard = kb.Controller()

lastPressed = datetime.now()
def on_press(key):
    global lastPressed, windowToOpen
    print key
    if (str(key) == 'Key.space'):
        tnow = datetime  .now()        
        if (tnow-lastPressed).microseconds < 200000:
            hwnd = win32gui.FindWindow(None, windowToOpen)
            win32gui.ShowWindow(hwnd, 9)
            keyboard.press(kb.KeyCode(vk=173))
            #with keyboard.pressed(Key.alt_l):
            #    keyboard.press(Key.f4)
        lastPressed = tnow
        
listener = Listener(on_press=on_press)
listener.start()
listener.join()

def __del__(self):
    listener.stop()
