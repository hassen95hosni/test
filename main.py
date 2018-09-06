def mainmachine():
    os.system("smartone.py")

def mainplayer():
    os.system('PROJETPY.py')

from tkinter import *

import os
import sys

mw=Tk()
a=Label(mw,text="Want to ")
b=Label(mw,text="Play")
a.grid(row=1,column=1)
b.grid(row=1,column=2)
c=Button(mw,text="player against player",command=mainplayer)
d=Button(mw,text="player against machine",command=mainmachine)
c.grid(row=2,column=1)
d.grid(row=2,column=2)
