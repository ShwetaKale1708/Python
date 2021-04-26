from tkinter import *
from pytube import YouTube
from os import getcwd,mkdir,chdir
root=Tk()
root.geometry('900x500')
root.resizable(0,0)
root.title("sms youtube video downloader")
label=Label(root,text="YouTube video downloader",bg="black",fg="green",font="Helvetika 40 bold",pady=30)
label.pack(fill=X)
f1=Frame(root,bg='black',height=900,width=900)
f1.pack()
Label(f1,text="paste a link below :",font="Helvetika 20 bold",bg="black",fg="white").place(x=320,y=20)
link=StringVar()
linkentry=Entry(f1,width=50,textvariable=link,fg="maroon4",font="helvetika 10 bold",bd=5).place(x=265,y=80)
def downloader():
       try:
           url=YouTube(str(link.get())) 
           video=url.streams.first() 
           try:
                mkdir("sms youtube downloader") 
           except FileExistsError:
                pass
           #video.download()
           t=getcwd()+"\sms youtube downloader" 
           chdir(t)
           video.download()
           path=getcwd()  
           text="your video is downloaded in....."+path
           Label(f1,text="DOWNLOAD COMPLETED...",font=" Helvetika 20 bold",bg="black",fg="VioletRed4").place(x=300,y=230)
           Label(f1,text=text,bg="black",fg="white",font="helvetika 10 bold").place(x=0,y=320)
       except :
           Label(f1,text="first paste a link..",font="Helvetika 15 bold",bg="black",fg="VioletRed4").place(x=300,y=230)

Button(f1,text="Download",font="Helvetika 18 bold",bg="blue4",fg="white",command=downloader).place(x=380,y=150)
root.mainloop()
