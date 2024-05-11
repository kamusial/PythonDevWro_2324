import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()

def button_clicked():
    showinfo(title='potwierdzenie', message='czy napewno?')

button_icon = tk.PhotoImage(file='./merito.png')

button = tk.Button(
    root, image=button_icon,
    text='przycisk',
    compound=tk.TOP,
    command=button_clicked)
button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()