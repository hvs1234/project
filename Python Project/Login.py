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
         
    else:
        messagebox.showerror('Invalid Login','Invalid username and Password')

# ------------------------------------------------------------------------------------------------------
l1 = Label(root,text = 'L-O-G-I-N ...',bg='orange',fg='black',font='Cambria 30 bold').place(x=140,y=60)
l2 = Label(root,text = 'Username ',bg='orange',fg='black',font='Cambria 15 bold').place(x=140,y=170)
l3 = Label(root,text = 'Password ',bg='orange',fg='black',font='Cambria 15 bold').place(x=140,y=260)
# -------------------------------------------------------------------------------------------------------
#s1 = StringVar()
e1 = Entry(root,bd=4,fg='indigo',bg='light gray',font='Cambria 10 bold',width=40); e1.place(x=280,y=170)
#s1.set("harsh")
#s2 = StringVar()
e2 = Entry(root,bd=4,fg='indigo',bg='light gray',font='Cambria 10 bold',width=40,
            show="*"); e2.place(x=280,y=260)
#s2.set("h1234")
# -------------------------------------------------------------------------------------------------------
chk1 = Checkbutton(root,text = ' Keep me logged in ...',font='Cambria 12 bold',bg='orange',fg='black'
        ).place(x=140,y=340)
# -------------------------------------------------------------------------------------------------------
b1 = Button(root,text = 'Login',width=6,bg='orange',fg='black', command = f1,
            font='Cabria 15 bold',bd=4); b1.place(x=140,y=410)
b2 = Button(root,text = 'Cancel',width=6,bg='orange',fg='black',font='Cabria 15 bold',bd=4,
            command = root.destroy); b2.place(x=300,y=410)
root.mainloop()
