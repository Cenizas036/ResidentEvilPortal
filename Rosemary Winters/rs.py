from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("1.mp3")
s1.play(loops=-1)
mixer.music.load("2.mp3")
mixer.music.play()
def play():
    mixer.music.load("3.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Rosemary Winters",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("rs.png"))
text=Label(t,text=""" "Happy Birthday Dad!" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=800,y=90)
text1=Label(t,text="""Rosemary "Rose" Winters
(ローズマリー・ウィンターズ Rōzumarī Wintāzu?) is an American superhuman.
The daughter of mutants Ethan and Mia Winters, Winters' body was comprised entirely of Mold,
which was replicating human DNA.
Following her rescue from an outbreak in Eastern Europe,
Rose grew up in the United States under special protection.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=800,y=350)
text1.place(x=700,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=700,y=80)
text3=Label(t,text="""Rose was born on August 2, 2020 whilst her parents were under BSAA protection.
Due to the family's mutations as well as Mia's former ties to The Connections,
they were at serious risk of abduction for experimentation or even assassination.
While there is evidence suggesting they were moved repeatedly,
by 2021 they were living in a mountain range in Eastern Europe.
At this point, Rose' existence was leaked through unspecified means,
either through the BSAA or The Connections.
When Mother Miranda, a mutant priestess from a nearby village,
obtained this information, she abducted Mia
and assimilated her DNA to take on her appearance.
When this assimilation took place is uncertain,
though the BSAA obtained evidence of the plot by Monday 8 February.
Though the raid was initially a success,
Miranda faked her death and was able to snatch Rose while the two were being transported.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=700,y=400)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()


