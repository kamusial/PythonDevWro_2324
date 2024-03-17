import tkinter as tk

root = tk.Tk()
root.title('Moja aplikacja')
root.geometry('600x400+100+50')
message = tk.Label(root, text='No siema')
message.pack()

root.mainloop()