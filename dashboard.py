from tkinter import *
from tkinter import messagebox 
import login,issuebook,donatebook,returnbook,status
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
            self.contentpanel = Frame(self.frame,width=1200,height=700,bg="white") # #454545
            self.contentpanel.place(x=250,y=70)


            self.issuebookBtn = Button(self.contentpanel, text = 'Issue Book',font=("sans=serif",20,"bold"),width=10,bg="#ff8080",command=self.issuefn) 
            self.issuebookBtn.place(x = 100, y = 150)

            self.returnBtn=Button(self.contentpanel,text="Return Book",font=("sans-serif",20,"bold"),width=10,bg="#C0FF80",command=self.returnfn)
            self.returnBtn.place(x=450,y=150)

            self.donateBtn=Button(self.contentpanel,text="Donate Book",font=("sans-serif",20,"bold"),width=10,bg="#80FFFF",command=self.donatefn)
            self.donateBtn.place(x=100,y=300)

            self.statusBtn=Button(self.contentpanel,text="Status",font=("sans-serif",20,"bold"),width=10,bg="#C080FF",command=self.statusfn)
            self.statusBtn.place(x=450,y=300)

            self.logoutBtn=Button(self.contentpanel,text="Logout",font="sans-serif 12 bold",command=self.logoutfn)
            self.logoutBtn.place(x=950,y=20)

            self.root.mainloop()

        def logoutfn(self):
               if messagebox.askyesno("Logout","Do yo really want to logout?"):
                     self.root.destroy()
                     login.FrameWindow()
        def issuefn(self):
               self.root.destroy()
               issuebook.issue()
        def donatefn(self):
               self.root.destroy()
               donatebook.donate()
        def returnfn(self):
               self.root.destroy()
               returnbook.returns()
        def statusfn(self):
               self.root.destroy()
               status.statuss()
        

if __name__ =='__main__':
        Dashboard()