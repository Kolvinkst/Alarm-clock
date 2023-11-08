from datetime import datetime
import pyglet
import os
from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Alarm clock")
root.geometry("800x600")





#def dwnld():



label_download = Label(text="Download songs:")
label_download.grid(row=0, column=0)
btn_dwnld = Button(root, text="Select and download", bg="green", fg="white")
btn_dwnld.grid(row=0, column=1, columnspan=1, pady=5, sticky=NSEW)


mus_dir = "songs"

songs = os.listdir(mus_dir)


label_songs = Label(text="Select song:")
label_songs.grid(row=1, column=0)
combobox = ttk.Combobox(values=songs)
combobox.grid(row=2, column=0)

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

label_hours = Label(text="Set hours:")
label_hours.grid(row=3, column=0)
inp_h = Entry(root, textvariable=hours)
inp_h.grid(row=4, column=0)
label_min = Label(text="Set minutes:").grid(row=3, column=1)
inp_min = Entry(root, textvariable=minutes)
inp_min.grid(row=4, column=1)
label_sec = Label(text="Set seconds:").grid(row=3, column = 2)
inp_sec = Entry(root, textvariable=seconds)
inp_sec.grid(row=4, column=2)




def start_play():
    while True:
        time.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        set_time = f"{hours.get()}:{minutes.get()}:{seconds.get()}"
        song = combobox.get()
        muz = pyglet.resource.media("songs/" + song)
        if (current_time >= set_time):
            muz.play()
            pyglet.app.run()
            break

btn = Button(root, text="Start", bg="green", fg="white", command=start_play)
btn.grid(row=5, column=0, columnspan=3, pady=5, sticky=NSEW)

root.mainloop()