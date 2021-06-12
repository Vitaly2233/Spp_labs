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


def renameFile(fileName, newFileName):
    file = fileName.get()
    newFile = newFileName.get()
    newNameFile = os.path.join(currentPath, newFile)
    path = os.path.join(currentPath, file)
    try:
        os.rename(path, newNameFile)
    except:
        print("can't rename the file")


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

# vars
directoryFiles = Listbox()
folderName = StringVar()
deletFileName = StringVar()
fileName = StringVar()
newFileName = StringVar()

# buttons
btnShow = Button(window, text="Show directory", command=showCurrent)
btnNewFolder = Button(window, text="new Folder",
                      command=lambda: newFolder(folderName))
btnRemoveFile = Button(
    window, text="delete file", command=lambda: deleteFolder(deletFileName)
)
btnRenameFile = Button(window, text='rename file',
                       command=lambda: renameFile(fileName, newFileName))


# input
input = Entry(window, textvariable=folderName)
deleteFileInput = Entry(
    window, textvariable=deletFileName)
directoryFiles.bind("<<ListboxSelect>>", clickingItem)
fileNameI = Entry(window, textvariable=fileName)
newFileNameI = Entry(window, textvariable=newFileName)

# grid
btnShow.grid(column=1, row=0)
lblDirectory.grid(column=0, row=1)
directoryFiles.grid(column=0, row=2)
input.grid(column=0, row=3)
btnNewFolder.grid(column=2, row=3)
deleteFileInput.grid(column=0, row=4)
btnRemoveFile.grid(column=2, row=4)
fileNameI.grid(column=0, row=5)
newFileNameI.grid(column=1, row=5)
btnRenameFile.grid(column=2, row=5)

# starting gui
window.mainloop()
