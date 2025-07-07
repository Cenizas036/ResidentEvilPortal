from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("e2.mp3")
s1.play(loops=-1)
mixer.music.load("1.mp3")
mixer.music.play()
def play():
    mixer.music.load("2.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Mother Miranda",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("23.png"))
text=Label(t,text="""  "You understand the love of a parent to her child.
Don't you?
How can you deny me?" """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=600,y=90)
text1=Label(t,text="""Miranda (ミランダ miranda) was an Eastern European biologist and cult leader who ruled over an isolated mountain village 
After losing her only daughter to the Spanish flu,
she discovered and became infected by the Mold within a nearby cave.
Gaining vast knowledge and superhuman powers from the infection,
she pioneered research on this mysterious fungus
and used it to conduct experiments on local villagers over the next century, hoping to find the perfect vessel to revive her daughter.
In February 2021, she abducted the infant Rosemary Winters for this purpose and,
seeing no further use for the villagers,
committed a genocide by unleashing Lycans on the local populace.
Miranda was ultimately killed by Rose's father Ethan Winters,
who had become intertwined with a BSAA operation to contain the outbreak.""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text2=Label(t,text="EARLY LIFE",fg="yellow",bg="black",font=("Verdana 20 bold"),justify=LEFT)
text2.place(x=600,y=500)
text1.place(x=430,y=250)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=500,y=80)
text3=Label(t,text="""Miranda was born sometime in the late 19th century in an agrarian mountain village in Eastern Europe.
1909, she gave birth to her first and only child, Eva. In 1919, the Spanish flu made its way to the village and devastated its population.
The death toll was so high that the cemetery was soon full to capacity,
forcing many survivors to bury their loved ones outside of the village, including the Potter's Field. Among those who perished in this pandemic was Eva, only 10 years old at the time of death
Driven to despair, Miranda ventured into a nearby cave wherein she intended to commit suicide.
However, before she could end her life, she came across a massive and ancient fungal super-colony,which she dubbed "the Mold".
Miranda touched a large mass growing from the Mold, the "Fungal Root", and in the process she saw the memories of hundreds,
if not thousands, of people who had been consumed by the fungus over the centuries.
Among those was Eva herself, whose body had been assimilated almost immediately after her burial.
Believing she could use the Mold to bring back her lost daughter, Miranda came to revere this substance as "the Black God".""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text3.place(x=20,y=550)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()
