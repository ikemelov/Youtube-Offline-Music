import tkinter as tk
from tkinter import *
from tkinter import filedialog
#from pytube import YouTube
from pytube import Playlist
from tkinter import filedialog, messagebox
import os


def widgets():
    link_label = Label(root, text= "YouTube Playlist Link: ",
                bg= "#E62C2C", fg="#ffffff")
    link_label.grid(row=1, column= 0, padx= 5, pady= 5)

    root.p_link = Entry(root, textvariable= playlist_link, width= 60)
    root.p_link.grid(row= 2, column= 0, padx= 5, pady= 5)

    destination_label = Label(root, text= "Destination: ",
                bg= "#E62C2C", fg="#ffffff")
    destination_label. grid(row=14, column= 0, padx= 5, pady= 5)

    root.destination_path = Entry(root, textvariable= download_path, 
                            width= 55)
    root.destination_path.grid(row= 15, column= 0, padx= 5, pady= 5)

    browse_button = Button(root, text= "Browse",width= 10,
                    bg= "#00992B", command= browse)
    browse_button.grid(row= 15, column= 1, padx= 5, pady= 5)


    download_button = Button(root, text= "Download",width= 10,
                    bg= "#00992B", command= download_playlist)
    download_button.grid(row= 16, column= 0, padx= 5, pady= 5)


def browse():
    download_dir = filedialog.askdirectory(initialdir= "Your directory path: ")
    download_path.set(download_dir)


def download_playlist():
    url = playlist_link.get()
    folder = download_path.get()
    yt_playlist = Playlist(url)
    for video in yt_playlist.videos:
        video.streams.first().download(folder)

    
    messagebox.showinfo("done")


def rename_files():
    url = playlist_link.get()
    folder = download_path.get()
    files = os.listdir(folder)

    # Changing file extension from video format to mp3 format
    for file_name in files:
        old_name = os.path.join(folder, file_name)
        new_name = old_name.replace('.3gpp', '.mp3')
        os.rename(old_name, new_name)



root = tk.Tk()

# Handling window styling and funtionality
# size of the window
root.geometry("700x400")

# restricting resize fuction
root.resizable(False, False)
# Title of the application
root.title("Liam's Offline Youtube Playlist Downloader")
# Color palette
root.config(background = "#222222")

playlist_link = StringVar()
download_path = StringVar()

# Draw labels
widgets()

root.mainloop()

rename_files()