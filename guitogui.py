from tkinter import *
t =Tk()
t.geometry("425x380")
def login():
    f2 =Frame(bg ="#3B2F2F")
    f2.place(x=0,y=0,width =425,height =380)
    l = Label(f2, text="Login Page",bg ="#3B2F2F",fg ="white")
    l.place(x=200, y=10)
    l1 =Label(f2,text ="Enter Name",bg ="#3B2F2F",fg ="white")
    l1.place(x =60,y =100)
    l2 =Label(f2,text ="Enter password",bg ="#3B2F2F",fg ="white")
    l2.place(x=60,y=150)
    e1 =Entry(f2)
    e1.place(x=200,y=100,width =120)
    e2 =Entry(f2,show='*')
    e2.place(x=200,y=150,width =120)
    b2 =Button(f2,text ="login",bg ="black",fg ="white")
    b2.place(x=180,y=200, width= 100,height =40)
    b3 =Button(f2,text ="<-",command =home,bg ="black",fg ="white")
    b3.place(x =0,y =0,width =50,height =40)
def register():
    f3 =Frame(bg ="#3B2F2F")
    f3.place(x=0,y=0,width =425,height =380)
    l = Label(f3, text="Registration Page",bg ="#3B2F2F",fg ="white")
    l.place(x=180, y=10)
    l1 = Label(f3, text="Enter Name",bg ="#3B2F2F",fg ="white")
    l1.place(x=60, y=100)
    l2 = Label(f3, text="Enter password",bg ="#3B2F2F",fg ="white")
    l2.place(x=60, y=150)
    l3 =Label(f3,text ="Enter email",bg ="#3B2F2F",fg ="white")
    l3.place(x=60,y=200)
    e1 = Entry(f3)
    e1.place(x=200, y=100, width=120)
    e2 = Entry(f3, show='*')
    e2.place(x=200, y=150, width=120)
    e3 =Entry(f3)
    e3.place(x=200,y =200,width =120)
    b2 = Button(f3, text="register",bg ="black",fg ="white")
    b2.place(x=180, y=250,width=100, height=40)
    b3 = Button(f3, text="<-", command=home,bg ="black",fg ="white")
    b3.place(x=0, y=0, width=50, height=40)
def home():
    f1 =Frame(bg="#3B2F2F")
    f1.place(x=0,y=0,width =425,height =380)
    b1 =Button(f1,text ="Login",command =login )
    b1.place(x=50,y=50,width =100,height =50)
    b2 = Button(f1, text="Register", command=register)
    b2.place(x=200,y=50,width =100,height =50)
home()

t.mainloop()