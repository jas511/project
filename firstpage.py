from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import login,register
class firstpage:
    def __init__(self):
        self.root=Tk()
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.frame =Frame(self.root, width=1600, height=950) 
        self.frame.place(x = 0, y = 0)
        self.frame1 =Frame(self.root, width=1600, height=950) 
        self.frame1.place(x = 0, y = 0)

        self.root.title("library manager")

        img1=Image.open(r"C:\Users\jasle\OneDrive\Pictures\Screenshots\Screenshot 2023-09-16 142550.png")
        img1=img1.resize((1600,950),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1600,height=950)

        self.loginBtn = Button(self.root,text='LOGIN',font=('sans-serif',13),command=self.loginn) 
        self.loginBtn.place(x=900,y=500,width=100,height=30)

        self.registerBtn=Button(self.root,text='SIGN UP',font=('sans-serif',13),command=self.registerr)
        self.registerBtn.place(x=1200,y=500,width=100,height=30)
        self.root.mainloop()


    def loginn(self):
        self.root.destroy()
        login.FrameWindow()

    def registerr(self):
         self.root.destroy()
         register.FrameWindow()    
        

if __name__=='__main__':
       firstpage()