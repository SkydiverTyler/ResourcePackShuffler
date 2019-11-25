# IF YOU SEE THIS, AND YOU ARE TRYING TO RUN THE SHUFFLER,
# YOU PROBABLY DON'T HAVE PYTHON INSTALLED.
# YOU WILL NEED TO INSTALL PYTHON TO RUN THE SHUFFLER.

# GET PYTHON AT:
# https://www.python.org/downloads/

# WHEN SETTING UP PYTHON, MAKE SURE TO CHECK "Add Python _._ to PATH"
# SEE THIS IMAGE FOR MORE INFORMATION:
# https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png

# Credits
# Made by Tyler Jones (SkydiverTyler)
# https://twitter.com/skydivertyler
# Please credit me, and link to the github project,
# if you use this in a YouTube video,
# or if you redistribute this program.

# Imports
import os
from os.path import expanduser
import subprocess
import zipfile
from tkinter import *

# Define variables
boolShowGUI = True
pathNew = "Shuffled packs"
boolAllowEmptyTextures = False

# Create folders if they don't already exist
try:
    os.mkdir(pathNew)
except:
    print("pathNew already exists")

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

    print("gui not shown")