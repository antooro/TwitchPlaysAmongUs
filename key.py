# For Windows
# http://stackoverflow.com/questions/1823762/sendkeys-for-python-3-1-on-windows
# https://stackoverflow.com/a/38888131

import win32api
import win32con
import win32gui
import time, sys
import pywinauto

keyDelay = 2.5
# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
keymap = {
    "up": win32con.VK_UP,
    "left": win32con.VK_LEFT,
    "down": win32con.VK_DOWN,
    "right": win32con.VK_RIGHT,
    "use": win32con.VK_SPACE, #use y sabotage
    "close": win32con.VK_ESCAPE, #salir de msion no se usa
    "map": win32con.VK_TAB, #mapa
    "rep": 0x52, # Reportar muerte
    "kill": 0x51, # Matar
    "stop": "stop"
}
def clearkeys():
    win32api.keybd_event(win32con.VK_RIGHT, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_DOWN, 0, win32con.KEYEVENTF_KEYUP, 0)

# this way has to keep window in focus
def sendKey(button):
    
    if button[-1].isdigit():
        keyDelay = int(button[-1])*.25
        button = button[:-1]

    win32api.keybd_event(keymap[button], 0, 0, 0)
    time.sleep(keyDelay)
    keyDelay = 0.1
    win32api.keybd_event(keymap[button], 0, win32con.KEYEVENTF_KEYUP, 0)

def SimpleWindowCheck(windowname):
    window = None
    print(windowName, "windowname")
    try:
        window = win32gui.FindWindow(windowName, None)
    except win32gui.error:
        try: 
            window = win32gui.FindWindow(None, windowName)
        except win32gui.error:
           
            return False
        else:
            return window
    else:
        return window

if __name__ == "__main__":
    print("Inicio de programa")
    windowName = " ".join(sys.argv[1:-1])
    key = sys.argv[-1]


    winId = SimpleWindowCheck(windowName)
    # winId = None

    if not (winId):
        windowList = []
        
        def enumHandler(hwnd, list):
            if windowName in win32gui.GetWindowText(hwnd):
                list.append(hwnd)
        
        win32gui.EnumWindows(enumHandler, windowList)
        # only the first id, may need to try the others
        winId = windowList[0]

        # can check with this
        for hwnd in windowList:
            hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
            
    win32gui.ShowWindow(winId, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(winId)
    sendKey(key)