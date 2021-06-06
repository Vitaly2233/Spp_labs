import os
from tkinter import *

global currentPath
global folder
global previousData
currentPath = "E://"
folder = [""]


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


def changePath():
    # clearing
    directoryFiles.delete(1, "end")
    lblDirectory.configure(text=currentPath)
    # adding files to list box from currentPath
    pathVal = os.listdir(currentPath)
    counter = 1
    for x in pathVal:
        directoryFiles.insert(counter, x)
        counter += 1


def showCurrent():
    global currentPath
    lblDirectory.configure(text=currentPath)
    directoryFiles.insert(0, "------back------")
    changePath()


def newFolder(folderName):
    newFolder = folderName.get()
    path = os.path.join(currentPath, newFolder)
    try:
        os.mkdir(path)
    except:
        print("can't create a file")


def deleteFolder(deleteFile):
    file = deleteFile.get()
    path = os.path.join(currentPath, file)
    try:
        os.remove(path)
    except:
        print("can't remove a file")


def noDot(checker):
    list(checker)
    counter = 0
    for x in checker:
        if x == ".":
            counter += 1
    print(counter)
    if counter < 0:
        return True
    else:
        return False


def clickingItem(event):
    global currentPath
    global folder
    listToString(currentPath)
    selection = event.widget.curselection()
    index = selection[0]
    data = event.widget.get(index)
    try:
        if data != "------back------":
            currentPath += data + "/"
            folder.append(data)
            changePath()
        else:
            currentPath = currentPath.replace(folder.pop() + "/", "")
            showCurrent()
    except ValueError:
        print("error")
        currentPath = currentPath.replace(folder.pop() + "/", "")
        showCurrent()


window = Tk()
window.title("Commander")
window.geometry("500x400")
lblDirectory = Label(window, text="You're in " + currentPath)
lblDirectory.grid(column=0, row=1)
btnShow = Button(window, text="Show directory", command=showCurrent)
btnShow.grid(column=0, row=0)
directoryFiles = Listbox()
directoryFiles.grid(column=0, row=2)
folderName = StringVar()
fileName = StringVar()
btnNewFolder = Button(window, text="new Folder", command=lambda: newFolder(folderName))
input = Entry(window, textvariable=folderName).grid(column=0, row=3)
btnRemoveFile = Button(
    window, text="delete file", command=lambda: deleteFolder(fileName)
).grid(column=1, row=4)
deleteFileInput = Entry(window, textvariable=fileName).grid(column=0, row=4)
btnNewFolder.grid(column=1, row=3)
directoryFiles.bind("<<ListboxSelect>>", clickingItem)

window.mainloop()
