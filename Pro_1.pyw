# Login Page
import tkinter
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk
import sqlite3
import os

mydb = sqlite3.connect("school_project.db")
db1 = mydb.cursor()

def sign_up_page():
    root.destroy()
    try:
        os.startfile("Pro_3.pyw")
    except Exception as e:
        print ("s")

def open_pro():
    try:
        os.startfile("Pro_2.pyw")
    except Exception as e:
        print ("s")

def forgot_pass():
    root.destroy()
    try:
        os.startfile("Pro_4.pyw")
    except Exception as e:
        print ("s")

def login():
    if enter_user.get() == "" and enter_pass.get() == "":
        messagebox.showerror("Error",message = "Please Enter username and Password", parent=root)

    elif enter_user.get() == "" and enter_pass.get() != "":
        messagebox.showerror("Error",message = "Invalid username or password", parent=root)

    elif enter_user.get() != "" and enter_pass.get() == "":
        messagebox.showerror("Error",message = "Invalid username or passsword", parent=root)

    elif enter_user.get() != "" and enter_pass.get() != "":
        db1.execute("select Username from users ")
        use =db1.fetchall()

        if (f"{enter_user.get()}",) in use :
            db1.execute("select Password from users ")
            use = db1.fetchall()
            if (f"{enter_pass.get()}",) in use:
                root.destroy()
                open_pro()

            else:
                messagebox.showerror(title = "error",message ="Invalid Username or Password")
        else:
            messagebox.showerror(title="error", message="Invalid Username or Password")
    else:
        pass

'''*********************************************************************************
   *********************************************************************************'''

root = tkinter.Tk()
root.title("Warehouse Inventory Management System  ")
fevicon = PhotoImage(file='logo.png')
root.iconphoto(False,fevicon)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 1350
h = 703
x = int(ws / 2 - w / 2 - 20)
y = int(hs / 2 - h / 2 - 30)
data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
root.geometry(data)
root.configure(bg="#ffffff")
# root.resizable(0,0)
background = ImageTk.PhotoImage(file = r"image5.jpg")
bgmage_label = Label(root,image = background).place(x = 0,y = 0,relwidth =1,relheight = 1)

back = ImageTk.PhotoImage(file = r"image4.jpg")
frame_login1 = Label(root,image =back )
frame_login1.place(x = 112,y = 120 ,height = 470,width = 400)

frame_login = Frame(root,bg = "#ffffff" )
frame_login.place(x = 512,y = 120 ,height = 470,width = 700)

#****************************( Object inside frame)**********************

title_login= Label (frame_login,text = "log In",bg = "#ffffff",fg = "#d77337",font =("Impact",35,"bold"))
title_login.place(x = 235,y = 25)

title_inst= Label(frame_login,text = "In order to use the  software you first need to login ",bg = "#ffffff",fg = "#d25d17",font =("Goudy old style",15,"bold"))
title_inst.place(x = 90,y = 110)

title_user= Label (frame_login,text = "Username",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
title_user.place(x = 90,y = 160)

enter_user= Entry (frame_login,font =("Times New Roman",15,),bg = "#ffffff",cursor = "hand2")
enter_user.place(x = 90,y = 190,width =350 , height = 35)

title_pass= Label (frame_login,text = "Password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
title_pass.place(x = 90,y = 231)

enter_pass= Entry (frame_login,font =("Times New Roman",15,),show ="*",bg = "#ffffff",cursor = "hand2")
enter_pass.place(x = 90,y = 265,width =350 , height = 35)

forget_password = Button(frame_login, text = "Forget password ?",bd =0,bg ="#ffffff",fg = "#d77337",font =("Times New Roman",12),relief =GROOVE,cursor = "hand2",command = forgot_pass)
forget_password.place(x =90,y =300 )

log_in_btn= Button(frame_login, text = "Log In",bd =0,fg = "#ffffff",bg = "#d77337" ,font =("Impact",42,),relief =FLAT,cursor = "hand2",command =login)
log_in_btn.place(x =90,y =350,width = 500,height = 90 )

Sign_up_btn_2= Button(frame_login1, text = "Sign up",bd =0,fg = "#000000",bg = "#ffffff" ,font =("Times New Roman",25,),relief =SUNKEN,cursor = "hand2",command = sign_up_page)
Sign_up_btn_2.place(x =80,y =350,width = 200,height = 50 )

root.mainloop()
