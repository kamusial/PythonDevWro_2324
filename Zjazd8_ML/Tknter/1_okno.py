import tkinter as tk

root = tk.Tk()
root.title('Moja aplikacja')
root.geometry('600x400+100+50')
#root.resizable(True, False)  #można zmienić szerokosć okna, nie mozna zmienić wysokości
root.minsize(200, 400)
root.maxsize(800, 600)
root.attributes('-alpha', 0.9)   # przeźroczystość
root.attributes('-topmost', 1)   # zawsze na wierzchu
root.i


message = tk.Label(root, text='No siema')
message.pack()

root.mainloop()