from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Kishlay-YouTube_Video_Downloader")
Label(root,text = 'YouTube Video Downloader', font='arial 20 bold ',foreground='red' ).pack()
 

#link portal
link = StringVar()

Label(root,text='Paste Your Link Here:',font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32 , y=90)

#function to download
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download( output_path="C:\\Users\\kishl\\Downloads") # put path where you want to download video
    Label(root,  text='DOWNLOAD', font='arial 15').place(x=180, y=210)
Button(root,text='DOWNLOAD', font='arial 15 bold', bg='light green', padx=2, command=Downloader).place(x=180 , y=150)
root.mainloop()
