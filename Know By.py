from curses.textpad import Textbox
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
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
        def f1():
            root2 = Tk()
            root2.configure(bg="grey")
            root2.geometry('700x500+350+100')
            root2.resizable(False,False)
            root2.title("Server 1 ...")

            def m1():
                root3 = Tk()
                root3.title('Editor ...')
                root3.configure(bg='white')
                root3.geometry('700x500+100+50')
                def fm1():
                    root4 = Tk()
                    root4.title('New File')
                    root4.geometry('700x500+100+50')
                    t1 = Text(root4,bd=6,bg='light grey',fg='black',width=116,height=36,
                        font='Fixedys 12 bold').place(x=0,y=0)
                    root4.mainloop()
                t1 = Text(root3,bd=6,bg='light grey',fg='black',width=116,height=34,
                        font='Fixedys 12 bold').place(x=0,y=0)
                main_menu = Menu(root3,bg='white')
                root3.config(menu = main_menu)
                filemenu = Menu(main_menu,bg='white')
                main_menu.add_cascade(label='File', menu = filemenu)
                filemenu.add_command(label='Open File')
                filemenu.add_command(label='Open New File',command=fm1)
                filemenu.add_separator()
                filemenu.add_command(label='Save')
                filemenu.add_command(label='Save as')
                sm1 = Menu(filemenu,bg='white')
                filemenu.add_cascade(label='Command Line',menu=sm1)
                sm1.add_command(label='(Terminal) >_')
                sm1.add_separator()
                sm1.add_command(label='Commands Instructions')
                root3.mainloop()

            b1 = Button(root2,text='Data Access',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b1.place(x=20,y=30)
            b2 = Button(root2,text='Server Request',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b2.place(x=20,y=110)
            b3 = Button(root2,text='Data Transfer',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b3.place(x=20,y=190)
            b4 = Button(root2,text='Address Transfer',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b4.place(x=20,y=270)
            b5 = Button(root2,text='Requirements',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b5.place(x=20,y=350)
            b6 = Button(root2,text='Error Detection',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b6.place(x=20,y=430)
            b7 = Button(root2,text='Issue',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b7.place(x=370,y=30)
            b8 = Button(root2,text='Connection',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b8.place(x=370,y=110)
            b9 = Button(root2,text='Server Manager',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b9.place(x=370,y=190)
            b10 = Button(root2,text='Task Complete',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b10.place(x=370,y=270)
            b11 = Button(root2,text='Editor',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold',
                    command=m1); b11.place(x=370,y=350)
            b12 = Button(root2,text='Details',width=20,bd=4,bg='grey',
                    fg='indigo',font='Cambria 15 bold'); b12.place(x=370,y=430)
            root2.mainloop()
        def f2():
            root3 = Tk()
            root3.configure(bg="grey")
            root3.geometry('700x500+350+100')
            root3.resizable(False,False)
            root3.title("Server 2 ...")
            
            def g1():
                a = [100,200,300,400]
                b = [15.6,34.899,23.78,44.567]
                c = [110,250,350,400]
                d = [25,23.678,40,40]
                plt.plot(a,b,color='g')
                plt.plot(c,d,color='r')
                plt.xlabel('Stock Market Product Values')
                plt.ylabel('Stock Percentage as per currency for different countries')
                plt.title('Stock Market Investment Graph')
                plt.show()
            def g2():
                a = ['USA','India','North Korea','Japan','Germany','China']
                b = [96.42,86.788,91.34,67.2,78.04,81.448]
                c = [95,45,73,57.98,88.612,99.873]
                plt.plot(a,b,color='y')
                plt.plot(a,c,color='g')
                plt.xlabel('Country')
                plt.ylabel('Percentage to sold the products in year 2021')
                plt.title('Graph to show Product Demand in last year 2021 (green-buy the product)'
                           ' and (yellow-sold the product)')
                plt.show()
                
            l1 = Label(root3,text = 'In this Server, we have to recognize the graph \n'
                                    'in different formation with four different stacks \n'
                                    'and it shows best way to find out the information.\n',
                font='Cambria 15',bg='grey',fg='cyan').place(x=100,y=20)
            l2 = Label(root3,text='Stock Market',font='Cambria 15',bg='grey',
                        fg='cyan').place(x=190,y=150)
            l3 = Label(root3,text='Country Products',font='Cambria 15',bg='grey',
                        fg='cyan').place(x=190,y=230)
            l4 = Label(root3,text='Car Sold',font='Cambria 15',bg='grey',
                        fg='cyan').place(x=190,y=310)
            l5 = Label(root3,text='Technology',font='Cambria 15',bg='grey',
                        fg='cyan').place(x=190,y=390)
            b1 = Button(root3,text='Graph 1',bg='grey',fg='indigo',width=10,
                        bd=4,font='Cambria 15 bold',command=g1).place(x=400,y=150)
            b2 = Button(root3,text='Graph 2',bg='grey',fg='indigo',width=10,
                        bd=4,font='Cambria 15 bold',command=g2).place(x=400,y=230)
            b3 = Button(root3,text='Graph 3',bg='grey',fg='indigo',width=10,
                        bd=4,font='Cambria 15 bold').place(x=400,y=310)
            b4 = Button(root3,text='Graph 4',bg='grey',fg='indigo',width=10,
                        bd=4,font='Cambria 15 bold').place(x=400,y=390)
            root3.mainloop()
        def f3():
            root4 = Tk()
            root4.configure(bg="grey")
            root4.geometry('700x500+350+100')
            root4.title("Server 3 ...")
            root4.resizable(False,False)
            root4.mainloop()
        def f4():
            root5 = Tk()
            root5.configure(bg="grey")
            root5.geometry('700x500+350+100')
            root5.title("Server 4 ...")
            root5.resizable(False,False)
            root5.mainloop()
        def f5():
            root6 = Tk()
            root6.configure(bg="grey")
            root6.geometry('700x500+350+100')
            root6.title("Server 5 ...")
            root6.resizable(False,False)
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
            fg='black',bg='orange',bd=4).place(x=120,y=50)
l2 = Label(root,text = "Username",font="Cambria 20 bold",
            fg='black',bg='orange',bd=4).place(x=120,y=160)
l3 = Label(root,text = "Password",font="Cambria 20 bold",
            fg='black',bg='orange',bd=4).place(x=120,y=250)
s1 = StringVar()
s2 = StringVar()
e1 = Entry(root,textvariable=s1,width=20,bd=4,fg='indigo',bg='light grey',font="Cambria 15 bold")
e1.place(x=300,y=160)
s1.set('harsh')
e2 = Entry(root,textvariable=s2,width=20,bd=4,fg='indigo',bg='lightgrey',font="Cambria 15 bold",show="*")
e2.place(x=300,y=250)
s2.set('h1234')
b1 = Button(root,text="Login",width=8,
            bd=6,height=2,font="Cambria 15 bold",fg='black',bg='orange',command=f1)
b1.place(x=120,y=350)
b2 = Button(root,text="Cancel",width=8,
            bd=6,height=2,font="Cambria 15 bold",fg='black',bg='orange',command=root.destroy)
b2.place(x=340,y=350)
root.mainloop()
