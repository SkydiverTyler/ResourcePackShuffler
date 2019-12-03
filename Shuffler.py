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
# from tkinter import *
import shutil
from datetime import datetime # for pack id

# Variables you can change
dirSrc = p.normpath(
    "C:/Users/skydi/Desktop/Code/_testfolder" # put your custom source path here, inside quotes!
) # the default is:
    # os.getcwd()
    # WITHOUT the # symbol
dirDest = p.normpath(
    p.join( dirSrc,"Shuffled Packs") # put your custom destination path here, inside quotes!
) # the default is
    # p.join( dirSrc,"Shuffled Packs")
    # WITHOUT the # symbol 

# Important variables: do NOT change anything below this point
dirTemp = p.join( dirSrc,"Generating pack - please wait" )
dirTempList = p.join(dirTemp,"Master file list")
dirTempExtr = p.join(dirTemp,"Extracted packs")
dirTempComp = p.join(dirTemp, "Assembling pack in here") # folder the shuffled pack will be assembled in
dirTempCompDummy = p.join(dirTempComp, "assets", "minecraft") # remove when algorithm is created

sec = r"\u00A7" # the section symbol, for Minecraft text formatting
strPackDesc = sec + "7Shuffle your resource packs: " + sec + "3" + sec + "lgit.io/JeXLV"
intPackFormat = 4
strPackID = " (" + str(datetime.now()).replace(":","-").replace(".","-") + ")"
strPackName = "Shuffled Pack" + strPackID

dictMaster = dict() # the dictionary that will keep track of every file
setMaster = set() # a set that keeps the unique paths included in all the packs

# Create folders
print()
def cDir(thisDir):
    try:
        os.makedirs(thisDir)
    except:
        print("Folder [" + thisDir + "] already exists")
cDir(dirSrc)
cDir(dirDest)
cDir(dirTemp)
cDir(dirTempList)
cDir(dirTempExtr)
cDir(dirTempComp)
cDir(dirTempCompDummy)

# Extract Folders and Create File Dictionary
os.chdir(dirSrc)
for item in os.listdir( os.getcwd() ):
    if item.endswith(".zip"):
        f = p.join(dirSrc, item) # location of "example.zip"
        z = zipfile.ZipFile(f) # zip file object of "example.zip"
        name = p.splitext(item)[0] # "example"
        nl = z.namelist().copy()

        setMaster.update(nl) # log the contents into the master set
        dictMaster[name] = nl # log the contents of the zip to the dictionary

        z.extractall(   # extract all zips to temp dir
            p.join(dirTempExtr, name)
        )

        # z.extractall(dirTempList,
        # members=(member for member in z.namelist() if not member.endswith('.mcmeta')) # from https://bit.ly/35JlqYs
        # )
        print("Extracted [" + item + "]")
        z.close()

dictMaster[strPackID] = sorted(list(setMaster)) # convert the master set into a list and add to dict

txt = p.join(dirTemp,"dictionary.txt") # export the dictionary log - debug
t = open(txt,"w")
t.write(
    str(dictMaster).replace("], ","],\n\n\n\n")
)
t.close
print("Logged dictionary to [" + p.join(dirTemp, "dictionary.txt") + "]" )

# # Get a list of all file names
# os.chdir(dirTempList)
# for folderName, subfolders, filenames in os.walk( dirTempList ): # Location of the src assets and pack
#     for filename in filenames:
#         filePath = p.relpath( p.join(folderName, filename) ) # create file path
#         setFileList.add(filePath)
#         print("Added [" + p.relpath(filePath) + "]")


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