from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
import mysql.connector as sqltor
import os
mc=sqltor.connect(host="localhost",user="root",passwd="Lol*1234",database="LOGIN")
c1=mc.cursor()
t=tkinter.Tk()
w=Canvas(t,bg="black",height=1000,width=3000)
t.iconbitmap(r"RE.ico")
t.title("RESIDENT EVIL PORTAL")
def e(m,f):
   top= Toplevel(t)
   top.geometry("750x250")
   top.title(f)
   Label(top, text=m, font=('Mistral 18 bold')).place(x=150,y=80)
def logintodb(u,p):
     c1.execute("SELECT * FROM login")
     n=c1.fetchall()
     for i in n:
         print(i[0],i[1])
         if(i[0]==u and i[1]==p):
             f=1
             break
         elif(i[0]==u and i[1]!=p):
             f=2
         else:
             f=3
     if(f==1):
         return 1
     else:
         return 2
def submitact():
    u = e1.get()
    p = e2.get()
    k= logintodb(u, p)
    if(k==1):
        os.chdir("D:\Python\Resident Evil Portal")
        os.system("python XX.py")
        e("Logged in Successfully","Success")
    elif(k==2):
        e("Invalid Account","Error")
def account():
   os.chdir("D:\Python\Resident Evil Portal")
   os.system("python REP1.py")
img=ImageTk.PhotoImage(Image.open("img.png"))
l=Label(t,text="WELCOME TO THE PORTAL",font=("Times",30,"bold italic"))
text=Label(t,text="LOGIN",fg="RED",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=650,y=100)
text=Label(t,text="USERNAME",fg="RED",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=500,y=200)
e1 = Entry(t,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
e1.place(x=700,y=200)
text=Label(t,text="PASSWORD",fg="RED",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=500,y=300)
e2 = Entry(t,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
e2.place(x=700,y=300)
L1 = Button(t, text ="Login",fg="white",bg="black",font=("Arial Bold",25),justify= LEFT,command = submitact)
L1.place(x = 650 , y = 400)
L1 = Button(t, text ="CREATE NEW ACCOUNT",fg="white",bg="black",font=("Arial Bold",25),justify= LEFT,command = account)
L1.place(x = 650 , y = 600)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()
