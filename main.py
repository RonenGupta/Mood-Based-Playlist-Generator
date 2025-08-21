import customtkinter as ctk
from customtkinter import CTkImage
from module import gemini_prompt
from PIL import Image

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry('800x500')
root.title('MoodTunes')
root.resizable(False, False)
img = Image.open('Images/headphone-symbol.png')
logo = Image.open('Images/Stretched.png')

outer_frame = ctk.CTkFrame(root, fg_color="#211F1F", border_color='white',border_width=2, width=600, height=400)
outer_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame = ctk.CTkFrame(outer_frame, fg_color="#0D0707", border_color='white', border_width=2)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

secondframe = ctk.CTkFrame(outer_frame, fg_color="#0D0707", border_color='white', border_width=2, width=200, height=200)
secondframe.grid(row=0, column=1, padx=10, pady=10, sticky="n")

thirdframe = ctk.CTkFrame(outer_frame, fg_color="#0D0707", border_color='white', border_width=2, width=220, height=100)
thirdframe.place(x=500, y=230)

label = ctk.CTkLabel(frame, image=CTkImage(dark_image=logo, size=(450, 150)), text='')
label.pack(padx=10, pady=5)

name_entry = ctk.CTkTextbox(frame, text_color= 'Black', fg_color='#8afa9b', scrollbar_button_color='#8afa9b', scrollbar_button_hover_color='white',
                          border_color='white', width=300, border_width=2)
name_entry.pack(padx=10, pady=5)

name_label = ctk.CTkLabel(thirdframe, text='Enter your mood!', width=200, height=90, font=('Lexend', 9), wraplength=180)
name_label.pack(padx=10, pady=5)

playlistlabel = ctk.CTkLabel(secondframe, image=CTkImage(dark_image=img, size=(200, 200)), text="Playlist image will appear here!")
playlistlabel.pack(padx=10, pady=5)

name_button = ctk.CTkButton(frame, text='Get your recommendation!', text_color='Black', hover_color="#52995c",fg_color='#8afa9b', 
                            corner_radius=32, border_color='white', border_width=2, image=CTkImage(dark_image=img),
                            command=lambda: gemini_prompt(name_entry, name_label, playlistlabel))
name_button.pack(padx=10, pady=5)

root.mainloop()
