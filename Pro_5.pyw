# Sale History
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
#_______________________________________________________________________________________________________________________
mydb = sqlite3.connect("school_project.db")
db = mydb.cursor()


def search_button_is_clicked():
    c = str(Entry1.get())
    cur = mydb.cursor()
    select = ("select * from sale_history where " + str(Search.get()) + " = '" + c + "'")
    cur.execute(select)
    rows = cur.fetchall()
    if len(rows) != 0:
        Field.delete(*Field.get_children())
        for row in rows:
            # if row[7] == None :
            #     print(row[7])
            Field.insert('', END, values=row)
            mydb.commit()

    else:
        Field.delete(*Field.get_children())
        for row in rows:
            Field.insert('', END, values=row)
            mydb.commit()


def delete_history():
    cursor_row = Field.focus()
    content = Field.item(cursor_row)
    row = content['values']
    cur = mydb.cursor()
    select = (f"delete from sale_history where Time = '{row[7]}'")
    cur.execute(select)
    mydb.commit()
    search_all_bth()


def search_all_bth():
    cur = mydb.cursor()
    select = "select * from sale_history "
    cur.execute(select)
    rows = cur.fetchall()
    Field.delete(*Field.get_children())
    for row in rows:
        Field.insert('', END, values=row)
        mydb.commit()

def ext_1():
    root.destroy()

def clear_button_2_is_clicked():
    Field.delete(*Field.get_children())

#_______________________________________________________________________________________________________________________
root = tkinter.Tk()
root.title("   Sale History ")
fevicon = ImageTk.PhotoImage(file='logo.png')
root.iconphoto(True,fevicon)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w = 1056
h = 562
x = int(ws / 2 - w / 2 - 20)
y = int(hs / 2 - h / 2 - 30)
data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
root.geometry(data)
root.configure(bg="#ffffff")
root.resizable(0, 0)

title_frame = LabelFrame(root)
title_frame.pack(fill="x")

title = Label(title_frame,
              text="Sale History",
              font=("Comic Sans MS", 25, "bold"),
              bg="#00e6a1",
              fg="#ffffff",
              anchor="center",
              bd=4)
title.pack(expand=True, fil="x")

Main_Frame = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")
Main_Frame.place(x=0, y=60, width=1056, height=500)

Searching_Frame = Frame(root, bd=1, relief=RIDGE)
Searching_Frame.place(x=0, y=60, width=1056, height=54)

Search_By_Label = Label(Searching_Frame, text="Search By", fg="#676767", font=("Comic Sans MS", 17, "bold"))
Search_By_Label.grid(row=0, column=0, pady=10, padx=20, sticky="w")

Search = StringVar()
Combo_Search = ttk.Combobox(Searching_Frame, textvariable=Search, font=("Comic Sans MS", 14), width=11,
                            state="readonly")

Combo_Search["values"] = ("","Customer_Name","Product_Name","Product ID", "Quantity", "Price",
                                                "Contact","Date")
Combo_Search.grid(row=0, column=1)

Entry1 = StringVar()
Search_Bar = Entry(Searching_Frame, textvariable=Entry1, width=23, fg="#000000", font=("Comic Sans MS", 15), bd=1,
                   relief=GROOVE, )
Search_Bar.grid(row=0, column=2, sticky="w", padx=27)

Search_Button = Button(Searching_Frame, width=10, text="Search", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                       bg="#ffffff",
                       fg="#000000", relief=SUNKEN,command = search_button_is_clicked ).grid(row=0, column=3,
                                                                                           padx=(10, 0), pady=7,
                                                                                           sticky="e")

Search_All_Button = Button(Searching_Frame, width=10, text="Search All", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                           bg="#ffffff",
                           fg="#000000", relief=SUNKEN,command = search_all_bth ).grid(row=0, column=4, padx=20, pady=7,
                                                                                     sticky="e")


Ext= Button(Searching_Frame, width=10, text="     Exit     ", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                           bg="#ffffff",
                           fg="#000000", relief=SUNKEN,command = ext_1 ).grid(row=0, column=5, padx=5, pady=7,
                                                                                     sticky="e")


Database_Window = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")
Database_Window.place(x=0, y=115, width=1056, height=370)

# ********************************************************* Scrrollbars () *****************************

Horizontal_Scrollbar = Scrollbar(Database_Window, orient=HORIZONTAL)
Vertical_Scrollbar = Scrollbar(Database_Window, orient=VERTICAL)

Field = ttk.Treeview(Database_Window, columns=("Customer Name","Product Name","Product ID", "Quantity", "Paid",
                                                "Phone.No","Date","Time"),
                     yscrollcommand=Vertical_Scrollbar.set,
                     xscrollcommand=Horizontal_Scrollbar.set)
Horizontal_Scrollbar.pack(side=BOTTOM, fill=X)
Vertical_Scrollbar.pack(side=RIGHT, fill=Y)
Horizontal_Scrollbar.config(command=Field.xview, )
Horizontal_Scrollbar.bind("<MouseWheel>",Field.xview)
Vertical_Scrollbar.config(command=Field.yview, )
Vertical_Scrollbar.bind("<MouseWheel>",Field.yview)

# Field.heading("Customer ID", text="Customer ID")
Field.heading("Customer Name", text="Customer Name")
Field.heading("Product ID", text="Product ID")
Field.heading("Product Name", text="Product Name")
Field.heading("Quantity", text="Quantity")
Field.heading("Paid", text="Paid")
Field.heading("Phone.No", text="Phone.No")
Field.heading("Date", text="Date")
Field.heading("Time", text="Time")
Field['show'] = "headings"
Field.pack(expand=True,fill = BOTH)


button_frame2 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")
button_frame2.place(x=10, y=495, width=1030, height=54, )

delete_button = Button(button_frame2, width=10, text="Delete", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,
                       bg="#ffffff", fg="#000000", relief=SUNKEN,command = delete_history).grid(row=0,
                                                                                                         column=1,
                                                                                                         padx=(10, 0),
                                                                                                         pady=7)

Clear_button = Button(button_frame2, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",
                      fg="#000000", relief=SUNKEN, command=clear_button_2_is_clicked).grid(row=0, column=2, padx=(9, 0),
                                                                                           pady=7)
search_all_bth()


root.mainloop()