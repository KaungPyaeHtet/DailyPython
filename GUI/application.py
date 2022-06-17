import tkinter as tk
from tkinter import TclError, ttk
import csv
from datetime import datetime
from pathlib import Path

class BoundText(tk.Text):
    """Text Widget Improved"""
    def __init__(self, *args, textvariable=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._variable = textvariable
        if self._variable:
            self.insert('1.0', self._variable.get())
            self._variable.trace_add('write', self._variable.get())
            self.bind("<<Modified>>", self._set_var)
    def _set_var(self, *_):
        if self.edit_modified():
            content = self.get('1.0', 'end-1chars')
            self._variable.set(content)
            self.edit_modified(False)
    
class LabelInput(tk.Frame):
    """A widget containing both label and entry together"""
    def __init__(self, parent, label, var, input_class=tk.Entry, input_args = None, label_args=None, **kwargs):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = var
        self.variable.label_widget = self
        if input_class in (ttk.Button, ttk.Checkbutton):
            input_args['text'] = label
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=tk.W+tk.E)
        if input_class in (ttk.Button, ttk.Radiobutton, ttk.Checkbutton):
            input_args['variable'] = self.variable
        else:
            input_args['textvariable'] = self.variable
        if input_class == ttk.Radiobutton:
            self.input = tk.Frame(self)
            for v in input_args.pop('values', []):
                button = ttk.Radiobutton(
                    self.input, text=v, value=v, **input_args
                )
                button.pack(side=tk.LEFT, ipadx=10, ipady=2 ,expand=True)
        else:
            self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W+tk.E))
        self.columnconfigure(0, weight=1)
    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        """Override grid to add default sticky values"""
        super().grid(sticky=sticky, **kwargs)
class DataRecordForm(ttk.Frame):
    """The input form for widgets"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vars = {
            'Date': tk.StringVar(),
            'Time': tk.StringVar(),
            'Technician': tk.StringVar(),
            'Lab': tk.StringVar(),
            'Plot': tk.IntVar(),
            'Seed Sample': tk.StringVar(),
            'Humidity': tk.DoubleVar(),
            'Light': tk.DoubleVar(),
            'Temperature': tk.DoubleVar(),
            'Equipment Fault': tk.BooleanVar(),
            'Plants': tk.IntVar(),
            'Blossoms': tk.IntVar(),
            'Fruit': tk.IntVar(),
            'Max Height': tk.DoubleVar(),
            'Min Height': tk.DoubleVar(),
            'Med Height': tk.DoubleVar(),
            'Notes': tk.StringVar()
        }
        r_info = self.add_frame("Record Information")
        LabelInput(r_info, "Date", var=self._vars['Date']).grid(row=0, column=0)
        LabelInput(
            r_info, "Time", input_cls=ttk.Combobox, 
            input_args={"values":['8:00', "12:00"]},
            var=self._vars['Time']
            ).grid(row=0, column=1)
        LabelInput(r_info, "Technician", var=self._vars['Technician']).grid(row=0, column=2)
        LabelInput(
            r_info,  "Lab", input_class=ttk.Radiobutton, 
            input_args={"values:",["A", "B", "C"]}, 
            var=self._vars['Lab']
            ).grid(row=1, column=0)
        LabelInput(
            r_info, "Plot", var=self._vars['Plot'],
            input_class=ttk.Spinbox,
            input_args={"values", list(range(1,21))}
            ).grid(row=1, column=1)
        LabelInput(r_info, "Sample Seed", var=self._vars['Sample Seed']).grid(row=1, column=2)

        e_info = self.add_frame("Environment Information")
        LabelInput(e_info, "Humidity", input_class= ttk.Spinbox,  input_args={"from_":0.5, "to":52.0, "increment":.01}, var=self._vars['Humidity']).grid(row=0, column=0)
        LabelInput(e_info, "Light", input_class= ttk.Spinbox,  input_args={"from_":0, "to":100, "increment":.01}, var=self._vars['Light'], ).grid(row=0, column=1)
        LabelInput(e_info, "Temperature", input_class= ttk.Spinbox, input_args={"from_":4, "to":40, "increment":.01}, var=self._vars['Temperature']).grid(row=0, column=2)
        LabelInput(e_info, "Equipment Fault", input_class=ttk.Checkbutton, var=self._vars['Equipment Fault']).grid(row=0, column=2)

        p_info = self.add_frame("Plant Information")
        LabelInput(p_info, "Plants", input_class=ttk.Spinbox, input_args={"from_":0, "to":20, "increment":1},var=self._vars['Plants']).grid(row=0, column=0)
        LabelInput(p_info, "Blossoms", input_cls=ttk.Spinbox, input_args={"from_":0, "to":20, "increment":1},var=self._vars['Blossoms']).grid(row=0, column=1)
        LabelInput(p_info, "Fruit", var=self._vars['Fruit'], input_class=ttk.Spinbox, input_args={"from_":0, "to":20, "increment":1}).grid(row=0, column=2)
        LabelInput(p_info,  "Max Height", input_class=ttk.Spinbox,  var=self._vars['Max Height'], input_args={"from_":0, "to":1000, "increment":0.1}).grid(row=1, column=0)
        LabelInput(p_info, "Min Height", var=self._vars['Min Height'],input_class=ttk.Spinbox,input_args={"from_":0, "to":1000, "increment":0.1}).grid(row=1, column=1)
        LabelInput(p_info, "Med Height", var=self._vars['Med Height'], input_class=ttk.Spinbox, input_args={"from_":0, "to":1000, "increment":0.1}).grid(row=1, column=2)
        LabelInput(self, "Notes", var=self._vars['Notes'], input_class=BoundText, input_args={"width":75, "height":10}).grid(sticky=tk.W, row=3, column=0)

        buttons = tk.Frame(self)
        buttons.grid(sticky=tk.W+tk.E, row=4)
        self.save_button = ttk.Button(
            buttons, text="Save", command=self.master._on_save
        )
        self.save_button.pack(side=tk.RIGHT)
        self.reset_button = ttk.Button(
            buttons, text="Reset", command=self.master._on_reset
        )
        self.reset_button.pack(side=tk.RIGHT)
    def reset(self):
        for var in self._vars.values():
            if isinstance(var, tk.BooleanVar):
                var.set(False)
            else:
                var.set('')
    def get(self):
        data = dict()
        fault = self._vars['Equipment Fault']
        for key, value in self._vars.items():
            if fault and key in ("Humidity", "Light", "Temperature"):
                data[key] = ''
            else:
                try:
                    data[key] = value.get()
                except TclError:
                    message = f"Error in Field: {key}. Data was not saved"
                    raise ValueError(message)
        return data
    def _add_frame(self, label,cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=(tk.W+tk.E))
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

class Application(tk.Tk):
  """Application root window"""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.title("ABQ Data Entry Application")
    self.columnconfigure(0, weight=1)

    ttk.Label(
      self, text="ABQ Data Entry Application",
      font=("TkDefaultFont", 16)
    ).grid(row=0)

    self.recordform = DataRecordForm(self)
    self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))

    # status bar
    self.status = tk.StringVar()
    ttk.Label(
      self, textvariable=self.status
    ).grid(sticky=(tk.W + tk.E), row=2, padx=10)

    self._records_saved = 0

  def _on_save(self):
    """Handles save button clicks"""

    # For now, we save to a hardcoded filename with a datestring.
    # If it doesnt' exist, create it,
    # otherwise just append to the existing file
    datestring = datetime.today().strftime("%Y-%m-%d")
    filename = "abq_data_record_{}.csv".format(datestring)
    newfile = not Path(filename).exists()

    try:
      data = self.recordform.get()
    except ValueError as e:
      self.status.set(str(e))
      return

    with open(filename, 'a', newline='') as fh:
      csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
      if newfile:
        csvwriter.writeheader()
      csvwriter.writerow(data)

    self._records_saved += 1
    self.status.set(
      "{} records saved this session".format(self._records_saved))
    self.recordform.reset()


if __name__ == "__main__":

  app = Application()
  app.mainloop()