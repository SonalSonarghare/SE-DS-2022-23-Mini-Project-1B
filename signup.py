import os
from tkinter import *
from tkinter import Button
import mysql.connector
from PIL import Image, ImageTk

window = Tk()
window.title("SignUp")

#image1 = Image.open("E:\Python Project\societyProject\img\WhatsApp Image 2023-04-19 at 10.47.15 PM.jpeg")
#bgImg = ImageTk.PhotoImage(image1)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)

def login():
    window.destroy()
    os.system("py login.py")
    return True

def save():
    mycursor = mydb.cursor()
    mycursor.execute("insert into user(username,password) values('"+ varUserName.get() + "', '" + varPassword.get() + "')")
    mydb.commit()

registerLabel = Label(window, text="Create User")
userLabel = Label(window, text="User Name")
passwordLabel = Label(window, text="Password")

varUserName = StringVar()
varPassword = StringVar()

txtUser = Entry(window, textvariable=varUserName)
txtPass = Entry(window, textvariable=varPassword)

btnCreate = Button(text="Create", command=save)
btnLogin = Button(text="Login", command=login)

#backgroundLabel = Label(window, image=bgImg)
#backgroundLabel.place(x=0, y=0, relheight=1, relwidth=1)
registerLabel.grid(row=0, column=0, columnspan=2)
userLabel.grid(row=1, column=0)
txtUser.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0)
txtPass.grid(row=2, column=1)
btnCreate.grid(row=3, column=0)
btnLogin.grid(row=3, column=1)


# btnLogin.pack()
window.geometry('400x400')
window.mainloop()
