import ctypes
from infi.systray import SysTrayIcon


def turnOffKeyboard(systray):
    ctypes.windll.user32.BlockInput(True)


def turnOnKeyboard(systray):
    ctypes.windll.user32.BlockInput(False)


menu_options = (
    ("turn Off Keyboard", None, turnOffKeyboard),
    ("turn on Keyboard", None, turnOnKeyboard),
)
systray = SysTrayIcon("E://image.ico", "Example tray icon", menu_options)
systray.start()
