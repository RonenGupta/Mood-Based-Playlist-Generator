import customtkinter as ctk
from module import gemini_prompt

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry('500x400')
root.title('MoodTunes')

name_entry = ctk.CTkEntry(root, text_color= 'Black', fg_color='#8afa9b', placeholder_text="Enter the mood")
name_entry.pack(padx=20, pady=10)
name_label = ctk.CTkLabel(root, text='Enter your mood!')
name_label.pack(padx=20, pady=10)
name_button = ctk.CTkButton(root, text='Submit', text_color='Black', fg_color='#8afa9b', command=lambda: gemini_prompt(name_entry, name_label))
name_button.pack(padx=20, pady=10)


root.mainloop()
