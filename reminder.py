import smtplib
import os
import sys
import datetime
import mysql.connector
from tkinter import *


window = Tk()
window.title("Welcome to Society Regulation")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)

def openHome():
    window.destroy()
    os.system("py home.py " + user)
    return True


def save():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # app password: hgscfpziistxcnvp
    # Authentication
    s.login("padelkarurvi@gmail.com", "hgscfpziistxcnvp")

    # message to be sent
    message = 'Subject: {}\n\n{}'.format("Reminder",  emailbody.get())

    # sending the mail
    s.sendmail("padelkarurvi@gmail.com", email.get(), message)

    # terminating the session
    s.quit()

blankLabel = Label(window, text="  ")
titleLabel = Label(window, text="email id")
descriptionLabel = Label(window, text="Email body")

email = StringVar()
emailbody = StringVar()

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

txtEmailId = Entry(window, textvariable=email)
txtEmailBody = Entry(window, textvariable=emailbody)

btnSave = Button(window, text="Save", command=save)
btnHome = Button(window, text="Home", command=openHome)

blankLabel.grid(row=1, column=1)
titleLabel.grid(row=2, column=1)
txtEmailId.grid(row=2, column=2)
descriptionLabel.grid(row=3, column=1)
txtEmailBody.grid(row=3, column=2)
btnSave.grid(row=4, column=1)
btnHome.grid(row=4, column=2)

window.geometry('400x400')
window.mainloop()