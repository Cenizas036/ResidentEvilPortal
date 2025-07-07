from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("rc.mp3")
s1.play(loops=-1)
mixer.music.load("1.mp3")
mixer.music.play()
def play():
    mixer.music.load("d1.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Duke",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("dk.png"))
text=Label(t,text=""" "I have been waiting for you, Mister Winters" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=800,y=90)
text1=Label(t,text="""The Duke is a mysterious, morbidly obese character
who serves as a merchant and aids Ethan Winters in Resident Evil Village.
He has been the resident merchant of the village for years,
profiting well from his business transactions.
He becomes an important guide in Ethan's journey to rescue his daughter Rosemary.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=300,y=500)
text1.place(x=800,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=700,y=80)
text3=Label(t,text="""The Duke was the village's resident merchant for years.
He is an obese person with a jolly personality,
his Emporium littered with supplies and bedecked with garlic to fend off vampiric monsters.
His motives are often purely profit-driven, as he is willing to do business with anyone in the village,
including Lady Alcina Dimitrescu, as he had a station inside her castle.
Despite this, he has occasionally granted favors to several villagers;
he brought old newspapers to Ernest upon request so that he could read about goings-on of the outside world,
despite it being forbidden by Mother Miranda.
He also seems to know the Merchant from Spain.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=50,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()



