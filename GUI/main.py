import tkinter as tk
from datetime import datetime

class LabelInput(tk.Frame):
    def __init__(self, parent, labels, *args, **kwargs):
        super().__init__(parent, **kwargs)
        self.label = tk.Label(self, text=labels).pack()
        self.entry = tk.Entry(self).pack()
        
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        LabelInput(self, labels='Hello Everyone')

if __name__ == "__main__":
    app = App("root")
    app.mainloop()

        