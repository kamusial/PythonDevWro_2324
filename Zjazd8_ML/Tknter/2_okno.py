import tkinter as tk

root = tk.Tk()
root.title('wysrodkowane')

# window_width = 700
# window_height = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.5)   # szerokosć okna, 50% szerokości ekranu
window_height = 900
print(screen_width, screen_height)

#wyswietlić okno na środku ekranu
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

message = tk.Label(root, text='No siema')
message.pack()

root.mainloop()