import tkinter as tk
root = tk.Tk()
root.title('Pojemniki')
root.geometry('400x200+1300+100')
root.attributes('-topmost', 1)   # zawsze na wierzchu

box1 = tk.Label(root, text='pole1', bg='green', fg='white')
box1.pack(ipady=10, fill=tk.X, padx=10, pady=20)
box2 = tk.Label(root, text='pole2', bg='red', fg='white')
box2.pack(ipadx=30, ipady=30, fill=tk.BOTH, expand=True)

root.mainloop()