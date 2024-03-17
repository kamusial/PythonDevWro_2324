import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('600x400+100+50')
my_text = tk.StringVar()

def clicked():
    msg = f'wpisales: {my_text.get()}'
    showinfo(title='info', message=msg)

frame = tk.Frame(root)
frame.pack(padx=30, pady=30, fill='x', expand=True)

label = tk.Label(frame, text='wpisz text')
label.pack()

entry = tk.Entry(frame, textvariable=my_text)
entry.pack(fill='x')

button = tk.Button(frame, text='kliknij', command=clicked)
button.pack(fill='x', expand=True, pady=20)


root.mainloop()