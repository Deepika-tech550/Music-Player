from tkinter import *
from tkinter.tix import * #to import Balloon
from tkinter import filedialog as fd
from tkinter import messagebox
from pygame import mixer
from PIL import Image,ImageTk

root=Tk(className=' Music Player')
root.configure(bg="Brown")
global folder
folder=''
global value
value=True

lis=["D://Downloads//music//cinematic-dramatic-11120.mp3",
     "D://Downloads//music//fluidity-100-ig-edit-4558.mp3","D://Downloads//music//this-minimal-technology-12327.mp3" ]
global song
song="D://Downloads//music//cinematic-dramatic-11120.mp3"

v1=IntVar()
mixer.init()


root.geometry('500x500')
tip=Balloon(root)
img=PhotoImage(file='D:\\Downloads\\music\\music.png')

l2=Label(image=img)
l2.place(x=125,y=100)

def file():

   global folder
  
   file_folder=fd.askopenfile()
   folder=file_folder.name
   print(folder)
   
   

def play():
   global folder
   if folder=="":
      mixer.music.load("D://Downloads//music//cinematic-dramatic-11120.mp3")
      mixer.music.play()
   else:
      if folder:
         mixer.music
         mixer.music.load(folder)
         mixer.music.play()
         print('Music is Playing')
         
      else:
          messagebox.showinfo('Error','Select Directory')

def pause(is_value):
   
   if is_value==True:
      mixer.music.pause()
      global value
      value=False
   else:
      mixer.music.unpause()
      value=True
   
def stop():
    mixer.music.stop()
def speak():
   vol=v1.get()
   
   mixer.music.set_volume(vol)
def forward():
   global song
   if song in lis :
      pos=lis.index(song)
      new_pos=pos+1
      if new_pos<len(lis):
         mixer.music.load(lis[pos+1])
         mixer.music.play()
           
         song=lis[new_pos]
      else:
         pos=0
         song=lis[pos]
         new_pos=pos+1
         mixer.music.load(lis[pos])
         mixer.music.play()
         pos=pos+1
         
           
         

def backward():
   global song
   if song in lis :
      pos=lis.index(song)
      new_pos=pos-1
      if new_pos<len(lis):
         mixer.music.load(lis[pos-1])
         mixer.music.play()
           
         song=lis[new_pos]
      else:
         pos=0
         song=lis[pos]
         new_pos=pos-1
         mixer.music.load(lis[pos])
         mixer.music.play()
         pos=pos-1
         
   


l=Label(text='Music Player',font=('Cambria',34,'bold'),bg="Brown",fg="White")
l.place(x=130,y=20)

#Speaker
image1=Image.open('D:\\Downloads\\music\\speaker.png')
resimg1=image1.resize((60,60))
newimg1=ImageTk.PhotoImage(resimg1)
#Scale
b0=Button(image=newimg1,height=50,width=50,command=speak)
b0.place(x=60,y=400)
tip.bind_widget(b0,balloonmsg="Volume")
s=Scale(fg='Black',orient='vertical',from_=0,to_=1,variable=v1,width=2,length=51)
s.place(x=18,y=400)

#Backward
image2=Image.open('D:\\Downloads\\music\\backward.jpg')
resimg2=image2.resize((60,60))
newimg2=ImageTk.PhotoImage(resimg2)



# play button
image3=Image.open('D:\\Downloads\\music\\play.png')
resizeimg3=image3.resize((70,70))
newimg3=ImageTk.PhotoImage(resizeimg3)


#resume
image4=Image.open('D:\\Downloads\\music\\pause.png')
resimg4=image4.resize((60,60))
newimg4=ImageTk.PhotoImage(resimg4)

#stop
image5=Image.open('D:\\Downloads\\music\\stop.png')
resimg5=image5.resize((58,58))
newimg5=ImageTk.PhotoImage(resimg5)

#Forward
image6=Image.open('D:\\Downloads\\music\\forward.png')
resimg6=image6.resize((60,60))
newimg6=ImageTk.PhotoImage(resimg6)

#Buttons
b1=Button(image=newimg2,height=50,width=50,command=backward)
b1.place(x=130,y=400)
tip.bind_widget(b1, balloonmsg = "Backward")

b2=Button(image=newimg3,height=50,width=50,command=play)
b2.place(x=200,y=400)
tip.bind_widget(b2, balloonmsg = "PLAY")



b3=Button(image=newimg4,height=50,width=50,command=lambda:pause(value))
b3.place(x=270,y=400)
tip.bind_widget(b3, balloonmsg="RESUME & PLAY")


b4=Button(image=newimg6,height=50,width=50,command=forward)
b4.place(x=340,y=400)
tip.bind_widget(b4, balloonmsg = "Forward")

b5=Button(image=newimg5,height=50,width=50,command=stop)
b5.place(x=410,y=400)
tip.bind_widget(b5, balloonmsg = "STOP")

b6=Button(text='Open File',font=('Georgia',10,'bold'),bg='Yellow',command=file)
b6.place(x=210,y=260)




root.mainloop()
