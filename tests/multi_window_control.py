from win32con import *
from win32gui import *
from win32api import *
import time
target_hwnds = []
def print_next_title(hwnd, _extra):
    print(GetWindowText(hwnd))
def add_next_hwnd(hwnd, _extra):
    if GetWindowText(hwnd) == "Minecraft 1.8.9":
        EnumChildWindows(hwnd, print_next_title, None)
        target_hwnds.append(hwnd)
EnumWindows(add_next_hwnd, None)
while True:
    for hwnd in target_hwnds:
        SetForegroundWindow(hwnd)
        keybd_event(0x57, 0, 0, 0)
        keybd_event(0x57, 0, 0, KEYEVENTF_KEYUP)
        time.sleep(0.05)