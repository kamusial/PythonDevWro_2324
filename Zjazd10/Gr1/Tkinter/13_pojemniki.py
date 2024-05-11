import tkinter as tk

root = tk.Tk()
root.title('pojemniki')
root.geometry('400x200')

box1 = tk.Label(root,text='Pojemnik1', bg='green', fg='white')
box1.pack(fill=tk.X, ipady=10)
box2 = tk.Label(root,text='Pojemnik2', bg='red', fg='white')
box2.pack(ipadx=20, ipady=20, pady=5, fill=tk.BOTH, expand=True)

root.mainloop()