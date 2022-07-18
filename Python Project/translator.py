from tkinter import *
import pyttsx3
root = Tk()
root.title('Text To Speech Translator')
root.geometry('700x500+260+80')
root.configure(bg='cyan')
root.resizable(False,False)
def f1():
    engine=pyttsx3.init()
    engine.say(e1.get())
    if(e1.get()==""):
        engine.say("Please write something here")
    engine.runAndWait()
    engine.stop()
l1 = Label(root,text="Text To Speech Translator",bg='cyan',fg='black',font='Cambria 25 bold').place(x=160,y=40)
l2 = Label(root,text="Enter The Text",bg='cyan',fg='black',font='Cambria 15 bold').place(x=270,y=100)
e1 = Entry(root,bd=6,width=30,bg='light gray',fg='indigo',font='Cambria 10 bold')
e1.place(x=230,y=160)
b1 = Button(root,text='Speech The Text',bd=4,width=20,bg='cyan',fg='black',font='Cambria 15 bold',command=f1)
b1.place(x=230,y=220)
root.mainloop()
