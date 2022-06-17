""""Data Entry Using CSV"""
from tkinter import ttk
from pathlib import Path
from datetime import datetime
import tkinter as tk
import csv

# Setting Up Window
variables = dict()
records_saved = 0
root = tk.Tk()
root.title("Data Entry Application")
root.columnconfigure(0, weight=1)
root.resizable(False, False)

# Heading
ttk.Label(
    root,
    text="Data Entry Application",
    font=("TkDefaultFont", 16),
).grid()

# Data Form
drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E+tk.W))
drf.columnconfigure(0, weight=1)

# Record Information Section 
r_info = ttk.Labelframe(drf, text="Record Information Section")
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)

# Date
variables['Date'] = tk.StringVar()
ttk.Label(r_info, text="Date").grid(row=0, column=0)
ttk.Entry(
    r_info,
    textvariable=variables['Date'],
).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Time
time_values = [
    '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text="Time").grid(row=0, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Time'],
    values=time_values,
).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Technician
variables['Technician'] = tk.StringVar()
ttk.Label(r_info, text="Technician").grid(row=0, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['Technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Lab
variables['Lab'] = tk.StringVar()
ttk.Label(r_info, text="Lab").grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ("A", "B", "C"):
    ttk.Radiobutton(
        labframe,
        value=lab,
        text=lab,
        variable=variables['Lab']
    ).pack(side=tk.LEFT, expand=True)
labframe.grid(row=3,column=0)

# Plot
variables['Plot'] = tk.IntVar()
ttk.Label(r_info, text="Plot").grid(row=2, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Plot'],
    values=list(range(1,21)),
    justify="center"
).grid(row=3, column=1, sticky=(tk.W + tk.E))

# SeedSample
variables['Seed Sample'] = tk.StringVar()
ttk.Label(r_info, text="Seed Sample").grid(row=2, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['Seed Sample']
).grid(row=3, column=2, sticky=(tk.W + tk.E))

# Environment Data Section
e_info = ttk.LabelFrame(drf, text="Environment Data Section")
e_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    e_info.columnconfigure(i, weight=1)

# Humidity (g/m³)
variables['Humidity'] = tk.DoubleVar()
ttk.Label(e_info, text="Humidity (g/m³)").grid(row=0, column=0)
ttk.Spinbox(
    e_info,
    textvariable=variables['Humidity'],
    from_=0.5,
    to=52.0,
    increment=0.01,
).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Light
variables['Light'] = tk.DoubleVar()
ttk.Label(e_info, text="Light (klx)").grid(row=0, column=1)
ttk.Spinbox(
    e_info,
    textvariable=variables['Light'],
    from_=0,
    to=100,
    increment=0.1,
).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Temperature
variables['Temperature'] = tk.DoubleVar()
ttk.Label(e_info, text="Temperature (C)").grid(row=0, column=2)
ttk.Spinbox(
    e_info,
    textvariable=variables['Temperature'],
    from_=4,
    to=40,
    increment=0.01,
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Equipment faliure
variables['Equipment Failure'] = tk.BooleanVar(value=False)
ttk.Checkbutton(
    e_info,
    text="Equipment Failure",
    variable=variables['Equipment Failure']
).grid(row=2, column=0, pady=5,sticky=(tk.W + tk.E))

# Plant Data Section
p_info = ttk.LabelFrame(drf, text="Plant Data Section")
p_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

# Plants
variables['Plants'] = tk.IntVar()
ttk.Label(p_info, text='Plants').grid(row=0, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Plants'],
    from_=0, to=20, increment=1
).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Blossoms
variables['Blossoms'] = tk.IntVar()
ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Blossoms'],
    from_=0, to=1000, increment=1
).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Fruits
variables['Fruits'] = tk.IntVar()
ttk.Label(p_info, text='Fruits').grid(row=0, column=2)
ttk.Spinbox(
    p_info, textvariable=variables['Fruits'],
    from_=0, to=1000, increment=1
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Min Height
variables['Min Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Minimum Height (cm)').grid(row=2, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Min Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Max Height
variables['Max Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Maximum Height (cm)').grid(row=2, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Max Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=1, sticky=(tk.W + tk.E))

# Med Height
variables['Med Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Median Height (cm)').grid(row=2, column=2)
ttk.Spinbox(
    p_info, textvariable=variables['Med Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=2, sticky=(tk.W + tk.E))

# Notes
ttk.Label(drf, text='Notes').grid()
notes_inp = tk.Text(drf, width=75, height=10)
notes_inp.grid(sticky=(tk.W + tk.E), pady=10)

# buttons
buttons = ttk.Frame(drf)
buttons.grid(sticky=(tk.W + tk.E))
save_button = ttk.Button(buttons, text="Save")
save_button.pack(side=tk.RIGHT)
reset_button = ttk.Button(buttons, text="Reset")
reset_button.pack(side=tk.LEFT)

# Status Variable
status_var = tk.StringVar()
ttk.Label(
    root,
    textvariable=status_var
).grid(sticky=(tk.W + tk.E), row=99, padx=10)

# Reset Command
def on_reset():
    for variable in variables.values():
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set("")
    notes_inp.delete('1.0', tk.END)

def on_save():
    global records_saved
    datestring = datetime.today().strftime('%Y-%m-%d')
    filename = f"kaung_{datestring}.csv"
    fault = variables['Equipment Failure'].get()
    newfile = not Path(filename).exists()
    data = dict()
    for key, variable in variables.items():
        if fault and key in ('Humidity', 'Light', 'Temperature'):
            data[key] = ''
        else:
            try:
                data[key] = variable.get()
            except tk.TclError:
                status_var.set(
                    f"Error in field: {key}"
                )
                return
        data["Note"] = notes_inp.get('1.0', tk.END)
    with open(filename, 'a', newline='') as fh:
        csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
        if newfile:
            csvwriter.writeheader()
        csvwriter.writerow(data)
    records_saved += 1
    status_var.set(
        f"{records_saved} records have been saved this session"
    )
    on_reset()
    
save_button.configure(command=on_save)
on_reset()
root.mainloop()