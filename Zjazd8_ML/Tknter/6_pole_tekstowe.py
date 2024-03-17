import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('600x400+100+50')
my_text = tk.StringVar()

frame = tk.Frame(root)
frame.pack(padx=30, pady=30, fill='x', expand=True)

label = tk.Label(frame, text='wpisz text')
label.pack()

entry = tk.Entry(frame)
entry.pack(fill='x')

button = tk.Button(frame, text='kliknij')
button.pack(fill='x', expand=True, pady=20)


root.mainloop()