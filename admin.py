from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk,Image


class admin:
    def __init__(self):
        self.root=Tk()
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.frame =Frame(self.root, width=1600, height=950) 
        self.frame.place(x = 0, y = 0)
        self.frame1 =Frame(self.root, width=1600, height=950) 
        self.frame1.place(x = 0, y = 0)

        self.root.title("library manager")

        img1=Image.open(r"C:\Users\jasle\Downloads\[Original size] topic #5.png")
        img1=img1.resize((1600,950),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1600,height=950)

        self.firstLbl = Label(self.root, text = 'Admin name',fg = 'black',bg='#29465B', font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') 
        self.firstLbl.pack() 
        self.firstLbl.place(x = 500, y = 500) 
        self.userEntry = Entry(self.root,font=('sans a serif',15))
        self.userEntry.place(x = 650, y = 500,height=30) 

        self.passLbl = Label(self.root, text = 'Password',fg = 'black',bg='#29465B',font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') 
        self.passLbl.pack() 
        self.passLbl.place(x = 500, y = 550) 
        self.passEntry = Entry(self.root,show='*',font=('sans a serif',15)) 
        self.passEntry.place(x = 650, y = 550,height=30) 

        self.loginBtn = Button(self.root,text='LOGIN',font=('sans-serif',13)) 
        self.loginBtn.place(x=700,y=650,width=100,height=30)

        self.root.mainloop()

if __name__=='__main__':
       admin()