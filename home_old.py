import tkinter as tk
from tkinter import *
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="society"
)


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Bill Page")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Receipt Page")
       label.pack(side="top", fill="both", expand=True)

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       blankLabel = Label(self, text="  ")
       titleLabel = Label(self, text="Title")
       descriptionLabel = Label(self, text="Description")

       title = StringVar()
       description = StringVar()

       txtTitle = Entry(self, textvariable=title)
       txtDescription = Entry(self, textvariable=description)

       btnSave = Button(self, text="Save")

       blankLabel.grid(row=1, column=1)
       blankLabel.grid(row=1, column=2)
       titleLabel.grid(row=2, column=1)
       txtTitle.grid(row=2, column=2)
       descriptionLabel.grid(row=3, column=1)
       txtDescription.grid(row=3, column=2)
       btnSave.grid(row=4, column=1, columnspan=2)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Member Info", command=lambda: hello())
        b2 = tk.Button(buttonframe, text="Bill", command=p2.show)
        b3 = tk.Button(buttonframe, text="Receipt", command=p3.show)
        b4 = tk.Button(buttonframe, text="Register Complaint", command=p4.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()

        def hello():
            os.system("py memberInfo.py")
            self.destroy()

            return True


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()


def openMemberInfo():
    print("Hello")

