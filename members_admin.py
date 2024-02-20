from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import dbms
class Members():
    def __init__(self,frame):
        self.content = frame
        for widget in self.content.winfo_children():
            widget.destroy()
        
        self.col = ['userid','username','emailid']
        self.tree = ttk.Treeview(self.content,columns=self.col,show='headings',height=25)
        self.tree.heading('userid',text='User ID')
        self.tree.column('userid',anchor=CENTER,width=300)
        self.tree.heading('username',text='Name')
        self.tree.column('username',anchor=CENTER,width=300)
        self.tree.heading('emailid',text='E-Mail ID')
        self.tree.column('emailid',anchor=CENTER,width=300)
        self.tree.place(x=100,y=100)
        self.scrollbar = ttk.Scrollbar(self.content,orient="vertical",command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=983,y=101,height=523)

        try:
            result = dbms.fetchmemberdetails()
            for i in result:
                self.tree.insert('',1,values=i[:3])
        except:
            pass


        self.title = Label(self.content,text="All Members are listed here",font="Arial 25 bold",bg="white")
        self.title.place(x=350,y=20)
