from tkinter import *
from tkinter import messagebox

def fun1(e):
    print('pojedyncze klikniecie przycisku 1')

def fun2(e):
    print('zatrzymajmy')
    if messagebox.askyesno(title='Potwierdzenie', message='Czy wyjsc?'):
        import sys; sys.exit()


widget = Button(None, text='Klikanie myszy')
widget.pack()
widget.bind('<Button-1>', fun1)
widget.bind('<Double-3>', fun2)
widget.mainloop()

