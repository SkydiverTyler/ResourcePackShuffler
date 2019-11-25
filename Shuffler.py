# IF YOU SEE THIS, AND YOU ARE TRYING TO RUN THE SHUFFLER,
# PLEASE OPEN THE "README.MD" FILE IN A TEXT EDITOR
# FOR HELP

# Credits
    # Made by Tyler Jones (SkydiverTyler)
    # https://twitter.com/skydivertyler
    # Please credit me, and link to the github project,
    # if you use this in a YouTube video,
    # or if you redistribute this program.
    # This project is provided as-is without warranty.

# Imports
import os
from os.path import expanduser
import subprocess
import zipfile
from tkinter import *

# Define variables
boolShowGUI = False
boolAllowEmptyTextures = False
dirHere = os.getcwd() # current location of this python script
dirSrc = "C:/Users/skydi/Desktop/Code/_testfolder" # location of the source resource packs
dirDest = os.path.join(dirSrc,"Shuffled Packs") # where the shuffled packs will be placed
dirTemp = os.path.join(dirSrc,"Temp") # temp directory
intPackFormat = 5

# Create folders if they don't already exist
try:
    os.mkdir(dirFrom + "/" + dirDest)
except:
    print("Path [" + dirDest + "] already exists")

try:
    os.mkdir(dirFrom + "/" + dirTemp)
except:
    print("Path [" + dirTemp + "] already exists")

# Create the GUI
if boolShowGUI == True:

    root = Tk()
    root.configure(background='white')

    canv = Frame(root, padx=10, pady=10)
    canv.pack(fill=BOTH)

    lblPathNew = Label(canv, text="Folder to generate the shuffled packs in")
    lblPathNew.pack()

    txt1 = Entry(canv)
    txt1.pack()

    root.mainloop()

else:

    print("GUI not shown")

# Extract Folders
    # modified code from https://bit.ly/35ChcSB
for item in os.listdir(dirSrc): # loop through items in dir
    if item.endswith(".zip"): # check for ".zip" extension
        file_name = os.path.abspath(dirSrc + "/" + item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dirDest + "/" + os.path.splitext(item)[0] ) # extract files to dir, ext from dir
        zip_ref.close() # close file
        # os.remove(file_name) # delete zipped file