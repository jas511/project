from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
import login,dashboard,dbms,re
class FrameWindow:
      def __init__(self):
            self.root = Tk()
            self.root.state('zoomed')
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1600, height=900,bg="white") 
            self.frame.place(x = 0, y = 0)
            self.root.title("Registration")

            self.lbl1 = Label(self.frame,text="Library Manager",font="Arial 30 bold",bg="white")
            self.lbl1.place(x=135,y=400)
            
            self.lbl2 = Label(self.frame,text="Registration",font="Arial 27 bold",bg="white")
            self.lbl2.place(x=800,y=80)

            self.img1 = Image.open("project/images/book.png").resize((250,250))
            self.imgtk1 = ImageTk.PhotoImage(self.img1)
            self.imglbl = Label(self.frame,image=self.imgtk1,bg="white")
            self.imglbl.place(x=150,y=150)

            self.maillbl = Label(self.frame,text="E-mail", bg="white", font="Arial 20 bold")
            self.maillbl.place(x=685,y=190)
            self.mail_entry = Entry(self.frame, width=30, font="Arial 12", border=0)
            self.mail_entry.place(x=865,y=196)
            self.underline = Frame(self.frame,width=270, height=2, bg="black")
            self.underline.place(x=865,y=216)

            self.firstLbl = Label(self.frame, text = 'Username', fg = 'black',bg='WHITE', font="Arial 20 bold") 
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

            self.loginbtn = Button(self.frame,text="Sign up",bg="green",width=40,border=0,height=2,fg="white",cursor="hand2",font="Arial 10 bold",command=self.registeruserfn)
            self.loginbtn.place(x=745,y=450)

            self.signup_lbl = Label(self.frame,text="Already have an account?",bg="white",font="Arial 13")
            self.signup_lbl.place(x=765,y=500)
            self.signup_btn = Button(self.frame,text="Sign in",border=0, fg="green", cursor="hand2",bg="white",font="Arial 13", command=self.loginfn)
            self.signup_btn.place(x=945,y=498)
            self.root.mainloop() 
     
      def loginfn(self):
            self.root.destroy()
            login.FrameWindow()
      def registeruserfn(self):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if not(self.mail_entry.get()) or not(self.user_entry.get()) or not(self.pass_entry.get()):
                  messagebox.showwarning("Warning","Please enter all the fields")
            elif not(re.fullmatch(regex, self.mail_entry.get())):
                  messagebox.showwarning("Warning","Invalid Mail ID!")
            elif not(self.user_entry.get().strip()):
                  messagebox.showinfo("Username","Invalid Username!")
            else:
                  details = (self.mail_entry.get(),self.user_entry.get(),self.pass_entry.get())
                  res = dbms.registerUser(details)
                  if res[0]:
                        messagebox.showinfo("Registration","Account created successfully")
                        self.root.destroy()
                        login.FrameWindow()
                  else:
                  # error for already existed email or username
                        if 'username' in res[1]:
                              messagebox.showerror('Alert', 'Username already taken.')
                        if 'email' in res[1]:
                              messagebox.showerror('Alert', 'Email is already registered.')



if __name__ =='__main__':
      FrameWindow()