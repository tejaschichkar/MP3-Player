import pygame

import tkinter as tkr

from tkinter.filedialog import askdirectory

import os

musicplayer = tkr.Tk()

musicplayer.geometry('450x350')

musicplayer.title("Music Player")

directory = '/storage/emulated/0/MP3 /' #path of directory to search music

os.chdir(directory)

songlist = os.listdir()

playlist = tkr.Listbox(musicplayer, font ="Cambria 14 bold", bg="cyan", selectmode = tkr.SINGLE)

for item in songlist:

 pos=0

 playlist.insert(pos, item)

 pos = pos + 1

pygame.init()

pygame.mixer.init()

def play():

    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))

    var.set(playlist.get(tkr.ACTIVE))

    pygame.mixer.music.play()

 

def ExitMusicPlayer():

    pygame.mixer.music.stop()

 

def pause():

    pygame.mixer.music.pause()

 

def resume():

    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicplayer, width=4, height=2, font="Cambria 10 bold", text="Play", command=play, bg="lime green", fg="black")

Button2 = tkr.Button(musicplayer, width=4, height=2, font="Cambria 10 bold", text="Stop", command=ExitMusicPlayer, bg="red", fg="black")

Button3 = tkr.Button(musicplayer, width=2, height=4, font="Cambria 6 bold", text="Pause",command=pause, bg="yellow", fg="black")

Button4 = tkr.Button(musicplayer, width=2, height=4, font="Cambria 6 bold", text="Resume", command=resume, bg="skyblue", fg="black")

var = tkr.StringVar()

songtitle = tkr.Label(musicplayer, 

font="Helvetica 12 bold", textvariable=var, bg='white')

songtitle.place(relx = 0.5, rely = 0.8, anchor = 'center')

Button1.pack(side='top', fill='x')

Button2.pack(side='bottom', fill='x')

Button3.pack(side='left', fill='y')

Button4.pack(side='right', fill='y')

playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()
