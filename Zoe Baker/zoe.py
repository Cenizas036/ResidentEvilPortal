from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("sf.mp3")
s1.play(loops=-1)
a="1.mp3"
mixer.music.load(a)
mixer.music.play()
def play():
    mixer.music.load("2.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Zoe Baker",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("zb.png"))
text=Label(t,text=""" "It's you! I don't believe it.
You actually made it.You didn't forget about me.
Thank you Ethan."  """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=500,y=100)
text1=Label(t,text="""Zoe Baker (ゾイ・ベイカー Zoi Beikā?) is a woman from Dulvey,
Louisiana who was involved in the Dulvey incident,
a three-year series of abductions by her parents, Jack and Marguerite Baker, and her brother Lucas,
all at the behest of Eveline, a young girl genetically-engineered to control minds.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=500)
text1.place(x=400,y=250)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=400,y=100)
text3=Label(t,text="""Zoe lived with the Baker Family on the Plantation in Dulvey, Louisiana,
with her parents and older brother Lucas.
Zoe did an art project in the fourth grade of her
and her family which hung in the dining room. """,fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=450,y=560)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()



