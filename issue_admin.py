from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import dbms
class issue():
    def __init__(self,frame):
        self.content = frame
        for widget in self.content.winfo_children():
            widget.destroy()
        
        self.col = ['bookname','name','id']
        self.tree = ttk.Treeview(self.content,columns=self.col,show='headings',height=18)
        self.tree.heading('bookname',text='Book Name')
        self.tree.column('bookname',anchor=CENTER,width=300)
        self.tree.heading('name',text='Name')
        self.tree.column('name',anchor=CENTER,width=300)
        self.tree.heading('id',text='ID')
        self.tree.column('id',anchor=CENTER,width=300)
        self.tree.place(x=100,y=230)
        self.scrollbar = ttk.Scrollbar(self.content,orient="vertical",command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=983,y=231,height=384)

        try:
            result = dbms.fetchissuedetails()
            for i in result:
                self.tree.insert('',1,values=i[1:])
        except:
            pass


        self.title = Label(self.content,text="Issued Books are listed here",font="Arial 25 bold",bg="white")
        self.title.place(x=350,y=20)

        self.booknamelbl = Label(self.content,text="Enter Book Name",font="Arial 12",bg="white")
        self.booknamelbl.place(x=25,y=100)
        self.booknameinp = Entry(self.content,width=12,font="Arial 10 bold",bd=3)
        self.booknameinp.place(x=170,y=100)

        self.namelbl = Label(self.content,text="Enter Name",font="Arial 12",bg="white")
        self.namelbl.place(x=400,y=100)
        self.nameinp = Entry(self.content,width=12,font="Arial 10 bold",bd=3)
        self.nameinp.place(x=550,y=100)

        self.idlbl = Label(self.content,text="Enter id",font="Arial 12",bg="white")
        self.idlbl.place(x=780,y=100)
        self.idinp = Entry(self.content,width=12,font="Arial 10 bold",bd=3)
        self.idinp.place(x=910,y=100)

        self.enterdetails = Button(self.content,text="Enter Book Details",bg="#56a9e8",fg="white",font="Arial 10 bold",command=self.enterdetailfn)
        self.enterdetails.place(x=910,y=150)
    
    def enterdetailfn(self):
        if not(self.booknameinp.get()) or not(self.nameinp.get()) or not(self.idinp.get()):
            messagebox.showwarning("Warning","Please enter all the fields")
        else:
                if not dbms.checkbookavailability(self.booknameinp):
                    messagebox.showwarning("Warning","No Such Book Available!")
                    return
                res = messagebox.askyesnocancel("Confirmation","Do you really want to enter the details?")
                if res:
                    details = (self.booknameinp.get(),self.nameinp.get(),self.idinp.get())
                    result = dbms.enterissuedetail(details)
                if result:
                    messagebox.showinfo("Information","Details added succesfully")
                    self.tree.insert('',1,values=details)
