# Forgot Password
import tkinter
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk
import sqlite3
import os

mydb = sqlite3.connect("school_project.db")
db1 = mydb.cursor()


def pre():
    root.destroy()
    try:
        os.startfile("Pro_1.pyw")
    except Exception as e:
        print("s")

def sec_question():
    db1.execute(f"select Username from users where Username = '{name.get()}'")
    f = db1.fetchall()
    if name.get() == "" :
        messagebox.showinfo(title ="Empty",message ="Please enter your usermane !")

    elif (name.get(),) not in f :
        messagebox.showinfo(title="Empty", message="User doesnot exist")

    else :

        def check_answer():
            db1.execute(f"select Answer from users where username = '{name.get()}'")
            f =db1.fetchall()
            if (answ.get(),) in f :
                next_btn_f()
            elif (answ.get(),) == ("",) :
                messagebox.showinfo(message="Please answer the question")

            else :
                messagebox.showinfo(message = "Wrong answer")


        USRName_Label.destroy()
        USRName_Entry.destroy()
        next_btn_1.destroy()
        title_login = Label(frame_login, text="Answer the question to reset the password", bg="#ffffff", fg="#000000",
                            font=("Times New Roman", 15, "bold"))
        title_login.place(x=160, y=120)
        usr =name.get()
        db1.execute(f"select Security_Question from users where Username = '{usr}' ")
        f = db1.fetchall()
        g = str(f)
        rep1  = g.replace("[","")
        rep2 = rep1.replace("(", "")
        rep3 = rep2.replace(")", "")
        rep4 = rep3.replace("]", "")
        rep5 = rep4.replace("'", "")
        rep6 = rep5.replace(",", "")

        USRName_Entry3= Label(frame_login,font =("Times New Roman",17,),text =rep6,fg = "dark gray",bd = 1,bg = "#ffffff",cursor = "hand2")
        USRName_Entry3.place(x = 145,y = 170,width =400 , height = 35)


        answ =StringVar()
        sec_question_Label= Entry(frame_login,textvariable =answ,bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
        sec_question_Label.place(x = 150,y = 215,width =400 , height = 35)

        canc_btn = Button(frame_login, text="Cancel", bd=0, fg="#ffffff", bg="#00d30b",
                            font=("Times New Roman", 20, "bold"), relief=SUNKEN, cursor="hand2",command =pre )
        canc_btn.place(x=150, y=270, width=190, height=40)
        next_btn_2= Button(frame_login, text = "Next",bd =0,fg = "#ffffff",bg = "#00d30b" ,font =("Times New Roman",20,"bold"),relief =SUNKEN,cursor = "hand2",
        command =check_answer)
        next_btn_2.place(x =360,y =270,width = 190,height = 40 )

def login_page():
    root.destroy()
    try:
        os.startfile("Pro_1.pyw")
    except Exception as e:
        print("s")

def next_btn_f():
    def insert():
        cur =mydb.cursor()
        a = new_pass.get()
        b = name.get()
        insert = (f"UPDATE users SET Password = '{a}' WHERE Username ='{b}'")
        cur.execute(insert)
        mydb.commit()


    def reset_pass():
        if new_pass.get() != re_pass.get() :
            messagebox.showinfo("error",message="Password doesn't match")
        else :
            messagebox.showinfo(title="Reset password",message="Are you sure You want to reset your password? You wont be able to login using your previous password anymore.")
            insert()
            login_page()


    frame_login.destroy()
    frame_login2 = Frame(root,bg = "#ffffff" )
    frame_login2.place(x = 512,y = 120 ,height = 470,width = 700)

    new_pass = StringVar()
    re_pass = StringVar()
    title_login1= Label (frame_login2,text = "Reset Password",bg = "#ffffff",fg = "#00d30b",font =("Times New Roman",25,"bold"))
    title_login1.place(x = 45,y = 20)
    P_Label= Label (frame_login2,text = "Enter new password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
    P_Label.place(x = 155,y = 140)
    P_Entry= Entry (frame_login2,font =("Times New Roman",15,),textvariable =new_pass,show ="*",bg = "#ffffff",cursor = "hand2")
    P_Entry.place(x = 155,y = 170,width =390 , height = 35)

    new_pass_Label= Label (frame_login2,text = "Re-enter new password",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
    new_pass_Label.place(x = 155,y = 220)
    new_pass_Entry= Entry (frame_login2,font =("Times New Roman",15,),textvariable =re_pass,show ="*",bg = "#ffffff",cursor = "hand2")
    new_pass_Entry.place(x = 155,y = 250,width =390 , height = 35)

    save_btn_1= Button(frame_login2, text = "Save",bd =0,fg = "#ffffff",bg = "#00d30b" ,font =("Times New Roman",20,"bold"),relief =SUNKEN,cursor = "hand2",command =reset_pass)
    save_btn_1.place(x =354,y =300,width = 190,height = 40 )
    canc_btn = Button(frame_login2, text="Cancel", bd=0, fg="#ffffff", bg="#00d30b",
                      font=("Times New Roman", 20, "bold"), relief=SUNKEN, cursor="hand2", command=pre)
    canc_btn.place(x=153, y=300, width=190, height=40)

root = tkinter.Tk()
root.title("Warehouse Inventory Management System  ")
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
# root.resizable(0,0)
background = ImageTk.PhotoImage(file = r"image5.jpg")
bgmage_label = Label(root,image = background).place(x = 0,y = 0,relwidth =1,relheight = 1)

back = ImageTk.PhotoImage(file = r"image4.jpg")
frame_login1 = Label(root,image =back )
frame_login1.place(x = 112,y = 120 ,height = 470,width = 400)

################################################################################################
################################################################################################

frame_login = Frame(root,bg = "#ffffff" )
frame_login.place(x = 512,y = 120 ,height = 470,width = 700)

title_login= Label (frame_login,text = "Forgot Password",bg = "#ffffff",fg = "#00d30b",font =("Times New Roman",25,"bold"))
title_login.place(x = 25,y = 20)

name =StringVar()
USRName_Label= Label (frame_login,text = "Enter Username",bg = "#ffffff",fg="gray",font =("Goudy old style",15,))
USRName_Label.place(x = 145,y = 175)
USRName_Entry= Entry (frame_login,font =("Times New Roman",15,),textvariable = name ,bg = "#ffffff",cursor = "hand2")
USRName_Entry.place(x = 145,y = 210,width =400 , height = 35)

next_btn_1= Button(frame_login, text = "Next",bd =0,fg = "#ffffff",bg = "#00d30b" ,font =("Times New Roman",20,"bold"),relief =SUNKEN,cursor = "hand2",command = sec_question)
next_btn_1.place(x =354,y =260,width = 190,height = 40 )

back_2_btn_2= Button(frame_login1, text = "Log In",bd =0,fg = "#000000",bg = "#ffffff" ,font =("Times New Roman",25,),relief =SUNKEN,cursor = "hand2",command =login_page)
back_2_btn_2.place(x =90,y =350,width = 200,height = 50,)

root.mainloop()