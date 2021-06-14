import ctypes
import os
from infi.systray import SysTrayIcon
from time import sleep
from threading import Timer


def turnOffKeyboard(systray):
    print('введите время через сколько выключить клавиатуру:')
    s = int(input("Введите колличество секунд: "))
    m = int(input("Введите колличество минут: "))
    h = int(input("Введите колличество часов: "))

    genTime = s + m * 60 + h * 3600

    print('введите время через сколько включить клавиатуру:')
    s = int(input("Введите колличество секунд: "))
    m = int(input("Введите колличество минут: "))
    h = int(input("Введите колличество часов: "))

    genTimee = s + m * 60 + h * 3600

    sleep(genTime)
    ctypes.windll.user32.BlockInput(True)
    sleep(genTimee)
    ctypes.windll.user32.BlockInput(False)


def turnOnKeyboard(systray):
    ctypes.windll.user32.BlockInput(False)


def turnOffComputer(systray):
    print('введите время через сколько хотите выключить компютер:')
    s = int(input("Введите колличество секунд: "))
    m = int(input("Введите колличество минут: "))
    h = int(input("Введите колличество часов: "))

    genTime = s + m * 60 + h * 3600
    os.system("shutdown /s /t " + str(genTime))


def cancelTurningOff(systray):
    os.system("shutdown -a")


menu_options = (
    ("turn Off Keyboard", None, turnOffKeyboard),
    ("turn on Keyboard", None, turnOnKeyboard),
    ("turn off computer", None, turnOffComputer),
    ("cancel turning off", None, cancelTurningOff),

)
systray = SysTrayIcon("E://image.ico", "Example tray icon", menu_options)
systray.start()
