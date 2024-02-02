from tkinter import *
from tkinter import messagebox
import dashboard,login
from PIL import ImageTk,Image
#from tkvideo import tkvideo

class statuss:
    def __init__(self):
        self.root=Tk()
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.frame =Frame(self.root, width=500, height=500) 
      
        self.frame.place(x = 0, y = 0)
        self.frame1 =Frame(self.root, width=1000, height=1000) 
        self.frame1.place(x = 0, y = 0)

        self.root.title("User status")

        img1=Image.open(r"C:\Users\jasle\Downloads\dues pending.jpg")
        img1=img1.resize((1550,850),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=850)

        #lblVideo=Label(self.root)
        #lblVideo.pack()

        #player=tkvideo(r"C:\Users\jasle\Downloads\topic #5 (2).mp4",lblVideo,loop=0,size=(1550,950))
        #player.play()

        #self.firstLbl = Label(self.root, text = 'Issued books',fg = 'black',bg='#29465B', font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') 
        #self.firstLbl.pack() 
        #self.firstLbl.place(x = 1000, y = 500) 
        #self.userEntry = Entry(self.root,font=('sans a serif',15))
        #self.userEntry.place(x = 1000, y = 100,height=40,width=400) 

        self.passEntry = Entry(self.root,font=('sans a serif',15)) 
        self.passEntry.place(x = 850, y = 300,height=40,width=350)

        self.passEntry = Entry(self.root,font=('sans a serif',15)) 
        self.passEntry.place(x = 530, y = 600,height=40,width=350)

        self.loginBtn = Button(self.root, text = 'log out',font=('sans-serif',11),command=self.loginfn) 
        self.loginBtn.place(x = 1450, y = 0,width=100,height=20)

        self.loginBtn = Button(self.root, text = 'dashboard',font=('sans-serif',11),command=self.dashboardfn) 
        self.loginBtn.place(x = 1350, y = 0,width=100,height=20)

        self.root.mainloop()

    def loginfn(self):
        self.root.destroy()
        login.FrameWindow()

    def dashboardfn(self):
        self.root.destroy()
        dashboard.Dashboard()

if __name__=='__main__':
    statuss()