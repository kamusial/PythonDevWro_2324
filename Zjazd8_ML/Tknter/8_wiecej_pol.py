import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.title('kilka przyciskow')

def nic():
    print('nic nie robie')

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Close', command=exit)
filemenu.add_separator()
filemenu.add_command(label='nie rob nic', command=nic)

filemenu2 = tk.Menu(menubar)
filemenu2.add_command(label='Close', command=exit)
filemenu2.add_command(label='nie rob nic', command=nic)

menubar.add_cascade(menu=filemenu, label='Pierwszy')
menubar.add_cascade(menu=filemenu2, label='Drugi')
root.config(menu=menubar)


label = tk.Label(root, text='Hello', font=('Arial', 20), bg='blue')
label.pack(padx=20, pady=50)
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10, pady=10)
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=2)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, pady=20, padx=10)
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, pady=20, padx=10)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, pady=20, padx=10)
btn4 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, pady=20, padx=10)
btn5 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, pady=20, padx=10)
btn6 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, pady=20, padx=10)
buttonframe.pack(fill='x')

nextbtn = tk.Button(root, text='TEST')
nextbtn.place(x=200, y=400, height=100, width=100)


root.mainloop()