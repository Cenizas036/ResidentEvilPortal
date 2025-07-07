from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("ld1.mp3")
s1.play(loops=-1)
mixer.music.load("2.mp3")
mixer.music.play()
def play():
    mixer.music.load("sw.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Lady Dimitrescu",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("ld.png"))
text=Label(t,text=""" "So we Finally Meet" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=900,y=90)
text1=Label(t,text="""Countess Alcina Dimitrescu (オルチーナ・ドミトレスク oruchīna domitoresuku?),
commonly referred to as Lady Dimitrescu, was a mutant human aristocrat.
From the 1950s until her death in 2021,
Dimitrescu maintained a pseudo-feudal rule over
the peasantry near Castle Dimitrescu as one of the Four Lords of the region.
For more than sixty years, Dimitrescu was
feared by the locals over allegations of mass murder and cannibalism,
which were later found to be true.
She was killed by Ethan Winters in February 2021,
after conspiring with Mother Miranda in the abduction of his daughter Rose.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=500)
text1.place(x=800,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=800,y=80)
text3=Label(t,text="""Alcina Dimitrescu was born into the noble Dimitrescu family sometime before the Great War,
and through this ancestry inherited a hereditary blood disease.Although her family traced their origins to Cesare,
one of the four founders of an isolated mountain village in Europe, Alcina herself lived elsewhere, perhaps through a cadet branch.
At some point in her youth, likely the 1930s,
she had a brief music career in the emerging Jazz scene,
where she went by the name "Miss D" and played with a band called "The Pallboys".
In the aftermath of the Second World War and the abolition of the nobility,
Dimitrescu returned to her family's former lands,
which had fallen under the control of a neopagan cult worshipping the Black God.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=50,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()


