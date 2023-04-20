import os
import mysql.connector
from tkinter import *


window = Tk()
window.title("Welcome to Society Regulation")

society_label = Label(window, text="ABC Society", font=("Arial Bold", 17))
address_label = Label(window, text="Ghodbunder Road, Thane West, Thane, Maharashtra 400607",font=("Arial", 8))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)


def openHome():
  window.destroy()
  os.system("py home.py")
  return True

flatLabel = Label(window, text="Flat No")
user1Label = Label(window, text="Owner 1 Name")
user2Label = Label(window, text="Owner 2 Name")
mobileLabel = Label(window, text="Mobile No")
flatValueLabel = Label(window, text="101")
user1ValueLabel = Label(window, text="Urvi Padelkar")
user2ValueLabel = Label(window, text="")
mobileValueLabel = Label(window, text="4343221")
btnMemberInfo = Button(text="Home", command=openHome)

society_label.grid(row=0, columnspan=2)
address_label.grid(row=1, columnspan=2)

#label.grid(row=0, column=0, columnspan=2)
flatLabel.grid(row=2, column=0)
flatValueLabel.grid(row=2, column=1)
user1Label.grid(row=3, column=0)
user1ValueLabel.grid(row=3, column=1)
user2Label.grid(row=4, column=0)
user2ValueLabel.grid(row=4, column=1)
mobileLabel.grid(row=5, column=0)
mobileValueLabel.grid(row=5, column=1)
btnMemberInfo.grid(row=6, column=0, columnspan=2)

window.geometry('400x400')
window.mainloop()