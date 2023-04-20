import os
import sys
import datetime
import mysql.connector
from tkinter import *


window = Tk()
window.title("Welcome to Society Regulation")

society_label = Label(window, text="ABC Society", font=("Arial Bold", 17))
address_label = Label(window, text="Ghodbunder Road, Thane West, Thane, Maharashtra 400607", font=("Arial", 8))

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
    mycursor = mydb.cursor()
    current_date = StringVar()
    current_date = datetime.date.today()
    print(current_date)
    mycursor.execute(" insert into reqs(title, description) values('" + title.get() + "', '" + description.get() + "') ");
    mydb.commit()

blankLabel = Label(window, text="  ")
titleLabel = Label(window, text="Title")
descriptionLabel = Label(window, text="Description")

title = StringVar()
description = StringVar()

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

txtTitle = Entry(window, textvariable=title)
txtDescription = Entry(window, textvariable=description)

btnSave = Button(window, text="Submit", command=save)
btnHome = Button(window, text="Home", command=openHome)

society_label.grid(row=1, column=1, columnspan=2)
address_label.grid(row=2, column=1, columnspan=2)
titleLabel.grid(row=3, column=1)
txtTitle.grid(row=3, column=2)
descriptionLabel.grid(row=4, column=1)
txtDescription.grid(row=4, column=2)
btnSave.grid(row=5, column=1)
btnHome.grid(row=5, column=2)

window.geometry('400x400')
window.mainloop()