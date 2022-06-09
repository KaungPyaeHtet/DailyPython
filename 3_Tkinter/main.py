import tkinter as tk

root = tk.Tk()
root.geometry('400x300+600+400')
root.title("Kaung's Project")
root.resizable(False, False)
title = tk.Label(
    root,
    text="Kaung Playground",
    font="Arial 16 bold"
)
name_label = tk.Label(root, text="What is your name")
name_inp = tk.Entry(root)
play_inp = tk.Checkbutton(
    root,
    text="Check if you play python"
)
hour_label = tk.Label(root, text="How many hours do you play a day?")
hour_inp = tk.Spinbox(root, from_=0, to=24)
games_choices = (
    "Python", "Java", "Javascript", "Php",
    "C++", "C#", "C", "Ruby", "Rust", "Go",
    "Kotlin", "Switch", "R"
)
games_inp = tk.Listbox(root, height=len(games_choices))
for game in games_choices:
    games_inp.insert(tk.END, game)
location_label = tk.Label(root, text="Where do you code daily")
location_frame = tk.Frame(root)
location_indoor_inp = tk.Radiobutton(location_frame, text="Indoor")
location_outdoor_inp = tk.Radiobutton(location_frame, text="Outdoor")
your_review_label = tk.Label(root, text="What do you like that language and place")
your_review_inp = tk.Text(root, height=3)
submit_btn = tk.Button(root, text="Submit Survery", font="Arial 12 italic")
show_output = tk.Label(root, text='', anchor='w', justify='left')

title.grid()
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
title.grid(columnspan=2)
play_inp.grid(row=2, columnspan=2, sticky='we')


print("Success")
root.mainloop()
