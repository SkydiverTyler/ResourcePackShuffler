# IF YOU SEE THIS, AND YOU ARE TRYING TO RUN THE RANDOMIZER,
# YOU PROBABLY DON'T HAVE PYTHON INSTALLED.
# YOU NEED TO INSTALL PYTHON TO RUN THE RANDOMIZER.

# GET PYTHON AT:
# https://www.python.org/downloads/

# WHEN SETTING UP PYTHON, MAKE SURE TO CHECK "Add Python __ to PATH"
# SEE THIS IMAGE FOR MORE INFORMATION:
# https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png


# Imports
import os
from os.path import expanduser
import subprocess
import zipfile
# from tkinter import *

# Define variables
pathNew = "Shuffled packs"
boolAllowNone = False

# Create folders if they don't already exist
try:
    os.mkdir(pathNew)
except:
    print("pathNew already exists")

# # Create the GUI
# root = Tk()
# root.configure(background='white')

# canv = Frame(root, padx=10, pady=10)
# canv.pack(fill=BOTH)

# lbl1 = Label(canv, text="one", bg="red", fg="white")
# lbl1.pack()
# lbl2 = Label(canv, text="two", bg="white", fg="black")
# lbl2.pack(fill=X)
# lbl3 = Label(canv, text="three", bg="yellow", fg="black")
# lbl3.pack(side=LEFT,fill=Y)


# root.mainloop()