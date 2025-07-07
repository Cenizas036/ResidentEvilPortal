from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
import mysql.connector as sqltor
mc=sqltor.connect(host="localhost",user="root",passwd="Lol*1234",database="LOGIN")
c1=mc.cursor()
t=tkinter.Tk()
w=Canvas(t,bg="black",height=1000,width=3000)
def e(m,f):
   top= Toplevel(t)
   top.geometry("750x250")
   top.title(f)
   Label(top, text=m, font=('Mistral 18 bold')).place(x=150,y=80)
def submitact():
    u = e1.get()
    p = e2.get()
    c1.execute("SELECT * FROM login")
    n=c1.fetchall()
    for i in n:
        if(i[0]==u):
            e("USERNAME EXISTS","Error")
            return 23
    if(len(p)<8):
        e("Password Should be atleast 8 Characters","Error")
    else:
        k=1
    F1="INSERT INTO login(username,password) VALUES(%s,%s)"
    v=(u,p)
    c1.execute(F1,v)
    mc.commit()
    if(k==1):
        e("Account Created","Success")
t.iconbitmap(r"RE.ico")
t.title("RESIDENT EVIL PORTAL")
img=ImageTk.PhotoImage(Image.open("img.png"))
l=Label(t,text="CREATE ACCOUNT",font=("Times",30,"bold italic"))
text=Label(t,text="DETAILS",fg="RED",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=650,y=100)
text=Label(t,text="USERNAME",fg="RED",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=500,y=200)
e1 = Entry(t,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
e1.place(x=700,y=200)
text=Label(t,text="PASSWORD",fg="RED",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=500,y=300)
e2 = Entry(t,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
e2.place(x=700,y=300)
L1 = Button(t, text ="SUBMIT",fg="white",bg="black",font=("Arial Bold",25),justify= LEFT,command = submitact)
L1.place(x = 650 , y = 400)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()
