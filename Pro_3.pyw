# Create Account
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
import os

mydb = sqlite3.connect("school_project.db")
db1 = mydb.cursor()

def login_page():
    root.destroy()
    try:
        os.startfile("Pro_1.pyw")
    except Exception as e:
        print("s")

def enter_new_usr():
    cur = mydb.cursor()
    cur.execute("select Username, E_mail from users")
    f = cur.fetchall()
    if USRName.get() in f :

        messagebox.showinfo("error",message="this username had already been taken")
        pass
    elif Pass1.get() != Pass2.get() :
        messagebox.showinfo("error",message="Password doesn't match")
        pass
    else :

        cur.execute("INSERT INTO users values (:First, :Second, :Third, :Fourth, :Fifth, :Sixth)",{
                "First":FName.get()+" "+LName.get(),
                "Second":USRName.get(),
                "Third":E_mail.get(),
                "Fourth":Pass1.get(),
                "Fifth":Security_Q.get(),
                "Sixth":Security_A.get(),})
        mydb.commit()
        print("Done")
        messagebox.showinfo("Information",message ="Your account has been created now you will be redirected to the Login Page")
        login_page()

root = tkinter.Tk()
root.title("Warehouse Inventory Management System   ")
fevicon = ImageTk.PhotoImage(file='logo.png')
root.iconphoto(True,fevicon)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 1350
h = 703
x = int(ws / 2 - w / 2 - 20)
y = int(hs / 2 - h / 2 - 30)
data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
root.geometry(data)
root.configure(bg="#ffffff")
background = ImageTk.PhotoImage(file = r"image5.jpg")
bgmage_label = Label(root,image = background).place(x = 0,y = 0,relwidth =1,relheight = 1)

back = ImageTk.PhotoImage(file = r"image4.jpg")
frame_login1 = Label(root,image =back )
frame_login1.place(x = 112,y = 120 ,height = 470,width = 400)

frame_login = Frame(root,bg = "#ffffff" )
frame_login.place(x = 512,y = 120 ,height = 470,width = 700)

title_login= Label (frame_login,text = "Create an account",bg = "#ffffff",fg = "#00d30b",font =("Times New Roman",25,"bold"))
title_login.place(x = 35,y = 15)

FName = StringVar()
LName = StringVar()
USRName = StringVar()
E_mail = StringVar()
Pass1 = StringVar()
Pass2 = StringVar()
Security_Q= StringVar()
Security_A = StringVar()

FName_Label= Label (frame_login,text = "First Name",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
FName_Label.place(x = 35,y = 80)
FName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =FName ,bg = "#ffffff",cursor = "hand2")
FName_Entry.place(x = 35,y = 110,width =300 , height = 35)

LName_Label= Label (frame_login,text = "Last Name",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
LName_Label.place(x = 35,y = 160)
LName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =LName,bg = "#ffffff",cursor = "hand2")
LName_Entry.place(x = 35,y = 190,width =300 , height = 35)

USRName_Label= Label (frame_login,text = "Username",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
USRName_Label.place(x = 35,y = 240)
USRName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =USRName,bg = "#ffffff",cursor = "hand2")
USRName_Entry.place(x =35,y = 270,width =300 , height = 35)

E_mail_Label= Label (frame_login,text = "E-mail",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
E_mail_Label.place(x = 35,y = 320)
E_mail_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =E_mail,bg = "#ffffff",cursor = "hand2")
E_mail_Entry.place(x = 35,y = 350,width =300 , height = 35)

Pass1_Label= Label (frame_login,text = "Enter Password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Pass1_Label.place(x = 355,y = 80)
Pass1_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Pass1,show = "*",bg = "#ffffff",cursor = "hand2")
Pass1_Entry.place(x = 355,y = 110,width =300 , height = 35)

Pass_2_Label= Label (frame_login,text = "Re-enter Password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Pass_2_Label.place(x = 355,y = 160)
Pass_2_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Pass2,bg = "#ffffff",cursor = "hand2")
Pass_2_Entry.place(x = 355,y = 190,width =300 , height = 35)

Security_Q_Label= Label (frame_login,text = "Security Question",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Security_Q_Label.place(x = 355,y = 240)
Security_Q_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Security_Q,bg = "#ffffff",cursor = "hand2")
Security_Q_Entry.place(x = 355,y = 270,width =300 , height = 35)

Security_A_Label= Label (frame_login,text = "Security Answer",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
Security_A_Label.place(x = 355,y = 320)
Security_A_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable =Security_A,bg = "#ffffff",cursor = "hand2")
Security_A_Entry.place(x = 355,y = 350,width =300 , height = 35)

Create_btn= Button(frame_login, text = "Create account",bd =0,fg = "#ffffff",bg = "#00d30b" ,font =("Times New Roman",20,"bold"),relief =SUNKEN,cursor = "hand2",command = enter_new_usr)
Create_btn.place(x =395,y =400,width = 230,height = 40 )

back_2_btn_2= Button(frame_login1, text = "Log In",bd =0,fg = "#000000",bg = "#ffffff" ,font =("Times New Roman",25,),relief =SUNKEN,cursor = "hand2",command =login_page)
back_2_btn_2.place(x =90,y =350,width = 200,height = 50,)

root.mainloop()