from multi_window_control import get_hwnd
from win32con import *
from win32gui import *
from win32api import *
import time


def run():
     while True:
          SetForegroundWindow(get_hwnd(1))
          keybd_event(0x57, 0, 0, 0)
          keybd_event(0x57, 0, 0, KEYEVENTF_KEYUP)
          time.sleep(0.01)