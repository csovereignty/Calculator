from functions import *
from tkinter import *

#calcfunctions.method()

def menu_select():
    user_selection = var.get()
    if user_selection == 1:
        msg = f'It works, 1 was entered!'
    else:
        msg = f'Value other than 1 was entered, but it kind of works!'
    disp.set(msg)

running = True

#Main Window
ws = Tk()
ws.title('Calculatorialism')
ws.geometry('600x400')
ws.config(bg='#5671A6')

var = IntVar()
disp = StringVar()

Label(
    ws,
    text='Calculatorialism',
    font=('sans-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10,0))

Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 10)
).pack(pady=(50,10))

Button(
    ws,
    text='Enter selection',
    font=('sans-serif', 18),
    command=menu_select
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))

ws.mainloop()