import os
import sys
import mysql.connector
from tkinter import *


window = Tk()
window.title("Add Notice")

society_label = Label(window, text="ABC Society", font=("Arial Bold", 17))
address_label = Label(window, text="Ghodbunder Road, Thane West, Thane, Maharashtra 400607",font=("Arial", 8),anchor=CENTER)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)

def openHome():
    window.destroy()
    os.system("py admin.py " + user)
    return True


def save():
    mycursor = mydb.cursor()
    print(user)
    mycursor.execute("insert into notice(title, description) values('" + title.get() + "', '" + description.get() + "')")
    mydb.commit()

#blankLabel = Label(window, text="  ")
titleLabel = Label(window, text="Title")
descriptionLabel = Label(window, text="Description")

title = StringVar()
description = StringVar()
user = sys.argv[1]
txtTitle = Entry(window, textvariable=title)
txtDescription = Entry(window, textvariable=description)

btnSave = Button(window, text="Save", command=save)
btnHome = Button(window, text="Home", command=openHome)

society_label.grid(row=0, column=1, columnspan=2)
address_label.grid(row=1, column=1, columnspan=2)

#blankLabel.grid(row=1, column=1)
#blankLabel.grid(row=1, column=2)
titleLabel.grid(row=2, column=1)
txtTitle.grid(row=2, column=2)
descriptionLabel.grid(row=3, column=1)
txtDescription.grid(row=3, column=2)
btnSave.grid(row=4, column=1)
btnHome.grid(row=4, column=2)


window.geometry('400x400')
window.mainloop()