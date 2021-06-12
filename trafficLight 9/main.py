lightOne = int(
    input("Введіть час горіння першого зеленого світла на світлофорі:")
)
lightTwo = int(
    input("Введіть час горіння другого зеленого світла на світлофорі:")
)
roadWidth = 4
lineFirst = int(input("Введіть кількість ліній на першій дорозі(1-2):"))
lineSecond = int(input("Введіть кількість ліній на другій дорозі(1-2):"))
numberOfCars = (
    (lightOne * 10 * roadWidth * lineSecond) / 100
) + ((lightTwo * 10 * roadWidth * lineFirst) / 100)
if lineFirst == 1:
    print("      ║  ^  ║")
    print("      ║  ^  ║")
    print("══════╝  ^  ╚══════")
    if lineSecond == 1:
        print(" > > >       > > >")
    if lineSecond == 2:
        print(" > > >       > > >")
        print(" > > >       > > >")
    print("══════╗  ^  ╔══════")
    print("      ║  ^  ║")
    print("      ║  ^  ║")
if lineFirst == 2:
    print("      ║  ^ ^  ║")
    print("      ║  ^ ^  ║")
    print("══════╝  ^ ^  ╚══════")
    if lineSecond == 1:
        print(" > > >         > > >")
    if lineSecond == 2:
        print(" > > >         > > >")
        print(" > > >         > > >")
    print("══════╗  ^ ^  ╔══════")
    print("      ║  ^ ^  ║")
    print("      ║  ^ ^  ║")

print(int(numberOfCars))
