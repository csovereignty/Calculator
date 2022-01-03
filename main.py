from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equals():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expresion = ""
    except:
        equation.set("Error!")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

running = True

#Main Window
ws = Tk()
ws.title('Calculatorialism')
ws.geometry('270x150')
ws.config(bg="black")
var = IntVar()
equation = StringVar()

expression_field = Entry(ws, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
button1 = Button(ws, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)
 
button2 = Button(ws, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
 
button3 = Button(ws, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
 
button4 = Button(ws, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
 
button5 = Button(ws, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
 
button6 = Button(ws, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
 
button7 = Button(ws, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
 
button8 = Button(ws, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
 
button9 = Button(ws, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
 
button0 = Button(ws, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)
 
plus = Button(ws, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)
 
minus = Button(ws, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)
 
multiply = Button(ws, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
 
divide = Button(ws, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
 
equal = Button(ws, text=' = ', fg='black', bg='red',
                command=equals, height=1, width=7)
equal.grid(row=5, column=2)
 
clear = Button(ws, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
clear.grid(row=5, column='1')
 
Decimal= Button(ws, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)

ws.mainloop()