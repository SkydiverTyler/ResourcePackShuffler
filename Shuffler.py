# IF YOU SEE THIS, AND YOU ARE TRYING TO RUN THE SHUFFLER,
# PLEASE OPEN THE "README.MD" FILE IN A TEXT EDITOR
# FOR INSTRUCTIONS

# Credits
    # Made by Tyler Jones (SkydiverTyler)
    # https://twitter.com/skydivertyler
    # Please credit me.

# Imports (don't change these)
import os
from os import path as p
from os.path import expanduser
import subprocess
import zipfile
# from tkinter import *
import shutil
from datetime import datetime # for pack id
import random
import time




# Variables you can change are below:

intPackFormat = 4
    # The default is 4

    # If the source packs were compatible with the Minecraft version
    # you are using, then the shuffled pack should be compatible
    # no matter what Minecraft tells you.
    # For more information on pack formats, see
    # https://minecraft.gamepedia.com/Resource_pack#History

dirSrc = p.normpath(
    p.dirname(p.abspath(__file__))
)   # Paste your source folder path above, then put it inside quotes!
    # The default is:
    # str(os.getcwd())
    # WITHOUT the # symbol

dirDest = p.normpath(
    p.join( dirSrc,"Shuffled Packs") 
)   # Paste your destination folder path above, then put it inside quotes!
    # The default is
    # p.join( dirSrc,"Shuffled Packs")
    # WITHOUT the # symbol 

noUniques = False
    # The default is False.
    # In this case, every file will be merged and shuffled.
    
    # If you change this to True (case-sensitive),
    # textures that only exist in one resource pack will not be used.
    # Less textures will be in the final shuffled pack overall,
    # but each texture will have a chance to be different, every time you run the Shuffler.






# Important variables: do NOT change anything below this point

dirTemp = p.join( dirSrc,"Generating pack - please wait" )
dirTempExtr = p.join(dirTemp,"Extracted packs")
dirTempComp = p.join(dirTemp, "Assembling pack in here") # folder the shuffled pack will be assembled in
# dirTempCompDummy = p.join(dirTempComp, "assets", "minecraft") # remove when algorithm is created

sec = r"\u00A7" # the section symbol, for Minecraft text formatting
strPackDesc = sec + "7Shuffle your resource packs: " + sec + "3" + sec + "l" + "git.io/JeXLV"
strPackID = " (" + str(datetime.now()).replace(":","-").replace(".","-") + ")"
strPackName = "Shuffled Pack" + strPackID

dictFiles = dict() # the dictionary that will keep track of every file
setMaster = set() # a set that keeps the unique paths
listMaster = list() # setMaster, but in a list and later sorted




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
cDir(dirTempExtr)
cDir(dirTempComp)
# cDir(dirTempCompDummy)

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
    #todo - check formats of all the packs and display an error if more than one format exists
mcm = p.join(dirTempComp,"pack.mcmeta")
t = open(mcm,"w")
t.write( '{"pack": {"pack_format":' + str(intPackFormat) + ',"description": "' + strPackDesc + '"} }' )
t.close()

# dummyfile = p.join(dirTempCompDummy,"test.txt")
# t = open(dummyfile,"w")
# t.write("lmao")
# t.close()

# Actually shuffle the packs
for i in listMaster:
    tempList = []
    if str(i).endswith(".mcmeta") == False:
        for j, k in dictFiles.items():
            if i in k:
                print("[" + i + "] is in [" + j + "]")
                tempList.append( p.join(j,i) )
        
        if noUniques == False:
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

        else:   # if noUniques is True
            if len(tempList) >= 2:

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
            
            else:
                print("Skipped [" + i + "] because it only appears once")
        


# Create final resource pack zip folder
os.chdir(dirTempComp) # change working dir to compilation dir
with zipfile.ZipFile( p.join( dirDest, strPackName + '.zip') , 'w') as z: # Location of the zip file
    for folderName, subfolders, filenames in os.walk( dirTempComp ): # Location of the src assets and pack
        for filename in filenames:
            if filename.endswith(".zip") == False:
                filePath = p.join(folderName, filename) #create complete filepath of file in directory
                z.write( p.relpath( filePath ) ) # add file to zip
                print("Zipped [" + p.relpath(filePath) + "]")


os.chdir(dirSrc) # change directory, so that the temp dir can be deleted

shutil.rmtree(dirTemp) # remove the temp folder

# Let the user know the pack has been generated
print("")
print("\tSuccess! [" +strPackName + "] created.")
print("")

time.sleep(20)