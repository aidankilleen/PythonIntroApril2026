# tk_investigation

from tkinter import Frame, Listbox, Tk, Button, messagebox
import tkinter as tk
from user import User
from userdao import UserDao

dao = UserDao()
users = dao.get_users()

root = Tk()
root.geometry("600x400")
frm = Frame(root)

def on_click():
    print("clicked")
    messagebox.showinfo("Clicked", "You clicked the button")
    pass

btn = Button(root, text="Press Me", command=on_click)
btn.pack()

list_box = Listbox(root)
list_box.pack()

for user in users:
    list_box.insert(tk.END, user.name)

root.mainloop()




