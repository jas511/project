from tkinter import *
from PIL import Image, ImageTk
import book_admin, members_admin, newspaper_admin,issue_admin,return_admin,notreturned_admin,fine_admin
import login
from tkinter import messagebox

class FrontDetails():
        def __init__(self,frame):
            self.contentpanel = frame
            self.logoutBtn=Button(self.contentpanel,text="Logout",font="sans-serif 12 bold",fg="white",bg="#333232",command=self.logoutfn)
            self.logoutBtn.place(x=1000,y=20)

            self.heading = Label(self.contentpanel,text="Control Panel",font="Arial 25 bold",bg="white")
            self.heading.place(x=50,y=20)

            #self.bookimg = Image.open("project/images/issuebook.png").resize((100,100))
            self.bookimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\issuebook.png").resize((100,100))
            self.bookimgtk = ImageTk.PhotoImage(self.bookimg)
            self.books = Button(self.contentpanel,text="Books  ",bg="#56a9e8",fg="white",font="Arial 25 bold",image=self.bookimgtk,compound="right",height=100,width=300,command=self.bookfn)
            self.books.place(x=40,y=100)


            #self.memberimg = Image.open("project/images/members.png").resize((100,100))
            self.memberimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\members.png").resize((100,100))
            self.memberimgtk = ImageTk.PhotoImage(self.memberimg)
            self.members = Button(self.contentpanel,text="  Members",bg="#4ebf41",fg="white",font="Arial 25 bold",image=self.memberimgtk,compound="right",height=100,width=300,command=self.memberfn)
            self.members.place(x=400,y=100)


            #self.newspaperimg = Image.open("project/images/newspaper.png").resize((100,100))
            self.newspaperimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\newspaper.png").resize((100,100))
            self.newspaperimgtk = ImageTk.PhotoImage(self.newspaperimg)
            self.newspaper = Button(self.contentpanel,text="Newspaper ",bg="#fca232",fg="white",font="Arial 25 bold",image=self.newspaperimgtk,compound="right",height=100,width=300,command=self.newspaperfn)
            self.newspaper.place(x=760,y=100)


            #self.issuebookimg = Image.open("project/images/issue.png").resize((70,70))
            self.issuebookimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\issue.png").resize((70,70))
            self.issuebookimgtk = ImageTk.PhotoImage(self.issuebookimg)
            self.issuebooklbl = Button(self.contentpanel,text="     ISSUED     ",bg="white",font="Arial 15 bold",image=self.issuebookimgtk,compound="left",height=65,width=200,command=self.issuefn)
            self.issuebooklbl.place(x=60,y=300)


            #self.returnimg = Image.open("project/images/return.png").resize((70,70))
            self.returnimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\return.png").resize((70,70))
            self.returnimgtk = ImageTk.PhotoImage(self.returnimg)
            self.returnlbl = Button(self.contentpanel,text="     RETURNED     ",bg="white",font="Arial 12 bold",image=self.returnimgtk,compound="left",height=65,width=200,command=self.returnfn)
            self.returnlbl.place(x=320,y=300)


            #self.notreturnimg = Image.open("project/images/notreturn.png").resize((70,70))
            self.notreturnimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\notreturn.png").resize((70,70))
            self.notreturnimgtk = ImageTk.PhotoImage(self.notreturnimg)
            self.notreturnlbl = Button(self.contentpanel,text=" NOT RETURNED   ",bg="white",font="Arial 12 bold",image=self.notreturnimgtk,compound="left",height=65,width=200,command=self.notreturnfn)
            self.notreturnlbl.place(x=580,y=300)


            #self.fineimg = Image.open("project/images/fine.png").resize((70,70))
            self.fineimg = Image.open(r"C:\Users\jasle\OneDrive\Documents\GitHub\project\images\fine.png").resize((70,70))
            self.fineimgtk = ImageTk.PhotoImage(self.fineimg)
            self.finelbl = Button(self.contentpanel,text="            FINE            ",bg="white",font="Arial 12 bold",image=self.fineimgtk,compound="left",height=65,width=200,command=self.finefn)
            self.finelbl.place(x=840,y=300)
            

        def bookfn(self):
               book_admin.Book(self.contentpanel)

        def memberfn(self):
               members_admin.Members(self.contentpanel)

        def newspaperfn(self):
               newspaper_admin.Newspaper(self.contentpanel)

        def issuefn(self):
               issue_admin.issue(self.contentpanel)

        def returnfn(self):
               return_admin.returnbook(self.contentpanel)
        
        def logoutfn(self):
              if messagebox.askyesno("Logout","Do yo really want to logout?"):
                self.root.destroy()
                login.FrameWindow()

        def notreturnfn(self):
               notreturned_admin.notreturn(self.contentpanel)

        def finefn(self):
               fine_admin.fine(self.contentpanel)
