from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pickle
import smtplib
import threading
import DataBaser
import Main


def login():

    # ----------------- Getting User and Passwords from Entrys -------------------
    userLogin = userEntry.get()
    passLogin = passEntry.get()
    DataBaser.cursor.execute('''
    SELECT * FROM Users
    WHERE (User = ? and Password = ?);
    ''', (userLogin, passLogin))
    verifyLogin = DataBaser.cursor.fetchone()

    # ----------------- Checking If User and Password matches in DB -------------------
    try:
        if userLogin in verifyLogin and passLogin in verifyLogin:
            messagebox.showinfo(title="Login Info", message="Login Successful!\nWelcome!")
            # ----------------- Saving Name From the User in File -------------------
            userName = verifyLogin[1]
            file = open("user.dat", "wb")
            pickle.dump(userName, file)
            file.close()
            # ----------------- Closing Access Panel Window -------------------
            win.destroy()
            # ----------------- Opening Main Window -------------------
            Main.window()

    except:
        messagebox.showerror(title="Login Error", message="Login Unsuccessful.\nTry again.")


def register():

    # ----------------- Cleaning Entry -------------------
    nameEntry.delete(0, 'end')
    emailEntry.delete(0, 'end')
    userEntry.delete(0, 'end')
    passEntry.delete(0, 'end')
    # ----------------- Removing Login Widgets -------------------
    loginButton.place_forget()
    registerButton.place_forget()
    userEntry.place_forget()
    userLabel.place_forget()
    passEntry.place_forget()
    passLabel.place_forget()
    # ----------------- Placing Register Widgets -------------------
    nameLabel.place(x=88, y=40)
    nameEntry.place(x=150, y=46)
    emailLabel.place(x=84, y=70)
    emailEntry.place(x=150, y=76)
    userLabel.place(x=50, y=100)
    userEntry.place(x=150, y=106)
    passLabel.place(x=50, y=130)
    passEntry.place(x=150, y=136)
    # ----------------- Placing Register Buttons -------------------
    createButton.place(x=150, y=166)
    backButton.place(x=248, y=166)


def backtologin():

    # ----------------- Cleaning Entry -------------------
    nameEntry.delete(0, 'end')
    emailEntry.delete(0, 'end')
    userEntry.delete(0, 'end')
    passEntry.delete(0, 'end')
    # ----------------- Removing Register Widgets -------------------
    nameLabel.place_forget()
    nameEntry.place_forget()
    emailLabel.place_forget()
    emailEntry.place_forget()
    createButton.place_forget()
    backButton.place_forget()
    # ----------------- Replacing Login Widgets -------------------
    userLabel.place(x=50, y=100)
    userEntry.place(x=150, y=106)
    passLabel.place(x=50, y=130)
    passEntry.place(x=150, y=136)
    # ----------------- Replacing Login Buttons -------------------
    loginButton.place(x=206, y=165)
    registerButton.place(x=206, y=195)


def registertodatabaser():

    def smtpemail():
        # ----------------- Sending E-mail to the User -------------------
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        getEhlo = smtpObj.ehlo()
        getStarttls = smtpObj.starttls()
        getLogin = smtpObj.login('gamesifpe@gmail.com', '7519536842w')
        smtpObj.sendmail('gamesifpe@gmail.com', email,
                         f'Subject:Conta Criada com Sucesso\nSeja bem-vindo(a) {name} ao gerenciador de jogos do IFPE '
                         f'Campus Paulista.')

    # ----------------- Saving Accounts in Data Base -------------------
    name = nameEntry.get()
    email = emailEntry.get()
    user = userEntry.get()
    passw = passEntry.get()
    DataBaser.cursor.execute('''
        SELECT * FROM Users
        WHERE (User = ? or Email = ?);
        ''', (user, email))
    verifyRegister = DataBaser.cursor.fetchone()
    # ----------------- Checking If Has Empty Entrys -------------------
    if name == "" or email == "" or user == "" or passw == "":
        messagebox.showerror(title="Register Error", message="Cannot Have Empty Field")
    # ----------------- Checking If Email Already Exists in DB -------------------
    elif verifyRegister is not None and email in verifyRegister:
        messagebox.showerror(title="Register Error", message="E-mail Already Used")
        emailEntry.delete(0, 'end')
    # ----------------- Checking If User Already Exists in DB -------------------
    elif verifyRegister is not None and user in verifyRegister:
        messagebox.showerror(title="Register Error", message="User Already Used")
        userEntry.delete(0, 'end')

    else:
        # ----------------- Send User Datas to DB -------------------
        DataBaser.cursor.execute('''
        INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?);
        ''', (name, email, user, passw))
        DataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Account Created Successful")

        # ----------------- Cleaning Entrys -------------------
        nameEntry.delete(0, 'end')
        emailEntry.delete(0, 'end')
        userEntry.delete(0, 'end')
        passEntry.delete(0, 'end')

        # ----------------- Creating and Using a Thread to Send the E-mail -------------------
        thread = threading.Thread(target=smtpemail, args=())
        thread.start()

        # ----------------- Calling Function to go Back -------------------
        backtologin()


# ----------------- Creating Window ---------------
win = Tk()
win.title("IFPE Games System - Access Panel")
win.geometry("600x300")
win.configure(background="white")
win.resizable(width=False, height=False)
win.attributes("-alpha", 0.95)
win.iconbitmap(default="icons/LogoIcon.ico")

# ----------------- Loading Images ---------------
logo = PhotoImage(file="icons/logo.png")

# ----------------- Creating Widgets -------------------
leftFrame = Frame(win, width=200, height=300, bg="WHITE", relief="raise")
leftFrame.pack(side=LEFT)

rightFrame = Frame(win, width=400, height=300, bg="CHARTREUSE2", relief="raise")
rightFrame.pack(side=RIGHT)

logoLabel = Label(leftFrame, image=logo, bg="WHITE")
logoLabel.place(x=-30, y=0)

nameLabel = Label(rightFrame, text="Name:", font=("Century Gothic", 15), bg="CHARTREUSE2", fg="BLACK")

nameEntry = ttk.Entry(rightFrame, width=30)

emailLabel = Label(rightFrame, text="E-mail:", font=("Century Gothic", 15), bg="CHARTREUSE2", fg="BLACK")

emailEntry = ttk.Entry(rightFrame, width=30)

userLabel = Label(rightFrame, text="Username:", font=("Century Gothic", 15), bg="CHARTREUSE2", fg="BLACK")
userLabel.place(x=50, y=100)

userEntry = ttk.Entry(rightFrame, width=30)
userEntry.place(x=150, y=106)

passLabel = Label(rightFrame, text="Password:", font=("Century Gothic", 15), bg="CHARTREUSE2", fg="BLACK")
passLabel.place(x=50, y=130)

passEntry = ttk.Entry(rightFrame, width=30, show="•")
passEntry.place(x=150, y=136)

# ----------------- Creating Buttons -------------------
createButton = ttk.Button(rightFrame, text="Create", width=13, command=registertodatabaser)

backButton = ttk.Button(rightFrame, text="Back", width=13, command=backtologin)

loginButton = ttk.Button(rightFrame, text="Login", width=20, command=login)
loginButton.place(x=206, y=165)
win.bind('<Return>', lambda event=None: loginButton.invoke())

registerButton = ttk.Button(rightFrame, text="Register", width=20, command=register)
registerButton.place(x=206, y=195)


win.mainloop()
