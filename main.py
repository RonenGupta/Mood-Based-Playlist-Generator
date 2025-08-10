import tkinter as tk
from tkinter import ttk
from transformers import pipeline

pipeline = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

def synthesise_input(name_entry, name_label):
    user_input = name_entry.get()
    if user_input:
        user_input = pipeline(user_input)
        sentiment = user_input[0]['label']
        score = user_input[0]['score']
        name_label.config(text= f"Your score: {sentiment}, and the model's confidence: {score}")
        print(f"Detected Sentiment: {sentiment} (Confidence: {score:})")
    else:
        print("Please enter a mood!")

root = tk.Tk()
root.geometry('500x400')
root.title('MoodTunes')

name_entry = ttk.Entry(root, text="Enter the mood")
name_entry.pack(padx=20, pady=10)

name_label = tk.Label(root, text='Enter your mood!')
name_label.pack(padx=20, pady=10)
name_button = ttk.Button(root, text='Submit', command=lambda: synthesise_input(name_entry, name_label))
name_button.pack(padx=20, pady=10)


root.mainloop()
