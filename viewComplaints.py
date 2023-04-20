import os
from tkinter import *
from  tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)

admin = "admin"  # define admin as a global variable

def openHome():
    ws.destroy()
    os.system("py admin.py " + admin)
    return True

ws  = Tk()
ws.title('Complaints')
ws.geometry('400x400')                      #for size
ws['bg'] = '#AC99F2'                        #bg colour

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('id', 'user', 'title', 'description')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("id",anchor=CENTER,width=80)
my_game.column("user",anchor=CENTER, width=80)
my_game.column("title",anchor=CENTER,width=80)
my_game.column("description",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("id",text="Id",anchor=CENTER)
my_game.heading("user",text="User",anchor=CENTER)
my_game.heading("title",text="Title",anchor=CENTER)
my_game.heading("description",text="Description",anchor=CENTER)

mycursor = mydb.cursor()

mycursor.execute(
    "SELECT id, user, title, description from complaint")
myresult = mycursor.fetchall()

indx=0
for col in myresult:
    my_game.insert(parent='',index='end',iid=indx,text='',values=(col[0],col[1],col[2],col[3]))
    indx=indx+1

my_game.pack()

btnHome = Button(ws, text="Home", command=openHome)
btnHome.pack()

ws.mainloop()

