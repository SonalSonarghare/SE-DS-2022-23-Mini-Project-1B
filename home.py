import os
from tkinter import *
import sys

window = Tk()
window.title("Welcome to Society Regulation")


def openMmemberInfo():
    window.destroy()
    os.system("py memberInfo.py " + user)
    return True

def openBill():
    window.destroy()
    os.system("py bill.py " + user)
    return True

def openReceipt():
    window.destroy()
    os.system("py reciept.py " + user)
    return True

def openRegisterComplaint():
    window.destroy()
    os.system("py registerComplaint.py " + user)
    return True

def openViewNotice():
    window.destroy()
    os.system("py viewNotice.py " + user)
    return True

def openreqs():
    window.destroy()
    os.system("py reqs.py " + user)
    return True

btnMemberInfo = Button(text="MemberInfo", command=openMmemberInfo)
btnBill = Button(text="Bill", command=openBill)
btnReceipt = Button(text="Receipt", command=openReceipt)
btnRegisterComplaint = Button(text="RegisterComplaint", command=openRegisterComplaint)
btnViewNotice = Button(text="View Notice", command=openViewNotice)
btnreq = Button(text="Request", command=openreqs)

btnMemberInfo.grid(row=1, column=1)
btnBill.grid(row=1, column=2)
btnReceipt.grid(row=1, column=3)
btnRegisterComplaint.grid(row=1, column=4)
btnViewNotice.grid(row=1, column=5)
btnreq.grid(row=1,column=6)

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

# btnLogin.pack()
window.geometry('500x500')
window.mainloop()
