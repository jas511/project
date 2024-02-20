from tkinter import *
from tkinter import messagebox 
import login 
import frontdetails, members_admin
from PIL import ImageTk,Image
class Dashboard:
        def __init__(self):
            self.root = Tk()
            self.root.state("zoomed")
            self.root.resizable(False, False) 
            self.frame =Frame(self.root, width=1600, height=900,bg="white") 
            self.frame.place(x = 0, y = 0)
            self.root.title("Dashboard")

            self.leftpanel = Frame(self.frame,width=250,height=900,bg="#333232")
            self.leftpanel.place(x=0,y=70)
            self.leftcorner = Frame(self.frame,width=250,height=70,bg="#b57424")
            self.leftcorner.place(x=0,y=0)
            self.title = Label(self.leftcorner,text="Library Manager",fg="white",bg="#b57424",font="sans-serif 20 bold")
            self.title.place(x=10,y=17)
            self.toppanel = Frame(self.frame,width=1500,height=70,bg="#fca232")
            self.toppanel.place(x=250,y=0)

       #      self.adminphoto = Image.open("project\images\user.png").resize((70,70))
       #      self.adminphototk = ImageTk.PhotoImage(self.adminphoto)
       #      self.adminphotolbl = Label(self.leftpanel,image=self.adminphototk,bg="#333232")
       #      self.adminphotolbl.place(x=90,y=40)
            self.adminlbl = Label(self.leftpanel,text="ADMIN",bg="#333232",fg="white",font="Arial 15")
            self.adminlbl.place(x=92,y=120)

            self.dashboardbtn = Button(self.leftpanel,text="DASHBOARD",fg="white",bg="#454545",bd=0,font="Arial 17",width=19,command=self.dashboardfn)
            self.dashboardbtn.place(x=0,y=200)


            self.contentpanel = Frame(self.frame,width=1200,height=700,bg="white")
            self.contentpanel.place(x=250,y=70)

            frontdetails.FrontDetails(self.contentpanel)

            


            self.root.mainloop()
        
        def dashboardfn(self):
               try:
                      for widget in self.contentpanel.winfo_children():
                             widget.destroy()
               except:
                      pass
               frontdetails.FrontDetails(self.contentpanel)
        

if __name__ =='__main__':
        Dashboard()