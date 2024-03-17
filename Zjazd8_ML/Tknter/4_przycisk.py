import tkinter as tk
from tkinter.messagebox import showinfo

def clicked():
    showinfo(title='Informacja', message='Potwierdz')

root = tk.Tk()

button = tk.Button(root, text='info', command=clicked)
button.pack(ipadx=110, ipady=10, expand=True)   # ipad - wielkosc przycisku

root.mainloop()