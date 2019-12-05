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
import random

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

dictFiles = dict() # the dictionary that will keep track of every file
setMaster = set() # a set that keeps the unique paths included in all the packs
listMaster = list() # setMaster, but in a list and sorted




# Create folders
print()
def cDir(thisDir):
    try:
        os.makedirs(thisDir)
        print("Created folder [" + thisDir + "]")
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
        dictFiles[name] = nl # log the contents of the zip to the dictionary

        z.extractall(   # extract all zips to temp dir
            p.join(dirTempExtr, name)
        )
        # z.extractall(dirTempList,
        # members=(member for member in z.namelist() if not member.endswith('.mcmeta')) # from https://bit.ly/35JlqYs
        # )
        print("Extracted [" + item + "]")
        z.close()

listMaster = sorted(list(setMaster)) # convert the master set into a sorted list


txt = p.join(dirTemp,"dictionary.txt") # export the dictionary log - debug
t = open(txt,"w")
t.write(str(listMaster) + "\n\n\n\n\n")
t.write(str(dictFiles).replace("], ","],\n\n\n\n\n"))
t.close
print("Logged dictionary to [" + p.join(dirTemp, "dictionary.txt") + "]" )

# Write the Minecraft Meta file
    #todo - check formats of all the packs and display an error if more than one format
mcm = p.join(dirTempComp,"pack.mcmeta")
t = open(mcm,"w")
t.write( '{"pack": {"pack_format":' + str(intPackFormat) + ',"description": "' + strPackDesc + '"} }' )
t.close()

dummyfile = p.join(dirTempCompDummy,"test.txt")
t = open(dummyfile,"w")
t.write("lmao")
t.close()

# Actually shuffle the packs
for i in listMaster:
    tempList = []
    if str(i).endswith(".mcmeta") == False:
        for j, k in dictFiles.items():
            if i in k:
                print("[" + i + "] is in [" + j + "]")
                tempList.append( p.join(j,i) )
        chosenFile = random.choice(tempList)
        print("Chose [" + chosenFile + "] as the random texture or file!")
        chosenMeta = chosenFile + ".mcmeta"
        copyTo = p.join(dirTempComp,i)

        try:
            shutil.copy( p.join( dirTempExtr, chosenFile) , copyTo ) # copy file to final location
            print("Copied chosen file to [" + copyTo + "]")
            try:
                shutil.copy( p.join( dirTempExtr, chosenMeta) , copyTo + ".mcmeta" ) # copy the associated .mcmeta file if it exists
                print("Meta file ["+chosenMeta+"] copied to same location")   
            except:
                pass     
        except:
            cDir(copyTo) # create the folder if it's not a file


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