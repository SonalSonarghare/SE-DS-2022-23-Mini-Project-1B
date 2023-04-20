import tkinter as tk
from tkinter import *
import os
import sys

window = Tk()
window.title("Welcome to Society Regulation")

def openManageMember():
    window.destroy()
    os.system("py registerMember.py " + user)
    return True

def openAddNotice():
    window.destroy()
    os.system("py addNotice.py " + user)
    return True

def openViewComplaints():
    window.destroy()
    os.system("py viewComplaints.py " + user)
    return True



btnManageMember = Button(text="Manage Member", command=openManageMember)
btnAddNotice = Button(text="Add Notice", command=openAddNotice)
btnViewComplaints = Button(text="View Complaints", command=openViewComplaints)

btnManageMember.grid(row=1, column=1)
btnAddNotice.grid(row=1, column=2)
btnViewComplaints.grid(row=1, column=3)

user = sys.argv[1]

# btnLogin.pack()
window.geometry('400x400')
window.mainloop()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Manage Member")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Add Notice")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="View Complains")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Manage Member", command=showRegister)
        b2 = tk.Button(buttonframe, text="Add Notice", command=p2.show)
        b3 = tk.Button(buttonframe, text="View Complains", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()