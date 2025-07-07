from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("bl.mp3")
s1.play(loops=-1)
mixer.music.load("12.mp3")
mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Karl Heisenberg",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("kh.png"))
text=Label(t,text=""" "Let's see what you're really made of , Ethan Winters" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=600,y=90)
text1=Label(t,text="""Lord Karl Heisenberg (カール・ハイゼンベルク Kāru haizenberuku?) was a human mutant who lived in an Eastern European mountain range.
A genius in engineering,
he is presumably the patriarch of the Heisenberg family.
He runs the inherited Heisenberg Factory, located just outside the village,
and serves Mother Miranda,
along with the other three major houses in the mountain range.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=500,y=380)
text1.place(x=400,y=200)
p=PhotoImage(file='play.png')
text3=Label(t,text="""Heisenberg was one of the children who was kidnapped and subjected to the Cadou parasite experiments by Mother Miranda,
who tried to brainwash him into being her servant, with only limited success.
Eventually, he, Alcina Dimitrescu, Donna Beneviento, and Salvatore Moreau became Miranda's lieutenants.
Among the Lords of the Four Houses,
Heisenberg was the only one who held a grudge against Miranda,
due to her own selfish desire to revive her late daughter
and how he saw Miranda's family as nothing more than experiments.
As such, he secretly planned a rebellion, hoping to use Rose's latent powers to defeat Miranda.
At one point,he attempted to persuade Ethan to join him,
but the latter refused upon Heisenberg revealing his plan to weaponize Rose.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=450,y=430)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()
