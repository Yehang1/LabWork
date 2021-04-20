import os
import pickle

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
import pygame

root=Tk()
root.geometry("800x400")
root.wm_title("yehang ko music player")



#initialising pygame
pygame.mixer.init()
#creating playlist icons
song_box=Listbox(root,bg="blue",fg="white",width=100)
song_box.pack(pady=20)
#creting buttons
pause=PhotoImage(file=r"C:\Users\lenovo\Desktop\pause.png")
pause_btn=Button(root,image=pause).pack(side=TOP)





root.mainloop()





