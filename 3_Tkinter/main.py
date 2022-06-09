from tkinter import *

root =Tk()
root.geometry('600x400')
root.title("Sign Up / Log in")
root.resizable(False, False)
name_label = Label(
    root,
    text="Log In",
    font="Arial 16 bold"
).pack()
userName_entry = Entry(
    root
).pack()
userPsw_entry = Entry(
    root,
).pack()

root.mainloop()