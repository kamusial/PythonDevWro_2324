import tkinter as tk

root = tk.Tk()
root.title('Pierwsz okno')
root.geometry('600x400+1200+100')
root.resizable(False, True)   #pozwolenie na zmianę rozmiaru okna

message = tk.Label(root, text='Hello tkinter')
message.pack()

root.mainloop()
