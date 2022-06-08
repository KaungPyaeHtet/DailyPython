from tkinter import *

root = Tk()
root.geometry('400x200+650+400')
root.title('Banana Survey')

# Start
def get_pass():
    try:
        int(mybox.get())
        answer.config(text="congrats")
    except ValueError:
        answer.config(text="you silly")
password = 'kaungkaung2007'
label = Label(root, text="Write a number")
label.pack(pady=20)
mybox = Entry(root)
mybox.pack(pady=10)
mybtn = Button(root, text="submit", command=get_pass)
mybtn.pack(pady=30)
answer = Label(root, text='')
answer.pack()

root.mainloop()