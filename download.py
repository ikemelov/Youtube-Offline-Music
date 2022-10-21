from tkinter import *
from tkinter import filedialog

screen = Tk()
title = screen.title('Youtube Offline Music')
canvas = Canvas(screen, width = 500, height = 500)
canvas.pack()

link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter the link: ", font = ("Arial"))

canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)

screen.mainloop()
