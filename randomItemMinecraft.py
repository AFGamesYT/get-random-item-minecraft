import json
from random import choice
import tkinter as tk

root = tk.Tk()
root.geometry("800x150")
root.title("Get Random Item")

with open('items.json', 'r') as file:
    items = json.load(file)

item = choice(items)

label = tk.Label(root, text=item, font=("Arial", 32))
label.pack()

def on_button_click():
    global item, label
    item = choice(items)
    label['text'] = item

button = tk.Button(root, text="Get Another Item", command=on_button_click, font=("Arial", 25))
button.pack()

root.mainloop()

