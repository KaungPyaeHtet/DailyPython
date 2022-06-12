import tkinter as tk
import json

class LabelInput(tk.Frame):
    def __init__(self, parent, label, cls_inp, cls_arg, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label, anchor='w')
        self.input= cls_inp(self, **cls_arg)
        self.columnconfigure(0, weight=1)
        self.label.grid(sticky=tk.W + tk.E)
        self.input.grid(sticky=tk.W+tk.E)
root = tk.Tk()
textvar = tk.StringVar()
LabelInput(root, 'Name', tk.Spinbox, {"textvariable":textvar, "from_":1, "to":10})

root.mainloop()