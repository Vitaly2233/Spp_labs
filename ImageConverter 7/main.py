import numpy as np
from PIL import Image
import cv2 as cv
from matplotlib import pyplot as plt

image = Image.open("monster.png")

image_sequence = image.getdata()
image_array = np.array(image_sequence)

print(image_array[0])

print(
    "Что вы хотеите сделать с картинкой? 1 - пропорционально уменьшить размер(в сколько раз), 2 - вывести график цветов"
)
choise = int(input())

if choise == 1:
    print("в скольок раз уменьшить размер")
    cuttedTimes: int = int(input())
    newSize = (image.size[0] / cuttedTimes, image.size[1] / cuttedTimes)
    image.thumbnail(newSize)
    image.save("cutted" + str(cuttedTimes) + "times.png")
elif choise == 2:
    img = cv.imread("monster.png")
    color = ("b", "g", "r")
    qtdBlue = 0
    qtdGreen = 0
    qtdRed = 0
    totalPixels = 0

    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
        totalPixels += sum(histr)
        if i == 0:
            qtdBlue = sum(histr)
        elif i == 1:
            qtdGreen = sum(histr)
        elif i == 2:
            qtdRed = sum(histr)
    print("Red Quantity")
    print(qtdRed)

    print("Blue Quantity")
    print(qtdBlue)

    print("Green Quantity")
    print(qtdGreen)

    plt.show()
