from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
import subprocess
pygame.mixer.init()
mixer.init()
def bar():
    import Gh.py
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="RESIDENT EVIL 7 BIOHAZARD",font=("Times",30,"bold italic"))
text=Label(t,text="CHAPTERS",fg="red",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text.place(x=100,y=100)
W= Button(t,text="GUEST HOUSE",fg="red",bg="black",command=bar())
W.place(x=200,y=200)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
t.mainloop()


