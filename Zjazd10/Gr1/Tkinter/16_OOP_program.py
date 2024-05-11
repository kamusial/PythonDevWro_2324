import tkinter as tk
from tkinter import messagebox


class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x500+1400+50')
        self.root.attributes('-alpha', 0.9)
        self.root.config(background="Light Blue")

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Zamknij', command=self.zamknij)
        self.filemenu.add_command(label='czysc', command=self.czysc)

        self.filemenu2 = tk.Menu(self.menubar)
        self.filemenu2.add_command(label='Zamknij od razu', command=exit)
        self.filemenu2.add_separator()
        self.filemenu2.add_command(label='nic nie rob')

        self.menubar.add_cascade(menu=self.filemenu, label='Pierwsze')
        self.menubar.add_cascade(menu=self.filemenu2, label='Drugie')
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text='moj text')
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

        self.button = tk.Button(self.root, text='Show message', font=('Arial', 15), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.zamknij)

        self.clearbtn = tk.Button(self.root, text='czysc', font=('Arial', 16), command=self.czysc)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.mainloop()


    def short(self, event):
        # print('\nevent', event)
        # print('keysym',event.keysym)
        # print('state', event.state)
        # print('znak',event.char)
        if event.keysym == "Return" and event.state == 12:  #gdy ctrl+Enter
            self.show_message()

    def show_message(self):
        print('Wiadomosc')
        if self.check_state.get() == 0:   #jeśli checkbox NIE JEST zaznaczony
            print(self.textbox.get('1.0', tk.END))  #cały tekst
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def zamknij(self):
        if messagebox.askyesno(title='Wyjsc?', message='Czy chcesz wyjsc?'):
            self.root.destroy()   #zamknij okno

    def czysc(self):
        self.textbox.delete('1.0', tk.END)

MyGui()