from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('D-A-T-A-B-A-S-E  L-O-G-I-N ...')
root.configure(bg='orange')
root.resizable(False,False)
root.geometry('700x500+320+80')

def f1():
    a = e1.get();  b = e2.get()
    if(a=="" and b==""):
        messagebox.showwarning("Blank Login ...","Blanked Not Allowed")
    elif(a=="harsh" and b=="h1234"):
        messagebox.showinfo("Success","Login Success")
        root1 = Tk()
        root1.configure(bg="grey")
        root1.geometry('700x500+280+60')
        root1.resizable(False,False)
        root1.title('Connectivity To The World')
        l1 = Label(root1,text="... This is your entire world creation ...",bg='grey',fg='lime',
                    font="Cambria 18 bold",bd=4).place(x=100,y=50)
        b1 = Button(root1,text='Server 1',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey').place(x=240,y=140)
        b2 = Button(root1,text='Server 2',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey').place(x=240,y=200)
        b3 = Button(root1,text='Server 3',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey').place(x=240,y=260)
        b4 = Button(root1,text='Server 4',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey').place(x=240,y=320)
        b5 = Button(root1,text='Server 5',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey').place(x=240,y=380)
        root1.mainloop()
    else:
        messagebox.showerror("Invalid Login","Invalid Username and Password")

l1 = Label(root,text = "Welcome To Database ... ",font='Cambria 25 bold',
            fg='black',bg='orange',bd=4).place(x=120,y=50)
l2 = Label(root,text = "Username",font="Cambria 20 bold",
            fg='black',bg='orange',bd=4).place(x=120,y=160)
l3 = Label(root,text = "Password",font="Cambria 20 bold",
            fg='black',bg='orange',bd=4).place(x=120,y=250)
e1 = Entry(root,width=20,bd=4,fg='indigo',bg='light grey',font="Cambria 15 bold")
e1.place(x=300,y=160)
e2 = Entry(root,width=20,bd=4,fg='indigo',bg='lightgrey',font="Cambria 15 bold",show="*")
e2.place(x=300,y=250)
b1 = Button(root,text="Login",width=8,
            bd=6,height=2,font="Cambria 15 bold",fg='black',bg='orange',command=f1)
b1.place(x=120,y=350)

root.mainloop()
