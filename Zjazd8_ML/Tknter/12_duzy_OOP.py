import tkinter as tk
from tkinter import messagebox

class MyGui:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Pierwszy OOP')
        self.root.geometry('600x400+1300+50')
        self.root.attributes('-alpha', 0.8)
        self.root.attributes('-topmost', 1)
        self.root.config(background='Light Blue')

        self.label = tk.Label(self.root, text='Reagujemy na klawisze')
        self.label.config(
            background='#555',
            fg='#ccc',
            font=('Arial', 20),
            padx=20,
            pady=10)
        self.label.pack()

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15))
        self.textbox.bind('<KeyPress>', self.short)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='show', font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='show message', font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.zamknij)

        self.root.mainloop()

    def zamknij(self):
        print('Zamykam')
        if messagebox.askyesno(title='Potwierdzenie', message='Czy napewno?'):
            self.root.destroy()

    def short(self, event):
        print(event)
        print(event.keysym)
        print(event.state)
        if event.keysym == 'Return' and event.state == 12:
            self.zamknij()

    def show_message(self):
        print('Wiadomosc')
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Wiadomosc', message=self.textbox.get('1.0', tk.END))


MyGui()

