import sys

from infi.systray import SysTrayIcon
import ctypes
from ctypes import wintypes
import time



# def turnOffKeyboard(systray):
#
#
#
# def turnOnKeyboard(systray):
# 	print('value')




# menu_options = (("turn Off Keyboard", None, turnOffKeyboard), ("turn on Keyboard", None, turnOnKeyboard))
# systray = SysTrayIcon("E://image.ico", "Example tray icon", menu_options)
# systray.start()

import ctypes
from ctypes import wintypes

BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL

blocked = BlockInput(True)
if blocked:
    try:
        pass # do something
    finally:
        unblocked = BlockInput(False) # unblock in any case
else:
    raise RuntimeError('Input is already blocked by another thread!')