import os
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Welcome to Society Regulation")

image1 = Image.open("E:/Python Project/societyProject/img/login.jpeg")
bgImg = ImageTk.PhotoImage(image1)

#image2 = Image.open("E:/Python Project/societyProject/img/category.png")
#loginImg = ImageTk.PhotoImage(image2)


society_label = Label(window, text="ABC Society", font=("Arial Bold", 17))
address_label = Label(window, text="Ghodbunder Road, Thane West, Thane, Maharashtra 400607",font=("Arial", 7))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)


def login():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT username, password from user where username='" + user_name.get() + "' and password='"+ password.get() + "'")
    myresult = mycursor.fetchall()

    user = ""
    passw = ""
    for x in myresult:
        user = x[0]
        passw = x[1]

    if  len(myresult) >= 1 and  user_name.get() == "admin":
        msgLabel.configure(text="Login successful")
        window.destroy()
        os.system("py admin.py " + user_name.get())
        return True
    elif len(myresult) >= 1:
        msgLabel.configure(text="Login successful")
        window.destroy()
        os.system("py home.py " + user_name.get())
        return True
    else:
        msgLabel.configure(text="Wrong credentials")


def signup():
    window.destroy()
    os.system("py signup.py")
    return True

#tag_lower(backgroundLabel)

backgroundLabel = Label(window, image=bgImg)
backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)
userlabel=Label(window,text="Login Area").grid(row=2,column=1)
userLabel = Label(window, text="User Name")
passLabel = Label(window, text="Password")
msgLabel = Label(window, text="")

user_name = StringVar()
password = StringVar()

txtUser = Entry(window, textvariable=user_name)
txtPass = Entry(window, textvariable=password)

btnLogin = Button(text="Login", command=login)
btnSignUp = Button(text="Sign Up", command=signup)

society_label.grid(row=0, column=1, columnspan=2)
address_label.grid(row=1, column=1, columnspan=2)
userLabel.grid(row=3, column=0)
txtUser.grid(row=3, column=1)
passLabel.grid(row=4, column=0)
txtPass.grid(row=4, column=1)
btnLogin.grid(row=5, column=0)
btnSignUp.grid(row=5, column=1)
msgLabel.grid(row=6, column=0, columnspan=2)

# btnLogin.pack()
window.geometry('400x400')
window.mainloop()
#window.pack()
#window.tkraise(society_label)
#window.tkraise(address_label)