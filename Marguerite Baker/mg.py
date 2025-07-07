from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("re89.mp3")
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
l=Label(t,text="Marguerite Baker",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("mg.png"))
text=Label(t,text=""" "Zoe? Come look. Come see her gift.
Look at all the pretties my little girl has given me!"  """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=400,y=90)
text1=Label(t,text="""Marguerite Baker (マーガレット・ベイカー Māgaretto Beikā) was a resident of the Baker ranch household,
a mansion in Dulvey, Louisiana.
She was the wife of Jack Baker and mother of Zoe and Lucas Baker.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=300)
text1.place(x=300,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=300,y=80)
text3=Label(t,text="""Marguerite was the matriarch of the Baker family,
which consisted of her husband, Jack, and children, Lucas and Zoe.
They lived on a large plantation in the Louisiana swamps,
comprising a mansion and an older house, with mines and a pier nearby.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=380,y=380)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()


