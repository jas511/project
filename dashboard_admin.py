from tkinter import *
from tkinter import messagebox 
import login, book_admin
from PIL import ImageTk,Image
class Dashboard:
        def __init__(self):
            self.root = Tk()
            self.root.state("zoomed")
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1500, height=800,bg="white") 
            self.frame.place(x = 0, y = 0)
            self.root.title("Dashboard")

            self.leftpanel = Frame(self.frame,width=250,height=700,bg="#333232")
            self.leftpanel.place(x=0,y=70)
            self.leftcorner = Frame(self.frame,width=250,height=70,bg="#b57424")
            self.leftcorner.place(x=0,y=0)
            self.title = Label(self.leftcorner,text="Library Manager",fg="white",bg="#b57424",font="sans-serif 20 bold")
            self.title.place(x=10,y=17)
            self.toppanel = Frame(self.frame,width=1200,height=70,bg="#fca232")
            self.toppanel.place(x=250,y=0)
            self.contentpanel = Frame(self.frame,width=1200,height=700,bg="white")
            self.contentpanel.place(x=250,y=70)

            self.adminphoto = Image.open("project/images/user.png").resize((70,70))
            self.adminphototk = ImageTk.PhotoImage(self.adminphoto)
            self.adminphotolbl = Label(self.leftpanel,image=self.adminphototk,bg="#333232")
            self.adminphotolbl.place(x=90,y=40)
            self.adminlbl = Label(self.leftpanel,text="ADMIN",bg="#333232",fg="white",font="Arial 15")
            self.adminlbl.place(x=92,y=120)

            self.dashboardbtn = Button(self.leftpanel,text="DASHBOARD",fg="white",bg="#454545",bd=0,font="Arial 17",width=19,command=self.dashboardfn)
            self.dashboardbtn.place(x=0,y=200)

            self.logoutBtn=Button(self.contentpanel,text="Logout",font="sans-serif 12 bold",fg="white",bg="#333232",command=self.logoutfn)
            self.logoutBtn.place(x=1000,y=20)

            self.heading = Label(self.contentpanel,text="Control Panel",font="Arial 25 bold",bg="white")
            self.heading.place(x=50,y=20)

            self.bookimg = Image.open("project/images/issuebook.png").resize((100,100))
            self.bookimgtk = ImageTk.PhotoImage(self.bookimg)
            self.books = Button(self.contentpanel,text="Books  ",bg="#56a9e8",fg="white",font="Arial 25 bold",image=self.bookimgtk,compound="right",height=100,width=300,command=self.bookfn)
            self.books.place(x=40,y=100)


            self.memberimg = Image.open("project/images/members.png").resize((100,100))
            self.memberimgtk = ImageTk.PhotoImage(self.memberimg)
            self.members = Button(self.contentpanel,text="  Members",bg="#4ebf41",fg="white",font="Arial 25 bold",image=self.memberimgtk,compound="right",height=100,width=300,command=self.memberfn)
            self.members.place(x=400,y=100)


            self.newspaperimg = Image.open("project/images/newspaper.png").resize((100,100))
            self.newspaperimgtk = ImageTk.PhotoImage(self.newspaperimg)
            self.newspaper = Button(self.contentpanel,text="Newspaper ",bg="#fca232",fg="white",font="Arial 25 bold",image=self.newspaperimgtk,compound="right",height=100,width=300,command=self.newspaperfn)
            self.newspaper.place(x=760,y=100)


            self.issuebookimg = Image.open("project/images/issue.png").resize((70,70))
            self.issuebookimgtk = ImageTk.PhotoImage(self.issuebookimg)
            self.issuebooklbl = Button(self.contentpanel,text="     ISSUED     ",bg="white",font="Arial 15 bold",image=self.issuebookimgtk,compound="left",height=65,width=200,command=self.issuefn)
            self.issuebooklbl.place(x=60,y=300)


            self.returnimg = Image.open("project/images/return.png").resize((70,70))
            self.returnimgtk = ImageTk.PhotoImage(self.returnimg)
            self.returnlbl = Button(self.contentpanel,text="     RETURNED     ",bg="white",font="Arial 12 bold",image=self.returnimgtk,compound="left",height=65,width=200,command=self.returnfn)
            self.returnlbl.place(x=320,y=300)


            self.notreturnimg = Image.open("project/images/notreturn.png").resize((70,70))
            self.notreturnimgtk = ImageTk.PhotoImage(self.notreturnimg)
            self.notreturnlbl = Button(self.contentpanel,text=" NOT RETURNED   ",bg="white",font="Arial 12 bold",image=self.notreturnimgtk,compound="left",height=65,width=200,command=self.notreturnfn)
            self.notreturnlbl.place(x=580,y=300)


            self.fineimg = Image.open("project/images/fine.png").resize((70,70))
            self.fineimgtk = ImageTk.PhotoImage(self.fineimg)
            self.finelbl = Button(self.contentpanel,text="            FINE            ",bg="white",font="Arial 12 bold",image=self.fineimgtk,compound="left",height=65,width=200,command=self.finefn)
            self.finelbl.place(x=840,y=300)


            self.root.mainloop()

        def logoutfn(self):
               if messagebox.askyesno("Logout","Do yo really want to logout?"):
                     self.root.destroy()
                     login.FrameWindow()
        
        def dashboardfn(self):
               pass
        
        def bookfn(self):
               book_admin.Book(self.contentpanel)

        def memberfn(self):
               pass

        def newspaperfn(self):
               pass

        def issuefn(self):
               pass

        def returnfn(self):
               pass

        def notreturnfn(self):
               pass

        def finefn(self):
               pass

if __name__ =='__main__':
        Dashboard()