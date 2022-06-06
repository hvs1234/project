from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('D-A-T-A-B-A-S-E  L-O-G-I-N ...')
root.configure(bg='cyan')
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
        def f1():
            root2 = Tk()
            root2.configure(bg="grey")
            root2.geometry('700x500+350+100')
            root2.title("Server 1 ...")
            b1 = Button(root2,text='Access Portal',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b1.place(x=20,y=30)
            b2 = Button(root2,text='Server Components',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b2.place(x=20,y=110)
            b3 = Button(root2,text='Data Transfer',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b3.place(x=20,y=190)
            b4 = Button(root2,text='Address Transfer',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b4.place(x=20,y=270)
            b5 = Button(root2,text='Request Accept',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b5.place(x=20,y=350)
            b6 = Button(root2,text='Task Complete',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b6.place(x=20,y=430)
            b7 = Button(root2,text='Recheck Server Data',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b7.place(x=370,y=30)
            b8 = Button(root2,text='Error Detection',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b8.place(x=370,y=110)
            b9 = Button(root2,text='Issue',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b9.place(x=370,y=190)
            b10 = Button(root2,text='Security',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b10.place(x=370,y=270)
            b11 = Button(root2,text='Definition Manager',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b11.place(x=370,y=350)
            b12 = Button(root2,text='Details',width=20,font="Cambria 15 bold",bd=4,
                        bg='grey',fg='indigo'); b12.place(x=370,y=430)
            root2.mainloop()
        def f2():
            root3 = Tk()
            root3.configure(bg="grey")
            root3.geometry('700x500+350+100')
            root3.title("Server 2 ...")
            root3.mainloop()
        def f3():
            root4 = Tk()
            root4.configure(bg="grey")
            root4.geometry('700x500+350+100')
            root4.title("Server 3 ...")
            root4.mainloop()
        def f4():
            root5 = Tk()
            root5.configure(bg="grey")
            root5.geometry('700x500+350+100')
            root5.title("Server 4 ...")
            root5.mainloop()
        def f5():
            root6 = Tk()
            root6.configure(bg="grey")
            root6.geometry('700x500+350+100')
            root6.title("Server 5 ...")
            root6.mainloop()
        l1 = Label(root1,text="... This is your entire world creation ...",bg='grey',fg='lime',
                    font="Cambria 18 bold",bd=4).place(x=100,y=50)
        b1 = Button(root1,text='Server 1',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey',command=f1).place(x=240,y=140)
        b2 = Button(root1,text='Server 2',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey',command=f2).place(x=240,y=200)
        b3 = Button(root1,text='Server 3',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey',command=f3).place(x=240,y=260)
        b4 = Button(root1,text='Server 4',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1,
                    bg='grey',command=f4).place(x=240,y=320)
        b5 = Button(root1,text='Server 5',font='Cambria 10 bold',fg='lime',bd=4,width=20,height=1, 
                    bg='grey',command=f5).place(x=240,y=380)
        root1.mainloop()
    else:
        messagebox.showerror("Invalid Login","Invalid Username and Password")

l1 = Label(root,text = "Welcome To Database ... ",font='Cambria 25 bold',
            fg='black',bg='cyan',bd=4).place(x=120,y=50)
l2 = Label(root,text = "Username",font="Cambria 20 bold",
            fg='black',bg='cyan',bd=4).place(x=120,y=160)
l3 = Label(root,text = "Password",font="Cambria 20 bold",
            fg='black',bg='cyan',bd=4).place(x=120,y=250)
e1 = Entry(root,width=20,bd=4,fg='indigo',bg='light grey',font="Cambria 15 bold")
e1.place(x=300,y=160)
e2 = Entry(root,width=20,bd=4,fg='indigo',bg='lightgrey',font="Cambria 15 bold",show="*")
e2.place(x=300,y=250)
b1 = Button(root,text="Login",width=8,
            bd=6,height=2,font="Cambria 15 bold",fg='black',bg='cyan',command=f1)
b1.place(x=120,y=350)
b2 = Button(root,text="Cancel",width=8,
            bd=6,height=2,font="Cambria 15 bold",fg='black',bg='cyan',command=root.destroy)
b2.place(x=340,y=350)
root.mainloop()
