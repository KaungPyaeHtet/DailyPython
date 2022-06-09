import tkinter as tk

# Window Setup
root = tk.Tk()
root.geometry('800x600+400+300')
root.title("Kaung's Project")
root.resizable(False, False)

# Labels
title = tk.Label(
    root,
    text="Kaung Playground",
    font="Arial 16 bold"
)

# Username
name_label = tk.Label(root, text="What is your name: ")
name_inp = tk.Entry(root)

# Check if user like python
play_inp = tk.Checkbutton(
    root,
    text="Check if you play python"
)

# Hour of coding
hour_label = tk.Label(root, text="How many hours do you play a day?")
hour_inp = tk.Spinbox(root, from_=0, to=24)

# Best Programming Choice
game_label = tk.Label(root, text="What is the best language for programming?")
games_choices = (
    "Python", "Java", "Javascript", "Php",
    "C++", "C#", "C", "Ruby", "Rust", "Go",
    "Kotlin", "Switch", "R"
)
games_inp = tk.Listbox(root, height=len(games_choices))
for game in games_choices:
    games_inp.insert(tk.END, game)

# Place of Coding
location_label = tk.Label(root, text="Where do you code daily")
location_frame = tk.Frame(root)
location_indoor_inp = tk.Radiobutton(location_frame, text="Indoor")
location_outdoor_inp = tk.Radiobutton(location_frame, text="Outdoor")

# Review Part
your_review_label = tk.Label(root, text="What do you like that language and place")
your_review_inp = tk.Text(root, height=3)

# Submit and Output
submit_btn = tk.Button(root, text="Submit Survery", font="Arial 12 italic")
show_output = tk.Label(root, text='', anchor='w', justify='left')

# Grid
title.grid(columnspan=2)

name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)

play_inp.grid(row=2, columnspan=2, sticky='we')

hour_inp.grid(row=3, sticky=(tk.W))
hour_label.grid(row=3, column=1, sticky=(tk.W + tk.E))

game_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
games_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

location_indoor_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
location_outdoor_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
location_label.grid(row=6, columnspan=2, sticky=tk.W + tk.E)
location_frame.grid(row=7, columnspan=2, sticky=tk.W)

your_review_label.grid(row=8, sticky=tk.W)
your_review_inp.grid(row=9, columnspan=2, sticky='NESW')

submit_btn.grid(row=99)
show_output.grid(row=100, columnspan=2, sticky='NSEW')
print("Success")
root.mainloop()
