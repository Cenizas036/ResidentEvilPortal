from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter
from pygame import mixer
import pygame
pygame.mixer.init()
mixer.init()
s1=pygame.mixer.Sound("lucas.mp3")
s1.play(loops=-1)
a="1.mp3"
mixer.music.load(a)
mixer.music.play()
def play():
    mixer.music.load("2.mp3")
    mixer.music.play()
t=tkinter.Tk()
t.title("RESIDENT EVIL PORTAL")
t.iconbitmap(r"RE.ico")
w=Canvas(t,bg="black",height=1000,width=3000)
l=Label(t,text="Lucas Baker Arc",font=("Times",30,"bold italic"))
img=ImageTk.PhotoImage(Image.open("lb.png"))
text=Label(t,text=""" "Daddy, right? You mind if I borrow Mommy for a little bit?
Well don't just stand there - do something! "  """,fg="white",bg="black",font=("Arial Bold",25),justify= LEFT)
text.place(x=400,y=90)
text1=Label(t,text="""The psychopathic killer .
Lucas himself is never a physical threat.
Jack, Marguerite, and Mia are all active, physical threats.
Lucas is always hiding, either hidden behind the other two (like at the dinner),
behind locked doors (once in the Old House and twice by the birthday room), or over video/audio feeds (the barn, the couple of TV appearances).
Make sure you play the vhs tape in the trailer to prepare.
Once again taking the role of Clancy the cameraman, Lucas will drag you into his “testing area”
to see if you’re smart enough to solve a puzzle. When he leaves, turn around and grab the Candle from the animatronic clown.
Go left into the kitchen area and then right through a doorway towards a birthday cake - which is promptly doused by water as you step through.
Lucas will taunt you and ask if you can figure out a way to place a lit candle on the cake.
Note the barrel and the locked cabinet in the room, and grab the Winding Key from the barrel and go back into the kitchen.
Use the stove to light the Candle, but don’t go back through.
Instead, walk past the monitors of a creepy birthday scene to the rope-locked door, and light it with your Candle.
Enter the next room and push past the balloons. The door here is password coded,
so instead search the floor for an unfilled yellow Balloon. Take it, and head back to the Kitchen.
Look for the drawing on the wall with a gas line in the wall and fill the balloon-surprise it’s full of
sharp things! You’ll obtain a Quill Pen, so head back to the animatronic clown to find he’s missing a finger to hold it.Check behind the clown to find a toilet and flush it so you can reach in
to find a Dirty Telescope. We need to clean it off, so stand in front of the cake doorway and use
the telescope - and walk forward to clean it off in the water dispersal, turning it into a regular
Telescope that seems to have a polarizing filter. Now go back to the kitchen and look at the TV
screens using the telescope and you’ll find three images highlighted - A hanged person, a
tombstone, and a baby. Return to the cake room and enter the password to open the cabinet to
find a Straw Doll. Take the Straw Doll to the stove and light it up to reveal a Dummy Finger that
can be inserted into the animatronic clown. Now give the clown the Quill Pen and Winding Key
and he’ll helpfully carve the password on you.Return to the balloon room and enter the newfound password to unlock the door and grab the Valve Handle.
Enter the cake room and look for a slot for the valve by the doorway to shut off the water, and finally light the candle one last time and place it on the cake.
""",fg="red",bg="black",font=("Times",15),justify=LEFT)
text1.place(x=300,y=200)
p=PhotoImage(file='play.png')
b = Button(t, image=p,height=90,width=80, command=play)
b.place(x=300,y=80)
l.pack()
w.pack()
ch=50
cw=200000
n=int(ch/4)
w.create_line(0,n,cw,n)
w.create_image(20,20,anchor=NW,image=img)
t.mainloop()



