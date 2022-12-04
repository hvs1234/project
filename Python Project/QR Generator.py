#libraries
from tkinter import *
from tkinter import messagebox,colorchooser,dialog,simpledialog,filedialog
from qrcode import *

#set up window
root = Tk()
root.resizable(False,False)
root.geometry('1000x550+280+50')
root.title('QR Generator')
root.configure(bg="#AE2321")
image_icon = PhotoImage(file="E:\\pyImages\\qrcode.png")
root.iconphoto(False,image_icon)

#functions
def color(event):
    cls = colorchooser.askcolor(title="Select color to change")
    root.configure(bg=cls[1])
    l1.config(bg=cls[1])
    l2.config(bg=cls[1])
    b1.config(bg=cls[1])
    b2.config(bg=cls[1])

def generate():
    global qr
    a = e1.get()
    b = e2.get()
    if(a=="" and b==""):
        messagebox.showwarning("Blank Detail","Blank Not Allowed ...")
    else:
        if(a=="" or b==""):
            messagebox.showwarning("Blank Detail","Blank Not Allowed ...")
        else:
            qr = make(b)
            qr.save("QRimages/"+str(a)+".png")
            global img
            img = PhotoImage(file="QRimages/"+str(a)+".png")
            view_qr.config(image=img)    

#build up app
l1 = Label(root,text="Title",fg="white",bg="#AE2321",font="arial 25 bold")
l1.place(x=50,y=140)
l2 = Label(root,text="QR Generator Here ...",fg="white",bg="#AE2321",font="arial 25 bold")
l2.place(x=50,y=60)
e1 = Entry(root,width=13,font="arial 15 bold",fg="indigo",bg="light blue",bd=4)
e1.place(x=50,y=210)
e2 = Entry(root,width=28,font="arial 15 bold",fg="indigo",bg="light blue",bd=4)
e2.place(x=50,y=290)
b1 = Button(root,text="Generate",fg="white",bg="black",bd=4,width=20,height=2,command=generate)
b1.place(x=50,y=360)
b2 = Button(root,text="Exit",fg="white",bg="black",bd=4,width=20,height=2,command=root.destroy)
b2.place(x=50,y=430)
view_qr = Label(root,bg="#AE2321")
view_qr.pack(padx=50,pady=10,side=RIGHT)

root.bind('<Control-g>',color)
root.mainloop()
