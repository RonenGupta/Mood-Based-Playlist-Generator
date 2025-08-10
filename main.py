import tkinter as tk
from textblob import TextBlob


mood = str(input("How are you feeling today? "))
mood = TextBlob(mood)

print("Detected sentiment:", mood.sentiment.polarity)

root = tk.Tk()
root.mainloop()