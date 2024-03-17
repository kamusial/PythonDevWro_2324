import tkinter as tk
#from tkinter import ttk
# def f1():
#     print('Hej')

root = tk.Tk()

button = tk.Button(root, text='Wyjscie', command=root.quit)
button.pack(ipadx=110, ipady=10, expand=True)   # ipad - wielkosc przycisku

root.mainloop()