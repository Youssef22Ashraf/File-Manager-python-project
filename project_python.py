from tkinter import *  #for gui
import shutil  #to deals with files       
import os # to facilitate dealing with os and the program
import easygui # for select file from the system  
from tkinter import filedialog # folder selection 
from tkinter import messagebox as mb #read files
############################################################################## 
# opening window for select file to do the command
def open_window():
    read=easygui.fileopenbox()
    return read
#opening the choosing file 
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!") 
#searching file to copy
def copy_file():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('confirmation', "File Copied !")
#choosing file to delete    
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)             
    else:
        mb.showinfo('confirmation', "File not found !")
#take file and renaming it with a new one
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName+extension)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")
#change the file path to a new one (taking file to another folder)
def move_file():
    source = open_window()
    destination =filedialog.askdirectory()
    try:  
        shutil.move(source, destination)  
        mb.showinfo('confirmation', "File Moved !")
    except:
        mb.showinfo('confirmation', "you made a mistake the Source and destination are same so try again")
#creating new folder and put the folder's path
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")
# delete selected folder
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted !")
#############################################################################
def open_mainW():
    root = Tk(className='File Manger')
    root['background']='#93291E'
    root.geometry("400x400")
    titel=Label(root, text="File Manger", font=("Helvetica", 16), fg="#ED213A")
    titel.place(anchor=CENTER,relx=.5,rely=.1)
    FirstB=Button(root, text = "Open a File", command = open_file)
    FirstB.place(anchor=CENTER,relx=.5,rely=.2)
    soucandB=Button(root, text = "Copy a File", command = copy_file)
    soucandB.place(anchor=CENTER,relx=.5,rely=.3)
    therB=Button(root, text = "Delete a File", command = delete_file)
    therB.place(anchor=CENTER,relx=.5,rely=.4)
    fothB=Button(root, text = "Rename a File", command = rename_file)
    fothB.place(anchor=CENTER,relx=.5,rely=.5)
    fithB=Button(root, text = "Move a File", command = move_file)
    fithB.place(anchor=CENTER,relx=.5,rely=.6)
    sixthB=Button(root, text = "Make a Folder", command = make_folder)
    sixthB.place(anchor=CENTER,relx=.5,rely=.7)
    sevthB=Button(root, text = "Remove a Folder", command = remove_folder)
    sevthB.place(anchor=CENTER,relx=.5,rely=.8)
    soucandB=Button(root, text = "Exit",command=root.destroy)
    soucandB.place(anchor=CENTER,relx=.5,rely=.9)
    root.mainloop()
####################################################################################
root2 = Tk(className="Welcome to File Manger")
root2['background']='#93291E'
root2.geometry("350x350")
titel=Label(root2, text="WELCOME TO FILE MANAGER", font=("Helvetica", 16), fg="#ED213A")
titel.place(anchor=CENTER,relx=.5,rely=.1)
startB=Button(root2, text = "Start",command=lambda:[root2.destroy(),open_mainW()])
startB.place(anchor=CENTER,relx=.5,rely=.4)
soucandB=Button(root2, text = "Exit",command=root2.destroy)
soucandB.place(anchor=CENTER,relx=.5,rely=.7)
root2.mainloop()
#######################################################################################