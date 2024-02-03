from tkinter import *
from tkinter import messagebox 
import register,dbms,dashboard
from PIL import Image, ImageTk 


class FrameWindow():
    def __init__(self):
      self.root = Tk()
      self.root.state("zoomed")
      self.root.resizable(False, False) 
      self.frame =Frame(self.root, width=500, height=500) 
      self.frame.place(x = 0, y = 0)
      self.frame1 =Frame(self.root, width=1000, height=1000) 
      self.frame1.place(x = 0, y = 0)  
      self.root.title("login")
      # img1=Image.open(r"C:\Users\jasle\OneDrive\Pictures\Screenshots\Screenshot 2023-09-16 180012.png")
      # img1=img1.resize((1600,950),Image.ADAPTIVE)
      # self.photoimg1=ImageTk.PhotoImage(img1)

      # lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
      # lblimg.place(x=0,y=0,width=1600,height=950)
      
      self.firstLbl = Label(self.root, text = 'Username',fg = 'black',bg='WHITE', font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') 
      self.firstLbl.pack() 
      self.firstLbl.place(x = 1000, y = 500) 
      self.userEntry = Entry(self.root,font=('sans a serif',15))
      self.userEntry.place(x = 1150, y = 500,height=30) 

      self.passLbl = Label(self.root, text = 'Password',fg = 'black',bg='WHITE',font = ('Britannic Bold', 15, 'bold'), wraplength=400, justify='left') #
      self.passLbl.pack() 
      self.passLbl.place(x = 1000, y = 550) 
      self.passEntry = Entry(self.root,show='*',font=('sans a serif',15)) 
      self.passEntry.place(x = 1150, y = 550,height=30) 

      self.loginBtn = Button(self.root, text = 'Login',font=('sans-serif',13),command=self.loginfn) 
      self.loginBtn.place(x = 1100, y = 620,width=100) 

      self.gotonextBtn=Button(self.root,text="Don't have an account?",font=('sans-serif',13),command=self.registerfn)
      self.gotonextBtn.place(x=1300,y=700)
      self.root.mainloop()

    def registerfn(self):
       self.root.destroy()
       register.FrameWindow()

    def loginfn(self):
       username = self.userEntry.get()
       password = self.passEntry.get()
       if username and password:
          if(dbms.loginuser((username,password))):
             self.root.destroy()
             dashboard.Dashboard()
          else:
             messagebox.showwarning("Warning","Credentials not matched")
             
       else:
          messagebox.showwarning("Warning","Enter all Fields")
          


if __name__ =='__main__':
    FrameWindow()

