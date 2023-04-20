import os
import sys
from tkinter import *

window = Tk()
window.title("Register Member")

def showHome():
    window.destroy()
    os.system("py admin.py " + user)
    return True

registerLabel = Label(window, text="New Member")
flatLabel = Label(window, text="Flat No")
user1Label = Label(window, text="Owner 1 Name")
user2Label = Label(window, text="Owner 2 Name")
mobileLabel = Label(window, text="Mobile No")

varFlat = StringVar()
varUser1Name = StringVar()
varUser2Name = StringVar()
varMobile = StringVar()

txtFlat = Entry(window, textvariable=varFlat)
txtUser1 = Entry(window, textvariable=varUser1Name)
txtUser2 = Entry(window, textvariable=varUser2Name)
txtMobile = Entry(window, textvariable=varMobile)

btnLogin = Button(text="Register")
btnHome = Button(text="Home", command=showHome)

registerLabel.grid(row=0, column=0, columnspan=2)
flatLabel.grid(row=1, column=0)
txtFlat.grid(row=1, column=1)
user1Label.grid(row=2, column=0)
txtUser2.grid(row=2, column=1)
mobileLabel.grid(row=3, column=0)
txtMobile.grid(row=3, column=1)
btnLogin.grid(row=4, column=0)
btnHome.grid(row=4, column=1)
# btnLogin.pack()

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

window.geometry('400x400')
window.mainloop()
