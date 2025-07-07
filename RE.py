from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
import os
import sys
from pygame import mixer
import pygame
def bar():
    os.chdir("D:\Python\Resident Evil Portal\Ethan Winters")
    os.system("python EW.py")
def bar1():
     os.chdir("D:\Python\Resident Evil Portal\Mia Winters")
     os.system("python mia.py")
def bar3():
     os.chdir("D:\Python\Resident Evil Portal\Rosemary Winters")
     os.system("python rs.py")
def bar4():
     os.chdir("D:\Python\Resident Evil Portal\Jack Baker")
     os.system("python jack.py")
def bar5():
     os.chdir("D:\Python\Resident Evil Portal\Marguerite Baker")
     os.system("python mg.py")
def bar6():
     os.chdir("D:\Python\Resident Evil Portal\Lucas Baker")
     os.system('python lucas.py')
def bar7():
     os.chdir("D:\Python\Resident Evil Portal\Zoe Baker")
     os.system("python zoe.py")
def bar8():
     os.chdir("D:\Python\Resident Evil Portal\Duke")
     os.system("python duke.py")
def bar9():
     os.chdir("D:\Python\Resident Evil Portal\Lady Dimitrescu")
     os.system("python ld.py")
def bar10():
     os.chdir("D:\Python\Resident Evil Portal\Daughters")
     os.system("python 3d.py")
def bar11():
     os.chdir("D:\Python\Resident Evil Portal\Karl Heisenberg")
     os.system("python kh.py")
def bar12():
     os.chdir("D:\Python\Resident Evil Portal\Donna Beneviento")
     os.system("python db.py")
def bar13():
     os.chdir("D:\Python\Resident Evil Portal\Mother Miranda")
     os.system("python mm.py")
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="CHARACTERS",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("EW.png"))
img2=ImageTk.PhotoImage(Image.open("mia.png"))
img4=ImageTk.PhotoImage(Image.open("rs.png"))
img5=ImageTk.PhotoImage(Image.open("jack.png"))
img6=ImageTk.PhotoImage(Image.open("mg.png"))
img7=ImageTk.PhotoImage(Image.open("lb.png"))
img8=ImageTk.PhotoImage(Image.open("zoe.png"))
img9=ImageTk.PhotoImage(Image.open("dk.png"))
img10=ImageTk.PhotoImage(Image.open("ld.png"))
img11=ImageTk.PhotoImage(Image.open("3d.png"))
img12=ImageTk.PhotoImage(Image.open("kh.png"))
img13=ImageTk.PhotoImage(Image.open("db.png"))
img14=ImageTk.PhotoImage(Image.open("mm.png"))
W= Button(t,bg="black",image=img,height=150,width=150,command=bar)
W.place(x=100,y=200)
l1=Label(t,text="ETHAN WINTERS",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=100,y=330)
W= Button(t,bg="black",image=img2,height=150,width=150,command=bar1)
W.place(x=310,y=200)
l1=Label(t,text="MIA WINTERS",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=320,y=330)
W= Button(t,bg="black",image=img4,height=150,width=150,command=bar3)
W.place(x=610,y=200)
l1=Label(t,text="ROSEMARY WINTERS",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=590,y=330)
W= Button(t,bg="black",image=img5,height=150,width=150,command=bar4)
W.place(x=810,y=200)
l1=Label(t,text="JACK BAKER",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=820,y=330)
W= Button(t,bg="black",image=img6,height=150,width=150,command=bar5)
W.place(x=1001,y=200)
l1=Label(t,text="MARGUERITE BAKER",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=985,y=330)
W= Button(t,bg="black",image=img7,height=150,width=150,command=bar6)
W.place(x=1201,y=200)
l1=Label(t,text="LUCAS BAKER",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=1211,y=330)
W= Button(t,bg="black",image=img8,height=150,width=150,command=bar7)
W.place(x=10,y=400)
l1=Label(t,text="ZOE BAKER",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=20,y=530)
W= Button(t,bg="black",image=img9,height=150,width=150,command=bar8)
W.place(x=210,y=400)
l1=Label(t,text="DUKE",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=240,y=530)
W= Button(t,bg="black",image=img10,height=150,width=150,command=bar9)
W.place(x=410,y=400)
l1=Label(t,text="LADY DIMITRESCU",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=390,y=530)
W= Button(t,bg="black",image=img11,height=150,width=150,command=bar10)
W.place(x=610,y=400)
l1=Label(t,text="D DAUGHTERS",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=610,y=530)
W= Button(t,bg="black",image=img12,height=150,width=150,command=bar11)
W.place(x=810,y=400)
l1=Label(t,text="KARL HEISENBERG",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=790,y=530)
W= Button(t,bg="black",image=img13,height=150,width=150,command=bar12)
W.place(x=1010,y=400)
l1=Label(t,text="DONNA BENEVIENTO",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=990,y=530)
W= Button(t,bg="black",image=img14,height=150,width=150,command=bar13)
W.place(x=1210,y=400)
l1=Label(t,text="MOTHER MIRANDA",fg="red",bg="black",font=("Times",15),justify=LEFT)
l1.place(x=1210,y=530)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
t.mainloop()



