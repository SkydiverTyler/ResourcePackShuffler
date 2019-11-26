# IF YOU SEE THIS, AND YOU ARE TRYING TO RUN THE SHUFFLER,
# PLEASE OPEN THE "README.MD" FILE IN A TEXT EDITOR
# FOR HELP

# Credits
    # Made by Tyler Jones (SkydiverTyler)
    # https://twitter.com/skydivertyler
    # Please credit me.

# Imports
import os
from os import path as p
from os.path import expanduser
import subprocess
import zipfile
from tkinter import *
import shutil
import random # for pack naming
from datetime import datetime # for pack naming

# Define variables
boolShowGUI = False
boolAllowEmptyTextures = False
dirHere = os.getcwd() # current location of this python script
dirSrc = "C:/Users/skydi/Desktop/Code/_testfolder" # location of the source resource packs
dirDest = p.join( dirSrc,"Shuffled Packs" ) # where the shuffled packs will be placed
dirTemp = p.join( dirSrc,"Generating pack, please wait" ) # temp directory

sec = r"\u00A7" # the section symbol, for Minecraft text formatting
strPackDesc = sec + "7Shuffle your resource packs: " + sec + "3" + sec + "lgit.io/JeXLV"
intPackFormat = 4
intPackID = datetime.now()
strPackName = sec + "6Shuffled Resource Pack!" + sec + "r[ ID:" + str(intPackID) + "]"

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
for item in os.listdir(dirSrc):
    if item.endswith(".zip"):
        file_name = p.abspath(
            p.join(dirSrc, item)
        )
        z = zipfile.ZipFile(file_name)
        print("Extracting " + item)
        z.extractall(
            p.join(dirTemp, p.splitext(item)[0])
        )
        z.close()
        #shutil.rmtree(dirTemp)

# # Creating a list of all the files in each direcrory
# for path, subdirs, files in os.walk(dirTemp):
#     for name in files:
#         print( os.path.join(path, name) )

# Write the Minecraft Meta file
mcm = p.join(dirTemp,"pack.mcmeta")

# try:
#     os.remove(mcm)
# except:
#     print("The file pack.mcmeta already exists")

t = open(mcm,"w")
t.write( '{"pack": {"pack_format":' + str(intPackFormat) + ',"description": "' + strPackDesc + '"} }' )
t.close()

# Let the user know the pack has been generated
print(strPackName)
print()