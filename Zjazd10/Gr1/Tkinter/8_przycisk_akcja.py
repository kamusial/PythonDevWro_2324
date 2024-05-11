import tkinter as tk

root = tk.Tk()
exit_button = tk.Button(root, text='Wyjscie', command=root.quit)
exit_button.pack(ipadx=5, ipady=15, expand=True)

root.mainloop()
