from functions import *
from tkinter import *

calcfunctions.method()

running = True

#Main Window
mainWindow = Tk()
mainWindow.title('Calculatorism')
mainWindow.geometry('400x300')
mainWindow.config(bg='#F2B33D')

frame = Frame(mainWindow, bg='#F2B33D')
#example of padding
Button(mainWindow, text = "Addition", command=print_menu).grid(row=0, column=0, padx=10, pady=10, sticky='ew')
Button(mainWindow, text = "Subtraction", command=None).grid(row=0, column=1)

mainWindow.mainloop()

while(running):
    option = None
    print_menu()
    option = int(input("Enter your selection: "))
    print(f'You have selected option #{option}')
    if option == 0:
        running = False
    else:
        option = option_select(option)