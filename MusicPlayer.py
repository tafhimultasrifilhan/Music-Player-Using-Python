from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import time
from pygame import mixer
import os


root=Tk()
root.title("PyPlayer")
root.geometry('640x500')
root.resizable(False,False)
root.config(bg="#000000")

mixer.init()

def song():
	a=filedialog.askopenfilename()
	mixer.music.load(a)
	mixer.music.set_volume(0.05)
	mixer.music.play()
	x=os.path.basename(a)
	sn.config(text=x)
def play():
	mixer.music.unpause()
def pause():
	mixer.music.pause()		
def vup():
	a=mixer.music.get_volume()
	b=a+0.01
	mixer.music.set_volume(b)
def vdn():
	f=mixer.music.get_volume()
	e=f-0.005
	mixer.music.set_volume(e)

menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar,tearoff=False)

# add a menu item to the menu
file_menu.add_command(
    label='Open',
    command=song
)
menubar.add_cascade(
    label="File",
    menu=file_menu
)

h1=Label(text="PyPlayer",font=('Firenze SF',30),bg="#000000",fg="#ffffff").pack()
photo = PhotoImage(file="yo.png")
img = Label(image=photo,bg="#000000")
img.pack(pady=20)

sn=Label(root)
sn.config(text="",bg="#000000",fg="#ffffff",font=("Atma Medium",20))
sn.pack()

canvas = Canvas(root, background = "#D2D2D2",width = 500, height = 7)
progbar=ttk.Progressbar(canvas,orient=HORIZONTAL,length=500,mode="determinate")
canvas.create_window(1, 1, anchor=NW, window=progbar)
canvas.pack()


play=Button(text="▶️",font=("EmojiOne",25),fg="#ffffff",bg="#000000",activebackground="black",activeforeground="#ffffff",bd=0,command=play).place(relx = 1, x =-400, y = 370)
pause=Button(text="⏸️",font=("EmojiOne",25),fg="#ffffff",bg="#000000",activebackground="black",activeforeground="#ffffff",bd=0,command=pause).place(relx = 1, x =-300, y = 370)
vu=Button(text="🔊",font=("EmojiOne",15),fg="#ffffff",bg="#000000",activebackground="black",activeforeground="#ffffff",bd=0,command=vup).place(relx = 1, x =-100, y = 380)
vd=Button(text="🔈",font=("EmojiOne",15),fg="#ffffff",bg="#000000",activebackground="black",activeforeground="#ffffff",bd=0,command=vdn).place(relx = 1, x =-570, y = 380)
root.mainloop()