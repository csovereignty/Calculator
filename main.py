from functions import *
from tkinter import *

calcfunctions.method()

running = True

#Main Window
mainWindow = Tk()
#mainWindowTitle = Label(mainWindow, text="Calculatorialism")
#mainWindowTitle.pack()
#mainWindow.mainloop()
mainWindow.geometry('100x100')

btn = Button(mainWindow, text = "Click me!", bd = '5', command=mainWindow.destroy)
btn.pack(side = 'top')

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