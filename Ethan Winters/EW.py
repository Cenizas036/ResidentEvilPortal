from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("EW5.mp3")
s1.play(loops=-1)
a="D:\Python\Resident Evil Portal\Ethan Winters\EW4.mp3"
b="D:\Python\Resident Evil Portal\Ethan Winters\EW3.mp3"
mixer.music.load(b)
[mixer.music.queue(track) for track in [a]]
mixer.music.play()
def play():
    mixer.music.load("D:\Python\Resident Evil Portal\Ethan Winters\EW2.wav")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Ethan Winters",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("Ew1.png"))
text=Label(t,text=""" "GOODBYE ROSEMARY" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=900,y=90)
text1=Label(t,text="""The one and only.
The greatest father figures of the Resident Evil Universe and dare I say the gaming world.
Ethan Winters (イーサン・ウィンターズ Īsan Wintāzu)
(c.1984-10 February 2021) was an American mutant trained as systems engineer.
One of many mutant victims of biological weaponry,
Winters was infected with a weaponised species of "Mold" during the 2017 Dulvey incident.
He and his wife Mia were rescued by the Bioterrorism Security Assessment Alliance,
and were placed under witness protection in Eastern Europe.
This protection ultimately unravelled in February 2021 when their daughter,
Rosemary, was abducted by Mother Miranda. Winters was successful in rescuing Rosemary,
but gave his life to protect a BSAA tiltrotor.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=500)
text1.place(x=700,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=800,y=80)
text3=Label(t,text="""Little is known of Winter's early life, though it is known that by 2017 he was living and working in Los Angeles, California as a systems engineer.
In May 2011 he married his Texan girlfriend, Mia,who he believed was a high-ranking employee in a trading company
but was in fact a research assistant for The Connections, a manufacturer of illegal bioweapons.
Mia disappeared in October 2014 while crossing the Gulf of Mexico during a hurricane, and was assumed dead.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=50,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()

