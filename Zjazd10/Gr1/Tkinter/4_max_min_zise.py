import tkinter as tk

root = tk.Tk()
root.title('Wysrodkowane')
window_width = 300
window_height = 200

#pobranie wielkosci ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.minsize(200, 200)
root.maxsize(600, 400)

root.mainloop()
