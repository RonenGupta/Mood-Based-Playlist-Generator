import tkinter as tk
from tkinter import ttk
from module import synthesise_input

root = tk.Tk()
root.geometry('500x400')
root.title('MoodTunes')
root.configure(bg="Black")

name_entry = tk.Entry(root, text="Enter the mood")
name_entry.pack(padx=20, pady=10)

name_label = ttk.Label(root, text='Enter your mood!')
name_label.pack(padx=20, pady=10)
name_button = ttk.Button(root, text='Submit', command=lambda: synthesise_input(name_entry, name_label))
name_button.pack(padx=20, pady=10)


root.mainloop()
