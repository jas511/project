from tkinter import *
from tkinter import messagebox 
import login,issuebook,donatebook,returnbook,status
from PIL import ImageTk,Image
class Dashboard:
        def __init__(self):
            self.root = Tk()
            self.root.state("zoomed")
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1500, height=800) 
            self.frame.place(x = 0, y = 0)
            self.root.title("Dashboard")

            img1=Image.open(r"C:\Users\jasle\OneDrive\Pictures\Screenshots\Screenshot 2023-09-17 151834.png")
            img1=img1.resize((1600,950),Image.ADAPTIVE)
            self.photoimg1=ImageTk.PhotoImage(img1)

            lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=1600,height=950)

            self.issuebookBtn = Button(self.root, text = 'Issue Book',font=("sans=serif",13),width=15,command=self.issuefn) 
            self.issuebookBtn.place(x = 350, y = 450)

            self.returnBtn=Button(self.root,text="Return Book",font=("sans-serif",13),width=15,command=self.returnfn)
            self.returnBtn.place(x=350,y=700)

            self.donateBtn=Button(self.root,text="Donate Book",font=("sans-serif",13),width=15,command=self.donatefn)
            self.donateBtn.place(x=1050,y=450)

            self.statusBtn=Button(self.root,text="Status",font=("sans-serif",13),width=15,command=self.statusfn)
            self.statusBtn.place(x=1050,y=700)

            self.logoutBtn=Button(self.root,text="Logout",command=self.logoutfn)
            self.logoutBtn.place(x=1490,y=5)
            self.root.mainloop()

        def logoutfn(self):
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