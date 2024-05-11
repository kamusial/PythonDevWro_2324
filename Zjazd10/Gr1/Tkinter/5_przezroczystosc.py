import tkinter as tk

root = tk.Tk()
root.title('Przezroczystość')
root.geometry('600x400+1200+150')

root.attributes('-alpha', 0.8)  #nieprzezroczystosc

root.mainloop()
