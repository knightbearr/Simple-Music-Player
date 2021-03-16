# ---IMPORT PACKAGE---
from tkinter import *
from PIL import ImageTk,Image
import pygame

# ---TKINTER---
root = Tk()
root.title('Music Player')
root.geometry('1000x500')

# ---IMAGE---
bg = PhotoImage(file='twice.png')
bg1 = PhotoImage(file='twice2.png')
lbl = Label(root, image=bg)
lbl1 = Label(root, image=bg1)
lbl2 = Label(root, padx=10, pady=500, bg='grey')
lbl.place(x=0, y=0)
lbl1.place(x=300, y=0)
lbl2.place(x=300, y=0)

# ---DEFINE PYGAME---
pygame.mixer.init()

# ---SONG FUNCTION---
def play1():
    pygame.mixer.music.load('TWICE - BEHIND THE MASK.mp3')
    pygame.mixer.music.play(loops=0) # EXAMPLE 1

def play2():
    pygame.mixer.music.load('TWICE - DEPEND ON YOU.mp3')
    pygame.mixer.music.play(loops=0)

def play3():
    pygame.mixer.music.load('TWICE - HANDLE IT.mp3')
    pygame.mixer.music.play(loops=0)

def play4():
    pygame.mixer.music.load('TWICE - HELL IN HEAVEN.mp3')
    pygame.mixer.music.play(loops=0)

def play5():
    pygame.mixer.music.load("\TWICE - I CAN'T STOP ME.mp3")
    pygame.mixer.music.play(loops=0)

def play6():
    pygame.mixer.music.load('TWICE - UP NO MORE.mp3')
    pygame.mixer.music.play(loops=0)

# ---STOP AND PLAY FUNCTION---
def stop():
    pygame.mixer.music.pause()

def play():
    pygame.mixer.music.play()

# ---CREATE BUTTON IMAGE---
bg2 = PhotoImage(file='04 - Photo\\1.png')
bg3 = PhotoImage(file='04 - Photo\\2.png')
bg4 = PhotoImage(file='04 - Photo\\3.png')
bg5 = PhotoImage(file='04 - Photo\\4.png')
bg6 = PhotoImage(file='04 - Photo\\5.png')
bg7 = PhotoImage(file='04 - Photo\\6.png')
bg8 = PhotoImage(file='04 - Photo\\7.png')
bg9 = PhotoImage(file='04 - Photo\\8.png')

# ---SET BUTTON---
btn1 = Button(root, image=bg2, bd=0, command=play1)
btn2 = Button(root, image=bg3, bd=0, command=play2)
btn3 = Button(root, image=bg4, bd=0, command=play3)
btn4 = Button(root, image=bg5, bd=0, command=play4)
btn5 = Button(root, image=bg6, bd=0, command=play5)
btn6 = Button(root, image=bg7, bd=0, command=play6)
btn7 = Button(root, image=bg8, bd=0, command=play)
btn8 = Button(root, image=bg9, bd=0, command=stop)

# ---CREATE A LABEL NAME---
label1 = Label(root, text='Twice - Behind The Mask')
label2 = Label(root, text='Twice - Depend On You')
label3 = Label(root, text='Twice - Handle It')
label4 = Label(root, text='Twice - Hell In Heaven')
label5 = Label(root, text="Twice - I Can't Stop Me")
label6 = Label(root, text='Twice - Up No More')

# ---ADJUST THE LABEL---
label1.place(x=405,y=210)
label2.place(x=610,y=210)
label3.place(x=830,y=210)
label4.place(x=414,y=420)
label5.place(x=610,y=420)
label6.place(x=820,y=420)

# ---ADJUST THE BUTTON---
btn1.place(x=400,y=50)
btn2.place(x=600,y=50)
btn3.place(x=800,y=50)
btn4.place(x=400,y=260)
btn5.place(x=600,y=260)
btn6.place(x=800,y=260)
btn7.place(x=335,y=400)
btn8.place(x=335,y=450)

# ---MAINLOOP---
root.mainloop()
