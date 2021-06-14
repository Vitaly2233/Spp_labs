# imports
import os
import ctypes
from infi.systray import SysTrayIcon


# functions
def cls():
    os.system("cls" if os.name == "nt" else "clear")


def disable(time):
    os.system("shutdown /s /t " + time)


def reload(time):
    os.system("shutdown/r /t " + time)


def cancelShutdown():
    os.system("shutdown -a")


def turnOffKeyboard(time):
    ctypes.windll.user32.BlockInput(True)


# code
while True:

    print("--Вы хотите выключить или перезагрузить компютер--")
    choise = input(
        "Если выключить введите 1, а если перезагрузить нажмите 2, отменить действие \"-\", выключить клавиатуру и мышку 3, завершить программу 4: "
    )
    if choise == "-":
        cancelShutdown()
        continue

    if choise == '4':
        break
    s = int(input("Введите колличество секунд: "))
    m = int(input("Введите колличество минут: "))
    h = int(input("Введите колличество часов: "))

    genTime = s + m * 60 + h * 3600
    if choise == "1":
        disable(str(genTime))
    elif choise == "2":
        reload(str(genTime))
    elif choise == "3":
        turnOffKeyboard()

    print("Если хотите отменить действие напишите '-'")
