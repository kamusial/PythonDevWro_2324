import tkinter as tk
from tkinter.messagebox import showinfo

def changed():
    showinfo(title='1', message=my_variable.get())

root = tk.Tk()
my_variable = tk.StringVar()

my_checkbox = tk.Checkbutton(root,
                             text='Zaznacz', command=changed,
                             variable=my_variable,
                             onvalue='zaznaczono', offvalue='odznaczono')
my_checkbox.pack()
root.mainloop()