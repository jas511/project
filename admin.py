from tkinter import *
from tkinter import messagebox 
import dashboard_admin
class admin_login:
        def __init__(self):
            self.root = Tk()
            self.root.state("zoomed")
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1500, height=800,bg="white") 
            self.frame.place(x = 0, y = 0)
            self.root.title("Admin")

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

            self.firstLbl = Label(self.frame, text = 'Admin name', fg = 'black',bg='WHITE', font="Arial 20 bold") 
            self.firstLbl.place(x=685,y=280)
            self.user_entry = Entry(self.frame, width=30, font="Arial 12", border=0)
            self.user_entry.place(x=865,y=286)
            self.underline1 = Frame(self.frame,width=270, height=2, bg="black")
            self.underline1.place(x=865,y=306)

            self.passLbl = Label(self.frame, text = 'Password', fg = 'black',bg='WHITE', font="Arial 20 bold") #
            self.passLbl.place(x=685,y=370) 
            self.pass_entry = Entry(self.frame, width=30, font="Arial 12", border=0,show="*")
            self.pass_entry.place(x=865,y=376)
            self.underline2 = Frame(self.frame,width=270, height=2, bg="black")
            self.underline2.place(x=865,y=396)
            
            self.signup_btn = Button(self.frame,text="Log in",border=0, fg="green", cursor="hand2",bg="white",font="Arial 13", command=self.loginnfn)
            self.signup_btn.place(x=945,y=498)

            self.root.mainloop()

        def loginnfn(self):
               self.root.destroy()
               dashboard_admin.Dashboard()             
        

if __name__ =='__main__':
        admin_login()