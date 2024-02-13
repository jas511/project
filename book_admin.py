from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import dbms
class Book():
    def __init__(self,frame):
        self.content = frame
        for widget in self.content.winfo_children():
            widget.destroy()
        
        self.col = ['bookname','authorname','location']
        self.tree = ttk.Treeview(self.content,columns=self.col,show='headings')
        self.tree.heading('bookname',text='Book Name')
        self.tree.heading('authorname',text='Author Name')
        self.tree.heading('location',text='Location')
        self.tree.place(x=140,y=300)
        self.scrollbar = ttk.Scrollbar(self.content,orient="vertical",command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=722,y=301,height=224)

        try:
            result = dbms.fetchbookdetails()
            for i in result:
                self.tree.insert('',1,values=i[1:])
        except:
            pass


        self.title = Label(self.content,text="All Books are listed here",font="Arial 25 bold",bg="white")
        self.title.place(x=350,y=20)

        self.booknamelbl = Label(self.content,text="Enter Book Name",font="Arial 12",bg="white")
        self.booknamelbl.place(x=25,y=100)
        self.booknameinp = Entry(self.content,width=12,font="Arial 10 bold",bd=3)
        self.booknameinp.place(x=170,y=100)

        self.authornamelbl = Label(self.content,text="Enter Author Name",font="Arial 12",bg="white")
        self.authornamelbl.place(x=400,y=100)
        self.authornameinp = Entry(self.content,width=12,font="Arial 10 bold",bd=3)
        self.authornameinp.place(x=550,y=100)

        self.locationlbl = Label(self.content,text="Enter Location",font="Arial 12",bg="white")
        self.locationlbl.place(x=780,y=100)
        self.locationinp = Entry(self.content,width=12,font="Arial 10 bold",bd=3)
        self.locationinp.place(x=910,y=100)

        self.enterdetails = Button(self.content,text="Enter Book Details",bg="#56a9e8",fg="white",font="Arial 10 bold",command=self.enterdetailfn)
        self.enterdetails.place(x=910,y=150)
    
    def enterdetailfn(self):
        if not(self.booknameinp.get()) or not(self.authornameinp.get()) or not(self.locationinp.get()):
            messagebox.showwarning("Warning","Please enter all the fields")
        else:
                res = messagebox.askyesnocancel("Confirmation","Do you really want to enter the details?")
                if res:
                    details = (self.booknameinp.get(),self.authornameinp.get(),self.locationinp.get())
                    result = dbms.enterbookdetail(details)
                if result:
                    messagebox.showinfo("Information","Details added succesfully")
                    self.tree.insert('',1,values=details)
