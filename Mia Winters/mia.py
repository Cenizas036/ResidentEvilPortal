from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("Re72.mp3")
s1.play(loops=-1)
a="1.mp3"
b="2.mp3"
mixer.music.load(a)
[mixer.music.queue(track) for track in [b]]
mixer.music.play()
def play():
    mixer.music.load("re71.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Mia Winters",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("mia.png"))
text=Label(t,text=""" Mia's Message in Resident Evil 7 Biohazard  """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=700,y=90)
text1=Label(t,text="""Mia Winters (ミア・ウィンターズ Mia Wintāzu) is a former operative
for The Connections who worked covertly in the birth of Eveline,
acting as her "caretaker" for her while covering up her career
as a worker at a "trading company" to her husband, Ethan.
After being presumed dead in 2014, she was recovered by the Baker family,
and resided under lock and key at their property until being re-discovered in mid-2017.
After Eveline's death, Mia and Ethan started a family again
and Mia gave birth to their daughter, Rosemary Winters.
However, Mia was captured and used in experimentation by Mother Miranda
and her cult in an attempt to use Rose as a vessel to revive Miranda's late daughter,Eva.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=800,y=500)
text1.place(x=600,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=600,y=80)
text3=Label(t,text="""Mia was a resident of Texas in the 2000s when she began dating Ethan Winters.
In 2010, she began working as a researcher for The Connections,
a crime syndicate specializing in production of bio-weaponry.
This was kept secret from Ethan, who she would marry on May 29, 2011.
Whether they moved to California at this point or if Ethan did on his own is presently uncertain.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=580,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()


