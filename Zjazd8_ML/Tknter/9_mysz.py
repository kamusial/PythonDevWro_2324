from tkinter import *

root = Tk()
root.geometry('800x500')

def callback(e):
    x = e.x
    y = e.y
    if x % 10 == 0 or y % 10 == 0:
        print(f'Wspolzedne myszy to {x} {y}')

def hello(e):
    print('klik')

def wyjscie(e):
    print('podwojne klikniecie, koniec')
    import sys; sys.exit()

root.bind('<Motion>', callback)
root.bind('<Double-1>', wyjscie)
root.bind('<Button-1>', hello)
root.mainloop()