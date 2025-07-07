from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("3.mp3")
s1.play(loops=-1)
def play():
    mixer.music.load("bd.mp3")
    mixer.music.play()
def play1():
    mixer.music.load("cd1.mp3")
    mixer.music.play()
def play2():
    mixer.music.load("2.mp3")
    mixer.music.play()
mixer.music.load("1.mp3")
mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="The Dimitrescu Daughters",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("bl.png"))
img2=ImageTk.PhotoImage(Image.open("cc.png"))
img3=ImageTk.PhotoImage(Image.open("dd.png"))
text=Label(t,text=" Bela Dimitrescu",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text1=Label(t,text="""Bela Dimitrescu was a chimæric mutant human born from the Cadou research project,
and an adopted daughter of Countess Alcina Dimitrescu.
She resided at Castle Dimitrescu with the rest of her family,
including fellow adopted siblings Daniela and Cassandra.
She was the oldest daughter, noted to be quiet but with a strong head on her shoulders.
She was killed during a raid on the castle by Ethan Winters.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
p=PhotoImage(file='play.png')
text2=Label(t,text="""" "I can't believe Cassandra
   caused all this mess" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=990,y=80)
text2.place(x=1050,y=80)
text.place(x=300,y=80)
text1.place(x=300,y=130)
text3=Label(t,text=" Cassandra Dimitrescu",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text4=Label(t,text="""Cassandra Dimitrescu was a chimæric mutant human born from the Cadou research project,
and an adopted daughter of Countess Alcina Dimitrescu. She resided at Castle Dimitrescu with the rest of her family,
including fellow adopted siblings Bela and Daniela.
Cassandra was the middle child and she was noted to be a sadist
who particularly enjoyed tormenting and killing her victims.
She was killed during a raid on the castle by Ethan Winters.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
p=PhotoImage(file='play.png')
text5=Label(t,text="""" "You will not get away!
    You're my prey... mine.." """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text5.place(x=1050,y=400)
text3.place(x=300,y=300)
text4.place(x=300,y=350)
text6=Label(t,text="Daniela Dimitrescu",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text7=Label(t,text="""Daniela Dimitrescu was a chimæric mutant human born from the Cadou research project,
and an adopted daughter of Countess Alcina Dimitrescu.
She resided at Castle Dimitrescu with the rest of her family,
including fellow adopted siblings Bela and Cassandra.
Daniela was the youngest daughter
and she was noted to be the most delusional of the three.
She was killed during a raid on the castle by Ethan Winters.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
p=PhotoImage(file='play.png')
text8=Label(t,text="""" "So you finally
  came to see me!
Everyone falls for me in time!" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=990,y=80)
b = Button(t, image=p,height=90,width=80, command=play1)
b.place(x=990,y=400)
text8.place(x=1080,y=600)
text6.place(x=300,y=560)
text7.place(x=300,y=600)
b2= Button(t, image=p,height=90,width=80, command=play2)
b2.place(x=1000,y=600)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
w.create_image(20,250,anchor=NW,image=img2)
w.create_image(20,500,anchor=NW,image=img3)
t.mainloop()




