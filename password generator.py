from tkinter import *
import tkinter.ttk
import random
from tkinter import messagebox

pro = Tk()
pro.geometry("500x210+250+100")
pro.title("Password Generator")
pro.resizable(False, False)
pro.iconbitmap("pass_icon.ico")


def gen():
    global scl
    scl.set("")
    password = " "
    length = password_len.get()
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()"
    if len(length) == 0:
        messagebox.showerror("Error", "Please enter your password length!")
    elif length.isalpha:
        messagebox.showerror("Error", "Please enter your password length in numbers")
    else:
        length = int(password_len.get())
        for i in range(0, length):
            password = password + random.choice(chars)
        scl.set(password)


scl = StringVar("")
title1 = Label(pro, text="Password Generator", bg="Blue", fg="White", font=("Arial", 25))
title1.pack(fill=X)

f1 = Frame(pro, width="500", height="200", bg="Light blue")
f1.place(x=0, y=40)

l1 = Label(f1, text="Length of your password: ", bg="Light blue", fg="Purple", font=("Dubai", 14))
l1.place(x=10, y=10)
passw = Label(f1, text="Your password: ", bg="Light blue", fg="Black", font=("Dubai", 14))
passw.place(x=15, y=110)

password_len = Entry(f1, width=15, justify=CENTER, font=13)
password_len.place(x=220, y=20)
passw_ent = Entry(f1, width=25, justify=CENTER, font=15, textvariable=scl)
passw_ent.place(x=150, y=118)

b1 = Button(f1, text="Generate the password", fg="Blue", bg="White", font=("Calibri", 13), command=gen)
b1.place(x=165, y=60)


pro.mainloop()
