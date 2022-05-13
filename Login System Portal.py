from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('800x500+300+60')
root.resizable(False,False)
root.title('Login ...')
root.configure(bg='orange')
# ------------------------------------------------------------------------------------------------------
def f1():
    a = e1.get();  b = e2.get();
    if(a=="" and b==""):
        messagebox.showwarning('Blanked Login ...','BLanked Not Allowed !')
    elif(a=="harsh" and b=="h1234"):
        messagebox.showinfo('Login','Login Success')
        root1 = Tk()
        root1.geometry('800x500+280+40')
        root1.resizable(False,False)
        root1.configure(bg="gray")
        root1.title('All Learning Platform')
        # ----------------------------------------------------------------------------------------------
        fr1 = Frame(root1,bg='light gray',bd=10,
                width = 300, height = 300).place(x=20,y=20)
        root1.mainloop()
    else:
        messagebox.showerror('Invalid Login','Invalid username and Password')

def f2():
    root2 = Tk()
    root2.geometry('400x150+600+150')
    root2.title('...');  root2.resizable(False,False)
    root2.configure(bg='sky blue')
    l1 = Label(root2,text='Note:- Every time login will be reset.\n It is neccessary to enter\n'
    ' username or password, otherwise blanked\n username or password is not\n allowed. When you will fill correct'
    ' username\n or password then click "Keep me logged in ..."',font='Cambria 10 bold',bg='sky blue',
    fg='indigo').place(x=20,y=20)
    root2.mainloop()

# ------------------------------------------------------------------------------------------------------
l1 = Label(root,text = 'L-O-G-I-N ...',bg='orange',fg='black',font='Cambria 30 bold').place(x=140,y=60)
l2 = Label(root,text = 'Username ',
            bg='orange',fg='black',font='Cambria 15 bold').place(x=140,y=170)
l3 = Label(root,text = 'Password ',
            bg='orange',fg='black',font='Cambria 15 bold').place(x=140,y=260)
# -------------------------------------------------------------------------------------------------------
s1 = StringVar();
s2 = StringVar();
e1 = Entry(root,textvariable=s1,
        bd=4,fg='indigo',bg='light gray',font='Cambria 10 bold',width=40); e1.place(x=280,y=170)
s1.set('harsh')
e2 = Entry(root,textvariable = s2,bd=4,fg='indigo',bg='light gray',show="*",font='Cambria 10 bold',width=40
            ); e2.place(x=280,y=260)
s2.set('h1234')
# -------------------------------------------------------------------------------------------------------
chk1 = Checkbutton(root,text = ' Keep me logged in ...',font='Cambria 12 bold',bg='orange',fg='black'
        ).place(x=140,y=340)
# -------------------------------------------------------------------------------------------------------
b1 = Button(root,text = 'Login',width=6,bg='orange',fg='black', command = f1,
            font='Cabria 15 bold',bd=4); b1.place(x=140,y=410)
b2 = Button(root,text = 'Cancel',width=6,bg='orange',fg='black',font='Cabria 15 bold',bd=4,
            command = root.destroy); b2.place(x=300,y=410)
b3 = Button(root,text='...',fg='black',bg='orange',bd=4,width=1,
            command = f2).place(x=700,y=410)
root.mainloop()
