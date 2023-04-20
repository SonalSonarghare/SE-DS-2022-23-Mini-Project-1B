import os
from tkinter import *
from tkinter import ttk
import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)

ws = Tk()
ws.title('Notice')
ws.geometry('400x400')
ws['bg'] = '#AC99F2'

def openHome():
    ws.destroy()
    os.system("py home.py " + user)
    return True

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('id', 'title', 'description')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("id",anchor=CENTER,width=80)
my_game.column("title",anchor=CENTER,width=80)
my_game.column("description",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("id",text="Id",anchor=CENTER)
my_game.heading("title",text="Title",anchor=CENTER)
my_game.heading("description",text="Description",anchor=CENTER)

btnHome = Button(ws, text="Home", command=openHome)
btnHome.pack()

mycursor = mydb.cursor()

mycursor.execute("SELECT id, title, description FROM notice")
myresult = mycursor.fetchall()

indx = 0
for col in myresult:
    my_game.insert(parent='', index='end', iid=indx, text='', values=(col[0], col[1], col[2]))
    indx = indx + 1

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

my_game.pack()
ws.mainloop()





