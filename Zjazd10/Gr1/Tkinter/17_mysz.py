from tkinter import *

win = Tk()
win.geometry('600x400+1300+100')

def callback(e):
#    print(f'wszystko ',e)
    x = e.x
    y = e.y
    if x % 10 == 0 or y % 10 == 0:
        print('Wskaznik jest na pozycji %d, %d'%(x, y))

win.bind('<Motion>', callback)


win.mainloop()