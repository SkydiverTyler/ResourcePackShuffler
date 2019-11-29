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
boolAllowEmptyTextures = False

dirHere = os.getcwd() # current location of this python script
dirSrc = "C:/Users/skydi/Desktop/Code/_testfolder" # location of the source resource packs
dirDest = p.join( dirSrc,"Shuffled Packs" ) # where the shuffled packs will be placed
dirTemp = p.join( dirSrc,"Generating pack, please wait" ) # temp directory
dirComp = p.join(dirTemp, "_Assembling pack in here") # folder the shuffled pack will be assembled in
dirDummy = p.join(dirComp, "assets", "minecraft") # remove when algorithm is created

sec = r"\u00A7" # the section symbol, for Minecraft text formatting
strPackDesc = sec + "7Shuffle your resource packs: " + sec + "3" + sec + "lgit.io/JeXLV"
intPackFormat = 4
strPackID = " (" + str(datetime.now()).replace(":","-").replace(".","-") + ")"
strPackName = "Shuffled Pack" + strPackID

print("")

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
cDir(dirComp)
cDir(dirDummy)

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
os.chdir(dirSrc) # change working directory to source directory
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

# Write the Minecraft Meta file
mcm = p.join(dirComp,"pack.mcmeta")
t = open(mcm,"w")
t.write( '{"pack": {"pack_format":' + str(intPackFormat) + ',"description": "' + strPackDesc + '"} }' )
t.close()

dummyfile = p.join(dirDummy,"test.txt")
t = open(dummyfile,"w")
t.write("lmao")
t.close()

# Create final resource pack zip folder
print("")
os.chdir(dirComp) # change working dir to compilation dir
with zipfile.ZipFile( p.join( dirDest, strPackName + '.zip') , 'w') as z: # Location of the zip file
    for folderName, subfolders, filenames in os.walk( dirComp ): # Location of the src assets and pack
        for filename in filenames:
            if filename.endswith(".zip") == False:
                filePath = os.path.join(folderName, filename) #create complete filepath of file in directory
                z.write( p.relpath( filePath ) ) # add file to zip
                print("File [" + p.relpath(filePath) + "] zipped" )

# Let the user know the pack has been generated
print()
print(strPackName + " successfully created!")
print()