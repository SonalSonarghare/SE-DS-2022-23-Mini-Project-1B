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
    mycursor = mydb.cursor()
    mycursor.execute("insert into bill(flat_no, owners_name, bill_amt, year, date) values(" + flatNo.get() + ", '" + ownerName.get() + "', " + billAmount.get() + ", " + year.get() + ", '" + date.get() + "')")
    mydb.commit()

societyLabel = Label(window, text="ABC Society", font=("Arial Bold", 17))

addressLabel1 = Label(window, text="Off Bohra Colony,Ghodbunder Road,Thane West,", font=("Arial", 6))
addressLabel2 = Label(window, text="Maharashtra 400607,India", font=("Arial", 6))

blankLabel = Label(window, text="  \n\n")
flatLabel = Label(window, text="Flat No:")
ownerLabel = Label(window, text="Owner's Name:")
billLabel = Label(window, text="Total Maintenance Bill:")
yearLabel = Label(window, text="Year:")
dateLabel = Label(window, text="Date:")


flatNo = StringVar()
ownerName = StringVar()
billAmount = StringVar()
year = StringVar()
date = StringVar()
text = StringVar()

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

txtFlatNo = Entry(window, textvariable=flatNo)
txtOwnerName = Entry(window, textvariable=ownerName)
txtBillAmount = Entry(window, textvariable=billAmount)
txtyear = Entry(window, textvariable=year)
txtDate = Entry(window, textvariable=date)

btnSave = Button(window, text="Save", command=save)
btnHome = Button(window, text="Home", command=openHome)

societyLabel.grid(column=1, row=1, columnspan=2)
addressLabel1.grid(column=1, row=2, columnspan=2)
addressLabel2.grid(column=1, row=3, columnspan=2)

blankLabel.grid(row=7)

flatLabel.grid(row=4, column=1)
txtFlatNo.grid(row=4, column=2)

ownerLabel.grid(row=5, column=1)
txtOwnerName.grid(row=5, column=2)

billLabel.grid(row=6, column=1)
txtBillAmount.grid(row=6, column=2)

yearLabel.grid(row=7, column=1)
txtyear.grid(row=7, column=2)

dateLabel.grid(row=8, column=1)
txtDate.grid(row=8, column=2)

btnSave.grid(row=9, column=1)
btnHome.grid(row=9, column=2)

window.geometry('400x500')
window.mainloop()
