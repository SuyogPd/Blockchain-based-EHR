import main
from tkinter import *
import os
import csv
from csv import writer
filename = "User_Records.csv"

req = [ ]
access = [ ]
records = { }

def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=delete2).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()

def addRecords():
    uid = str(userid.get())
    uage = age.get()
    uchol = cholestrol.get()
    utrestbps = trestbps.get()
    ufbs = fbs.get()
    urest_ecg = rest_ecg.get()
    uthalach = thalach.get()

    records[uid] = [uage, uchol, utrestbps, ufbs, urest_ecg, uthalach]
    Label(screen6, text="Record Added").pack()
    main.func()


def view():

    user_id = str(U_id.get())
    if user_id == str(username1):
        print(records[user_id])
    else:
        Label(screen6, text="Access Denied").pack()


def request():
    user_id = str(D_id.get())
    req.append([user_id, str(username1)])
    print(req)
    main.func()

def grant():
    user_id = str(U_id.get())
    access.append([str(username1), user_id])
    print(access)
    main.func()

def view_rec():
    user_id = str(D_id.get())
    for i in access:
        if i[0] == user_id:
            if str(username1) in i:
                print(records[user_id])


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()
    clicked_info = clicked.get()
    print(clicked_info)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()

    with open(filename, 'a') as csvfile:
        writer_object = writer(csvfile)
        List = [clicked_info, username_info, password_info]

        writer_object.writerow(List)


def login_verify():

    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()
    user = clicked1.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    rows = []
    cols = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        cols = next(csvreader)
        for row in csvreader:
            rows.append(row)

    bael = False
    length = len(rows)
    for i in range(0,length):
        if username1 == rows[i][1]:
            if user == rows[i][0]:
                if password1 == rows[i][2]:
                    print("Login successful")
                    Label(screen2, text="Successful Login", fg="green", font=("calibri", 11)).pack()
                    if user == "Admin":
                        global screen6
                        screen6 = Tk
                        screen6 = Toplevel(screen)
                        screen6.title("Admin")
                        screen6.geometry("600x550")

                        global userid
                        global userid_entry
                        global age
                        global age_entry
                        global cholestrol
                        global cholestrol_entry
                        global trestbps
                        global trest_entry
                        global fbs
                        global fbs_entry
                        global rest_ecg
                        global rest_ecg_entry
                        global thalach
                        global thalach_entry

                        userid = StringVar()
                        age = StringVar()
                        cholestrol = StringVar()
                        trestbps = StringVar()
                        fbs = StringVar()
                        rest_ecg = StringVar()
                        thalach = StringVar()

                        Label(screen6, text="User ID").pack()
                        userid_entry = Entry(screen6, textvariable=userid)
                        userid_entry.pack()

                        Label(screen6, text="Age").pack()
                        age_entry = Entry(screen6, textvariable=age)
                        age_entry.pack()

                        Label(screen6, text="Cholestrol").pack()
                        cholestrol_entry = Entry(screen6, textvariable=cholestrol)
                        cholestrol_entry.pack()

                        Label(screen6, text="Trestbps").pack()
                        trest_entry = Entry(screen6, textvariable=trestbps)
                        trest_entry.pack()

                        Label(screen6, text="Fbs").pack()
                        fbs_entry = Entry(screen6, textvariable=fbs)
                        fbs_entry.pack()

                        Label(screen6, text="Rest_ECG").pack()
                        rest_ecg_entry = Entry(screen6, textvariable=rest_ecg)
                        rest_ecg_entry.pack()

                        Label(screen6, text="Thalach").pack()
                        thalach_entry = Entry(screen6, textvariable=thalach)
                        thalach_entry.pack()

                        Button(screen6, text="Add Details", width=10, height=1, command=addRecords).pack()

                    elif user == "Patient":
                        screen6 = Toplevel(screen)
                        screen6.title("Patient")
                        screen6.geometry("600x550")

                        global U_id
                        global u_id
                        U_id = StringVar()
                        Label(screen6, text="Welcome!!!!").pack()
                        u_id = Entry(screen6, textvariable=U_id)
                        u_id.pack()
                        Button(screen6, text="View Details", width=10, height=1, command=view).pack()
                        Button(screen6, text="Grant Access", width=10, height=1, command=grant).pack()
                    else:
                        screen6 = Toplevel(screen)
                        screen6.title("Doctor")
                        screen6.geometry("600x550")
                        global D_id
                        global d_id
                        D_id = StringVar()
                        Label(screen6, text="Welcome!!!!").pack()
                        d_id = Entry(screen6, textvariable=D_id)
                        d_id.pack()
                        Button(screen6, text="Request Access", width=10, height=1, command=request).pack()
                        Button(screen6, text="View Record", width=10, height=1, command=view_rec).pack()

                    bael = True
                    break

    if bael == False:
        print("Invalid Credentials")
        Label(screen2, text="Login Failed!!!", fg="red", font=("calibri", 11)).pack()


def register():
    global screen1
    screen1 = Tk
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x550")

    global username
    global password
    global username_entry
    global password_entry
    global clicked
    global entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    clicked = StringVar()
    clicked.set("Admin")
    drop = OptionMenu(screen1, clicked, "Admin", "Doctor", "Patient")
    drop.pack()

    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    password_entry.config(show="*")
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Tk
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("600x550")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify
    global clicked1

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    clicked1 = StringVar()
    clicked1.set("Admin")
    drop = OptionMenu(screen2, clicked1, "Admin", "Doctor", "Patient")
    drop.pack()

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    password_entry1.config(show="*")
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()