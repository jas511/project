
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
import login,dbms,dashboard
class FrameWindow:
      def __init__(self):
            self.root = Tk()
            self.root.state('zoomed')
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1600, height=900) 
            self.frame.place(x = 0, y = 0)
            self.frame1 =Frame(self.root, width=1600, height=900) 
            self.frame1.place(x = 200, y = 0) 
            self.root.title("Registration")

            
            img1=Image.open(r"C:\Users\jasle\OneDrive\Pictures\Screenshots\Screenshot 2023-09-18 131128.png")
            #img1=Image.open(r"C:\Users\jasle\Downloads\dues pending (3).jpg")
            img1=img1.resize((1600,950),Image.ADAPTIVE)
            self.photoimg1=ImageTk.PhotoImage(img1)

            lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=1600,height=950)

            self.firstLbl = Label(self.root, text = 'Username', fg = 'black',bg='WHITE', font = ('sans-serif', 15, 'bold'), wraplength=400, justify='left') 
            self.firstLbl.pack() 
            self.firstLbl.place(x = 100, y = 500,height=30) 
            self.userEntry = Entry(self.root,font=('sans-serif',15))
            self.userEntry.place(x = 250, y = 500) 

            self.passLbl = Label(self.root, text = 'Password', fg = 'black',bg='WHITE', font = ('sans-serif', 15, 'bold'), wraplength=400, justify='left') #
            self.passLbl.pack() 
            self.passLbl.place(x = 100, y = 550,height=30) 
            self.passEntry = Entry(self.root,show='*',font=('sans-serif',15)) 
            self.passEntry.place(x = 250, y = 550,height=30) 

            self.createBtn = Button(self.root, text = 'Create Account',font=('asans-serif',13),command=self.registeruserfn) 
            self.createBtn.place(x = 180, y = 630) 

            self.gobackBtn=Button(self.root,text="Already have an account?",font=('sans-serif',13),command=self.loginfn)
            self.gobackBtn.place(x=720,y=750,width=200)
            self.root.mainloop() 
     
      def loginfn(self):
            self.root.destroy()
            login.FrameWindow()
      def registeruserfn(self):
            username=self.userEntry.get()
            password= self.passEntry.get()
            if username and password:
                  dbms.registeruser((username,password))
                  self.root.destroy()
                  dashboard.Dashboard()
            else:
                  messagebox.showwarning("Warning","Enter all Fields")



if __name__ =='__main__':
        FrameWindow()