from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("2.mp3")
s1.play(loops=-1)
mixer.music.load("1.mp3")
mixer.music.play()
def play():
    mixer.music.load("dl.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Donna Beneviento",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("d.png"))
text=Label(t,text=""" "Don't leave...I can't let you..." """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=900,y=90)
text1=Label(t,text="""Donna Beneviento was a mutant human doll-maker
who resided in an Eastern European mountain range.
Dressed in a black garb,
she was usually seen with her doll, Angie,
through which she often communicated.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=900,y=380)
text1.place(x=700,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=800,y=80)
text3=Label(t,text="""Donna Beneviento was born into gentry sometime in the 20th century.
The family of House Beneviento had ancestral links to Berengario,
an ancient mutant in folklore said to have settled the region with three others,
from whom the Dimitrescu, Moreau and Heisenberg families are descendant.
Whether this feudal rule over the region was continually maintained or had disappeared by the Great War is uncertain,
though Miranda - a prophet serving the Black God -
sought to establish their descendants as a council controlling the region under her oversight""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=700,y=430)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()
