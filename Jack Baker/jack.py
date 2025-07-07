from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("jack1.mp3")
s1.play(loops=-1)
a="1.mp3"
b="2.mp3"
mixer.music.load(a)
[mixer.music.queue(track) for track in [b]]
mixer.music.play()
def play():
    mixer.music.load("wtfs.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Jack Baker",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("jack.png"))
text=Label(t,text=""" "WELCOME TO THE FAMILY , SON" " """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=900,y=90)
text1=Label(t,text="""Jack Baker (ジャック・ベイカー Jakku Beikā) was an American serial killer who kidnapped,
murdered and ate over a hundred men and women in Dulvey Parish,
Louisiana from 2014-2017, in coordination with his wife Marguerite,
son Lucas and adopted daughters Eveline and Mia.
At the time of his death in August 2017 it was determined by the BSAA that the
family's actions were the result of a psychoactive fungal bio-weapon that induced extreme violent tendencies.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=500)
text1.place(x=400,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=800,y=80)
text3=Label(t,text="""As a child, Jack grew up with his brother Joe at the Baker ranch in Dulvey Parish, Louisiana.
The two were well known in the area for getting into fights, including with one another.
This did not, however, prevent Jack from serving in the US Marine Corps in 1980.
How long he served for is uncertain, though by the 1990s he had settled down with Marguerite and had inherited the farm from his parents,
with Joe living close-by in a shack in the bayou.
By 1994, he and Marguerite had two children, Lucas and Zoe.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=50,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()


