
from tkinter import *
from tkinter import colorchooser,filedialog,simpledialog
from tkinter.font import Font
class texteditor:
    def color(self):
        cls = colorchooser.askcolor(title = "Select Color")
        root.config(bg=cls[1])
        self.t1.config(bg=cls[1])
        self.sc1.config(bg=cls[1])
        self.main_menu.config(bg=cls[1])
        self.file_menu.config(bg=cls[1])
        self.edit_menu.config(bg=cls[1])
        self.font_menu.config(bg=cls[1])

    current_file = "no_file"
    def openfile(self):
        of = filedialog.askopenfile(initialdir="/",filetypes=(("Text Files",".txt"),("Python File",".py")
        ,("Java Files",".java"),("C++ Files",".cpp"),("C Files",".c"),("All Files","*.*")),
        title="Select Files To Open")
        if(of!=NONE):
            self.t1.delete(1.0,END)
            for line in of:
                self.t1.insert(END,line)
            self.current_file = of.name
        of.close()

    def openfile1(self,event):
        of = filedialog.askopenfile(initialdir="/",filetypes=(("Text Files",".txt"),("Python File",".py")
        ,("Java Files",".java"),("C++ Files",".cpp"),("C Files",".c"),("All Files","*.*")),
        title="Select Files To Open")
        if(of!=NONE):
            self.t1.delete(1.0,END)
            for line in of:
                self.t1.insert(END,line)
            self.current_file = of.name
        of.close()

    def saveasfile(self):
        sf = filedialog.asksaveasfile(mode="w",defaultextension=(".txt","*.*"),
        title="Select Files To Save")
        if sf is NONE:
            return
        textsave = self.t1.get(1.0,END)
        self.current_file = sf.name
        sf.write(textsave)
        sf.close()

    def saveasfile1(self,event):
        sf = filedialog.asksaveasfile(mode="w",defaultextension=(".txt","*.*"),
        title="Select Files To Save")
        if sf is NONE:
            return
        textsave = self.t1.get(1.0,END)
        self.current_file = sf.name
        sf.write(textsave)
        sf.close()

    def savefile(self):
        if(self.current_file=="no_file"):
            self.saveasfile()
        else:
            f = open(self.current_file, 'w+')
            f.write(self.t1.get(1.0,END))
            f.close()
         
    def newfile(self):
        self.t1.delete(1.0,END)
        self.current_file = "no_file"

    def copytext(self):
        pass
     
    def cuttext(self):
        pass
    
    def pastetext(self):
        pass

    def __init__(self,master):
        self.master = master
        master.title("Text Editor (created by - HVS)")
        master.configure(bg="#004854")
        master.geometry('700x500+340+80')

        self.sc1 = Scrollbar(master,bg="#004854");
        self.sc1.pack(fill=Y,side=RIGHT)

        self.t1 = Text(master,bd=4,bg="#004854",fg="white",yscrollcommand=self.sc1.set,wrap=WORD); 
        self.sc1.config(command=self.t1.yview)
        self.t1.pack(fill=BOTH,expand=1)
        

        self.main_menu = Menu(master,bg="#004854",fg="lime",tearoff=False);
        master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu,bg="#004854",fg="lime",tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="Open File",command=self.openfile)
        self.file_menu.add_command(label="New File",command=self.newfile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save",command=self.savefile)
        self.file_menu.add_command(label="Save As",command=self.saveasfile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit",command=master.destroy)
        self.edit_menu = Menu(self.main_menu,bg="#004854",fg="lime",tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy",command=self.copytext)
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Paste")
        self.font_menu = Menu(self.main_menu,bg="#004854",fg="lime",tearoff=False)
        self.main_menu.add_cascade(label="Font",menu=self.font_menu)
        self.font_menu.add_command(label="Color Configuration",command=self.color)
        
        master.bind('<Control-o>',self.openfile1); master.bind('<Control-s>',self.saveasfile1)
        master.mainloop()

root = Tk()
te = texteditor(root)
root.mainloop()