from tkinter import *
from tkinter import messagebox 
import admin,login
class admin_login:
        def __init__(self):
            self.root = Tk()
            self.root.state("zoomed")
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1500, height=800,bg="white") 
            self.frame.place(x = 0, y = 0)
            self.root.title("library manager")

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

            self.issuebookBtn = Button(self.contentpanel, text = 'ADMIN',font=("sans=serif",20,"bold"),width=10,bg="#ff8080",command=self.adminfn) 
            self.issuebookBtn.place(x = 400, y = 150)

            self.returnBtn=Button(self.contentpanel,text="MEMBER",font=("sans-serif",20,"bold"),width=10,bg="#C0FF80",command=self.loginfn)
            self.returnBtn.place(x=400,y=350)

            self.root.mainloop()

        def adminfn(self):
               self.root.destroy()
               admin.admin_login()

        def loginfn(self):
               self.root.destroy()
               login.FrameWindow()            
        

if __name__ =='__main__':
        admin_login()