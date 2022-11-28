# libraries
import pyttsx3
from tkinter import *
from tkinter import messagebox,filedialog,dialog,colorchooser
from tkinter.ttk import Combobox
import os
# Application setup
root = Tk()
root.resizable(False,False)
root.geometry("900x450+360+180")
root.title("Text To Speech Simulator")
root.configure(bg="#305065")

# functions
engine = pyttsx3.init() 
def color(event):
    cls = colorchooser.askcolor(title="Select Color")
    root.configure(bg=cls[1])

def speaknow():
    text=text_area.get(1.0, END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text=text_area.get(1.0, END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            engine.runAndWait()
    if(text):
        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

root.bind('<Control-g>',color)

#Application creation
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)
Top_Frame = Frame(root,bg="white",width=900,height=100)
Top_Frame.place(x=0,y=0)
Logo = PhotoImage(file="speaker.png")

Label(Top_Frame,image=Logo,bg="white",height=150).place(x=10,y=-25)
Label(Top_Frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)
Label(root,text="VOICE",bg="#305065",fg="white",font="arial 15 bold").place(x=580,y=160)
Label(root,text="SPEED",bg="#305065",fg="white",font="arial 15 bold").place(x=760,y=160)

text_area = Text(root,font="Roboto 20",bg="white",bd=4,fg="dark green",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

gender_box = Combobox(root,values=['Male','Female'],font="arial 14 bold",state='r',width=10) 
gender_box.set("Gender")
gender_box.place(x=550,y=200)

speed_box = Combobox(root,values=['Fast','Normal','Slow'],font="arial 14 bold",state='r',width=10) 
speed_box.set('Speed')
speed_box.place(x=730,y=200)

btn_icon1 = PhotoImage(file="speak.png")
btn = Button(root,text="Speak",compound=LEFT,image=btn_icon1,width=130,font="arial 14 bold",bg="light blue",fg="black",command=speaknow)
btn.place(x=550,y=280)
btn_icon2 = PhotoImage(file="download.png")
btn = Button(root,text="Download",compound=LEFT,image=btn_icon2,width=130,font="arial 12 bold",bg="#39c790",fg="black",command=download)
btn.place(x=730,y=280)

root.mainloop()
