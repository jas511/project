from tkinter import *
from tkinter import messagebox
import dashboard,login
from PIL import ImageTk,Image

class donate:
    def __init__(self):
        self.root=Tk()
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.frame =Frame(self.root, width=500, height=500) 
      
        self.frame.place(x = 0, y = 0)
        self.frame1 =Frame(self.root, width=1000, height=1000) 
        self.frame1.place(x = 0, y = 0)

        self.root.title("Donate book")

        img1=Image.open(r"C:\Users\jasle\OneDrive\Pictures\Screenshots\Screenshot 2023-09-24 120352.png")
        img1=img1.resize((1550,850),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=850)

        #self.firstLbl = Label(self.root, text = 'Book Name',fg = 'black',bg='#29465B', font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') 
        #self.firstLbl.pack() 
        #self.firstLbl.place(x = 1000, y = 500) 
        self.userEntry = Entry(self.root,font=('sans a serif',15))
        self.userEntry.place(x = 730, y = 150,height=40,width=400) 

        #self.passLbl = Label(self.root, text = 'Author Name',fg = 'black',bg='#29465B',font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') #
        #self.passLbl.pack() 
        #self.passLbl.place(x = 1000, y = 550) 
        self.passEntry = Entry(self.root,font=('sans a serif',15)) 
        self.passEntry.place(x = 180, y = 370,height=40,width=400)

        self.loginBtn = Button(self.root, text = 'DONATE',font=('sans-serif',13)) 
        self.loginBtn.place(x = 650, y = 650,width=200)

        self.loginBtn = Button(self.root, text = 'log out',font=('sans-serif',13),command=self.loginfn) 
        self.loginBtn.place(x = 1450, y = 0,width=100)

        self.loginBtn = Button(self.root, text = 'dashboard',font=('sans-serif',13),command=self.dashboardfn) 
        self.loginBtn.place(x = 1350, y = 0,width=100)


        self.root.mainloop()

    def loginfn(self):
        self.root.destroy()
        login.FrameWindow()

    def dashboardfn(self):
        self.root.destroy()
        dashboard.Dashboard()


if __name__=='__main__':
    donate()