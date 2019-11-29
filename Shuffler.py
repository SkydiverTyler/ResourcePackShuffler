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
from datetime import datetime # for pack naming

# Define variables
boolShowGUI = False
dirHere = os.getcwd() # current location of this python script
dirSrc = "C:/Users/skydi/Desktop/Code/_testfolder" # location of the source resource packs
dirDest = p.join( dirSrc,"Shuffled Packs" ) # where the shuffled packs will be placed
dirTemp = p.join( dirSrc,"Generating pack - please wait" ) # temp directory
dirTempList = p.join(dirTemp,"Master file list")
dirTempExtr = p.join(dirTemp,"Extracted packs")
dirTempComp = p.join(dirTemp, "Assembling pack in here") # folder the shuffled pack will be assembled in
dirTempCompDummy = p.join(dirTempComp, "assets", "minecraft") # remove when algorithm is created
sec = r"\u00A7" # the section symbol, for Minecraft text formatting
strPackDesc = sec + "7Shuffle your resource packs: " + sec + "3" + sec + "lgit.io/JeXLV"
intPackFormat = 4
strPackID = " (" + str(datetime.now()).replace(":","-").replace(".","-") + ")"
strPackName = "Shuffled Pack" + strPackID
masterFileList = set()

print()

# Functions
def cDir(thisDir): # create the neccesary folders
    try:
        os.makedirs(thisDir)
    except:
        print("Folder [" + thisDir + "] already exists")

# Create folders
cDir(dirSrc)
cDir(dirDest)
cDir(dirTemp)
cDir(dirTempList)
cDir(dirTempExtr)
cDir(dirTempComp)
cDir(dirTempCompDummy)

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
    print("GUI hidden")

# Extract Folders
    # modified code from https://bit.ly/35ChcSB
os.chdir(dirSrc) # change working directory to source directory
for item in os.listdir( os.getcwd() ):
    if item.endswith(".zip"):
        file_name = p.join(dirSrc, item)
        z = zipfile.ZipFile(file_name)
        z.extractall(   # extract all zips to temp dir
            p.join(dirTempExtr, p.splitext(item)[0])
        )
        z.extractall(dirTempList,
            members=(member for member in z.namelist() if not member.endswith('.mcmeta')) # from https://bit.ly/35JlqYs
        )
        print("Extracted [" + item + "]")
        z.close()

# Get a list of all file names
os.chdir(dirTempList)
for folderName, subfolders, filenames in os.walk( dirTempComp ): # Location of the src assets and pack
    for filename in filenames:
        if filename.endswith(".zip") == False:
            filePath = p.join(folderName, filename) #create complete filepath of file in directory
            z.write( p.relpath( filePath ) ) # add file to zip
            print("Zipped [" + p.relpath(filePath) + "]")


# Actually shuffle the packs

# Write the Minecraft Meta file
mcm = p.join(dirTempComp,"pack.mcmeta")
t = open(mcm,"w")
t.write( '{"pack": {"pack_format":' + str(intPackFormat) + ',"description": "' + strPackDesc + '"} }' )
t.close()

dummyfile = p.join(dirTempCompDummy,"test.txt")
t = open(dummyfile,"w")
t.write("lmao")
t.close()

# Create final resource pack zip folder
os.chdir(dirTempComp) # change working dir to compilation dir
with zipfile.ZipFile( p.join( dirDest, strPackName + '.zip') , 'w') as z: # Location of the zip file
    for folderName, subfolders, filenames in os.walk( dirTempComp ): # Location of the src assets and pack
        for filename in filenames:
            if filename.endswith(".zip") == False:
                filePath = p.join(folderName, filename) #create complete filepath of file in directory
                z.write( p.relpath( filePath ) ) # add file to zip
                print("Zipped [" + p.relpath(filePath) + "]")

# Let the user know the pack has been generated
print("")
print("Success! [" +strPackName + "] created.")
print("")