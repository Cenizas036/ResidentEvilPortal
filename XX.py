from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
import os
import sys
from pygame import mixer
import pygame
def bar():
    os.chdir("D:\Python\Resident Evil Portal\Resident Evil 7")
    os.system("python RE7.py")
def bar1():
     os.chdir("D:\Python\Resident Evil Portal\Resident Evil Village")
     os.system("python Re8.py")
def bar3():
        os.chdir("D:\Python\Resident Evil Portal")
        os.system("python RE.py")
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="WELCOME TO THE RE VERSE",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("RE7.png"))
img2=ImageTk.PhotoImage(Image.open("RE8.png"))
img4=ImageTk.PhotoImage(Image.open("REV.png"))
W= Button(t,bg="black",image=img,height=400,width=400,command=bar)
W.place(x=100,y=200)
W= Button(t,bg="black",image=img2,height=400,width=400,command=bar1)
W.place(x=550,y=200)
W= Button(t,bg="black",image=img4,height=400,width=400,command=bar3)
W.place(x=1000,y=200)
l1=Label(t,text="CHARACTERS",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=1130,y=570)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
t.mainloop()



