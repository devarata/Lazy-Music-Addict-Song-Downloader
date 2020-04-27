import tkinter as tk
from tkinter import StringVar
import os
import tkinter.messagebox as mb



def getSong(entry1,root):
    outF = open("C:\\Users\\devar\\Desktop\\gitprojects\\Lazy-Music-Addict-Song-Downloader\\output.txt","w")
    outF.write(entry1.get())
    outF.close()
    root.destroy()



def song_name(root,final_song):
    try:
        os.remove("C:\\Users\\devar\\Desktop\\gitprojects\\Lazy-Music-Addict-Song-Downloader\\output.txt")
    except OSError:
        pass
    canvas = tk.Canvas(root, width = 400, height = 300,  relief = 'raised',bg = "#ccffcc")
    canvas.pack()
    label1 = tk.Label(root, text='Song Downloader')
    label1.config(font=('helvetica', 14))
    label1.config(bg="#ccffcc")
    canvas.create_window(200, 25, window=label1)
    label2 = tk.Label(root, text='Type the song to download:')
    label2.config(font=('helvetica', 10))
    label2.config(bg = "#ccffcc")
    canvas.create_window(200, 100, window=label2)
    entry1 = tk.Entry(root)
    entry1.focus()
    canvas.create_window(200, 140, window=entry1)
    button1 = tk.Button(text='Download', command=lambda:getSong(entry1,root), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 180, window=button1)
    root.mainloop()



def song_name_func():
    root= tk.Tk()
    final_song = ""
    song_name(root,final_song)
    try:
        with open('C:\\Users\\devar\\Desktop\\gitprojects\\Lazy-Music-Addict-Song-Downloader\\output.txt','r') as f:
            final_song = f.readline()
    except FileNotFoundError:
            mb.showerror('Output','closed the box without entering anything')
    return final_song
