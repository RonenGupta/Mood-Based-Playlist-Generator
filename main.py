import customtkinter as ctk
from customtkinter import CTkImage
from module import gemini_prompt
from PIL import Image

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry('800x600')
root.title('MoodTunes')
img = Image.open('Images/headphone-symbol.png')
logo = Image.open('Images/Stretched.png')

outer_frame = ctk.CTkFrame(root, fg_color="#302C2C", border_color='white',border_width=2, width=600, height=400)
outer_frame.pack(expand=True, fill="both", padx=40, pady=40)

frame = ctk.CTkFrame(outer_frame, fg_color="#0D0707", border_color='white', border_width=2)
frame.pack(expand=True)

label = ctk.CTkLabel(frame, image=CTkImage(dark_image=logo, size=(450, 150)), text='')
label.pack(padx=20, pady=10)

name_entry = ctk.CTkTextbox(frame, text_color= 'Black', fg_color='#8afa9b', scrollbar_button_color='#8afa9b', scrollbar_button_hover_color='white',
                          border_color='white', width=300, border_width=2)
name_entry.pack(padx=20, pady=10)

name_label = ctk.CTkLabel(frame, text='Enter your mood!', width=100)
name_label.pack(padx=20, pady=10)

name_button = ctk.CTkButton(frame, text='Submit', text_color='Black', hover_color='black',fg_color='#8afa9b', 
                            corner_radius=32, border_color='white', border_width=2, image=CTkImage(dark_image=img),
                            command=lambda: gemini_prompt(name_entry, name_label))
name_button.pack(padx=20, pady=10)


root.mainloop()
