import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
agreement = tk.StringVar()

def changed():
    showinfo(title='zaznacz', message=agreement.get())

checkbox = tk.Checkbutton(root,
               text='Zaznacz', command=changed,
               variable=agreement,
               onvalue='zaznaczono', offvalue='odznaczono')
checkbox.pack()

root.mainloop()
