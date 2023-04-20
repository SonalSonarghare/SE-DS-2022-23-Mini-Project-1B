import os
import sys
import datetime
import mysql.connector
from tkinter import *

window = Tk()
window.title("Receipt")
window.geometry("400x400")

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

def getDetail():
    mycursor = mydb.cursor()
    mycursor.execute(
        "select owners_name, bill_amt from bill where flat_no='" + flatNo.get() + "'")

    myresult = mycursor.fetchall()

    name = ""
    amt = ""
    for x in myresult:
        name = x[0]
        amt = x[1]
    ownerName.set(name)
    billAmount.set(amt)

def save():
    mycursor = mydb.cursor()
    current_date = StringVar()
    current_date = datetime.date.today()
    mycursor.execute(
        "insert into receipt(flat_no, owners_name, bill_amt, cheque_no, cheque_date,cheque_amt) values('" + flatNo.get() + "', '" + ownerName.get() + "', '" + billAmount.get() + "', '" + chequeNo.get() + "', '" + txtChequeDate.get() + "', "+chequeamt.get()+")")
    mydb.commit()

    # Generate receipt
    receipt = Toplevel(window)
    receipt.title("Receipt")

    # Create labels and display data from form
    societyLabel = Label(receipt, text="ABC Society", font=("Arial Bold", 17))
    societyLabel.pack()

    addressLabel = Label(receipt, text="Off Bohra Colony,Ghodbunder Road,Thane West,Thane, Maharashtra 400607,India",
                         font=("Arial", 6))
    addressLabel.pack()

    receiptDate = Label(receipt, text="Date: " + str(current_date))
    receiptDate.pack()

    receiptFlat = Label(receipt, text="Flat No.: " + flatNo.get())
    receiptFlat.pack()

    receiptOwner = Label(receipt, text="Owner's Name: " + ownerName.get())
    receiptOwner.pack()

    receiptAmount = Label(receipt, text="Total Maintenance Bill: Rs." + billAmount.get())
    receiptAmount.pack()

    #receiptCheque = Label(receipt, text="Cheque No.: " + chequeNo.get())
    #receiptCheque.pack()

    #receiptChequeDate = Label(receipt, text="Cheque Date: " + txtChequeDate.get())
    #receiptChequeDate.pack()

    #receiptText = Label(receipt, text="Complaint: " + text.get('1.0', END))
    #receiptText.pack()

    btnForm = Button(receipt, text="Back to Form", command=receipt.destroy)
    btnForm.pack()

    btnHome = Button(receipt, text="Home", command=openHome)
    btnHome.pack()


#societyLabel = Label(window, text="ABC Society", font=("Arial Bold", 17))

#addressLabel = Label(window, text="Off Bohra Colony,Ghodbunder Road,Thane West,Thane, Maharashtra 400607,India",
                     #font=("Arial", 6))

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

blankLabel = Label(window, text="  ")
flatLabel = Label(window, text="Flat No:")
ownerLabel = Label(window, text="Owner's Name:")
billLabel = Label(window, text="Total Maintenance Bill:")
chequeLabel = Label(window, text="Cheque No:")
chequeDateLabel = Label(window, text="Cheque Date:")
chequeamtLabel = Label(window, text="Cheque Amount:")
#complaintLabel = Label(window, text="Complaint:")

flatNo = StringVar()
ownerName = StringVar()
billAmount = StringVar()
chequeNo = StringVar()
txtChequeDate = StringVar()
chequeamt = StringVar()
#text = Text(window, height=10, width=30)

flatEntry = Entry(window, textvariable=flatNo)
ownerEntry = Entry(window, textvariable=ownerName)
billEntry = Entry(window, textvariable=billAmount)
chequeEntry = Entry(window, textvariable=chequeNo)
chequeDateEntry = Entry(window, textvariable=txtChequeDate)
chequeamtEntry = Entry(window, textvariable=chequeamt)
#complaintEntry = Entry(window, textvariable=text)

#societyLabel.pack()
#addressLabel.pack()
blankLabel.pack()
flatLabel.pack()
flatEntry.pack()
ownerLabel.pack()
ownerEntry.pack()
billLabel.pack()
billEntry.pack()
chequeLabel.pack()
chequeEntry.pack()
chequeDateLabel.pack()
chequeDateEntry.pack()
chequeamtLabel.pack()
chequeamtEntry.pack()
#complaintLabel.pack()
#complaintEntry.pack()

btnSave = Button(window, text="Save", command=save)
btnSave.pack()

btnGet = Button(window, text="Get", command=getDetail)
btnGet.pack()

window.geometry('400x500')
window.mainloop()
