import tkinter as tk
from tkinter import messagebox


class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x500+1400+100')
        self.label = tk.Label(self.root, text='moj text')
        self.label.config(
            background='#555',
            fg='#ccc',
            font=('Arial', 20),
            padx=20,
            pady=10)
        self.label.pack()

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15))
        self.textbox.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text='show', font=('Arial', 15))
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show message', font=('Arial', 15))
        self.button.pack(padx=10, pady=10)


        self.root.mainloop()


MyGui()