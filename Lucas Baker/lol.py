from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound(".mp3")
s1.play(loops=-1)
mixer.music.load("1.mp3")
mixer.music.play()
def play():
    mixer.music.load("cr1.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Chris Redfield",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("cr.png"))
text=Label(t,text=""" "Sorry Ethan" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=900,y=90)
text1=Label(t,text="""Captain Chris Redfield (クリス・レッドフィールド Kurisu Reddofīrudo) is an American operator in the Bioterrorism Security Assessment Alliance,
in which he has served since its foundation in 2003.
Redfield has built up and dedicated his career in destroying Bio Organic Weapons
and fighting against producers and sellers of bioweapons after his experiences with bioterrorism in 1998.
He is the older brother of TerraSave member Claire Redfield.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=500)
text1.place(x=700,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=800,y=80)
text3=Label(t,text="""Not much is known about Redfield's early life, except that he and Claire had lost their parents at some point before 1998,
having only each other as family. As an adult, Redfield joined the United States Air Force, where he received flight training for both planes and helicopters.
He served in a unit alongside Barry Burton, whom he befriended.
Redfield held strong convictions that often put him at odds with his senior officers,
and he either resigned in protest or was discharged for insubordination.
During this period Redfield also trained with a variety of weapons, including knives,
and was known for his skills in hand-to-hand combat and marksmanship, which he won a contest for.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=50,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()


