from tkinter import *
import sqlite3
from tkinter import messagebox
t =Tk()
t.geometry("600x400")
t.resizable(0,0)
def login():
    f2 =Frame(bg ="#3B2F2F")
    f2.place(x=0, y=0, width=600, height=600)
    name =Label(f2,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry()
    e1.place(x =200,y=100)
    password=Label(f2,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry()
    e2.place(x=200, y=150)

    b1 =Button(f2,text="login")
    b1.place(x=150,y =200)

    b2 = Button(f2, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f2, text="register",command =register)
    b2.place(x=490, y=350, width=100, height=40)

def register():
    f3 =Frame(bg ="#3B2F2F")
    f3.place(x=0, y=0, width=600, height=600)
    r1 =StringVar()
    r2 =StringVar()
    r3 =StringVar()
    name =Label(f3,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry(textvariable =r1)
    e1.place(x =200,y=100)
    password=Label(f3,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry(textvariable=r2)
    e2.place(x=200, y=150)

    contact = Label(f3, text="Enter your C.No.", bg="#3B2F2F", fg="white")
    contact.place(x=50, y=200)
    e1 = Entry(textvariable=r3)
    e1.place(x=200, y=200)

    # creating a button of regis1 for register in the data base
    def regis1():
        db = sqlite3.connect('new.db')
        cr = db.cursor()
        cr.execute("insert into regis values('" + r1.get() + "','"+r2.get()+"','"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title","data  is inserted")
        r1.set("")
        r2.set("")
        r3.set("")
    b1 =Button(f3,text="register", command =regis1)
    b1.place(x=150,y =250)

    b2 = Button(f3, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f3, text="login", command =login)
    b2.place(x=490,y=350, width=100, height=40)

def home():
    f1 =Frame(bg="#3B2F2F")
    f1.place(x =0,y =0,width =600,height =600)
    b1 =Button(f1,text ="login",command =login)
    b1.place(x =220,y=150)
    b1 = Button(f1, text="register",command =register)
    b1.place(x=310, y=150)
home()
t.mainloop()