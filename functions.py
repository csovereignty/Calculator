import calcfunctions

object = calcfunctions.arithmetic()

def print_menu():
    for key in menu_options.keys():
        print(key, " | ", menu_options[key])

menu_options = {
    1: 'Addition',
    2: 'Subtraction',
    3: 'WIP',
    0: 'Quit',
}

def option_select(user_selection):
    if user_selection == 1:
        val1 = int(input("Enter 1st value: "))
        val2 = int(input("Enter 2nd value: "))
        # printing noob way
        print(val1, "+", val2, "=", + object.add(val1, val2))
    if user_selection == 2:
        val1 = int(input("Enter 1st value: "))
        val2 = int(input("Enter 2nd value: "))
        # printing f-string way
        print(f'{val1} + {val2} = {object.sub(val1, val2)}')
    else:
        quit()