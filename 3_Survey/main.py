import tkinter as tk

# Window Setup
root = tk.Tk()
root.geometry('800x600+400+300')
root.title("Survey")
root.resizable(False, False)

# Labels
title = tk.Label(
    root,
    text="Programming Survery",
    font="Arial 16 bold"
)
title.configure(fg='#ffffff', bg='#000000')
# Username
name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What is your name: ")
name_inp = tk.Entry(root, textvariable=name_var)

# Check if user like python
play_var = tk.BooleanVar()
play_inp = tk.Checkbutton(
    root,
    text="Check if you play python",
    variable=play_var
)

# Hour of coding
hour_var = tk.IntVar(value=3)
hour_label = tk.Label(root, text="How many hours do you play a day?")
hour_inp = tk.Spinbox(root, textvariable=hour_var,from_=0, to=24)

# Best Programming Choice
game_var = tk.StringVar(value='Python')
game_label = tk.Label(root, text="What is the best language for programming?")
games_choices = (
    "Python", "Java", "Javascript", "Php",
    "C++", "C#", "C", "Ruby", "Rust", "Go",
    "Kotlin", "Switch", "R"
)
games_inp = tk.OptionMenu(root, game_var, *games_choices)


# Place of Coding
location_var = tk.BooleanVar()
location_label = tk.Label(root, text="Where do you code daily")
location_frame = tk.Frame(root)
location_indoor_inp = tk.Radiobutton(location_frame, text="Indoor", value=True, variable=location_var)
location_outdoor_inp = tk.Radiobutton(location_frame, text="Outdoor", value=False, variable=location_var)

# Review Part
your_review_label = tk.Label(root, text="Why do you like that language", font="Arial 15 bold")
your_review_inp = tk.Text(root, height=3)

# Submit and Output
show_var = tk.StringVar(value='')
submit_btn = tk.Button(root, text="Submit Survery", font="Arial 12 italic")
show_output = tk.Label(root, textvariable=show_var, anchor='w')

# Grid
title.grid(columnspan=2)

name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)

play_inp.grid(row=2, columnspan=2, sticky='we')

hour_inp.grid(row=3, sticky=(tk.E + tk.N))
hour_label.grid(row=3, column=1, sticky=(tk.W))

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

root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

# Functions
def on_submit():
    name = name_var.get()
    try:
        hour = hour_var.get()
    except tk.TclError:
        hour = 4
    play = play_var.get()
    game = game_var.get()
    location = location_var.get()
    review = your_review_inp.get('1.0', tk.END)
    message = f'Thank you for taking survey, {name}\n'
    if not hour:
        message += 'So you don\'t like coding\n'
    else:
        message += f'You code {game} {hour} hours daily\n'
    if location:
        message += f'You code {location}\n'
    else:
        message += f'You don\'t code on earth\n'
    if review.strip():
        message += f"Your review:\n {review}"
    show_var.set(message)

submit_btn.configure(command=on_submit)

print("Success")
root.mainloop()
