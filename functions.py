import calcfunctions

object = calcfunctions.arithmetic()

def print_menu():
    for key in menu_options.keys():
        print(key, " | ", menu_options[key])

menu_options = {
    1: 'Addition',
    2: 'Subtraction',
    3: 'Multiplication',
    4: 'Division',
    0: 'Quit',
}

def option_select(user_selection):
    if user_selection == 1:
        val1 = int(input("Enter 1st value: "))
        val2 = int(input("Enter 2nd value: "))
        # printing noob way
        print(val1, "+", val2, "=", + object.add(val1, val2))
        return 1
    if user_selection == 2:
        val1 = int(input("Enter 1st value: "))
        val2 = int(input("Enter 2nd value: "))
        # printing f-string way
        print(f'{val1} - {val2} = {object.sub(val1, val2)}')
        return 1
    if user_selection == 3:
        val1 = int(input("Enter 1st value: "))
        val2 = int(input("Enter 2nd value: "))
        # printing f-string way
        print(f'{val1} * {val2} = {object.multiply(val1, val2)}')
        return 1
    if user_selection == 4:
        val1 = int(input("Enter 1st value: "))
        val2 = int(input("Enter 2nd value: "))
        # printing f-string way
        print(f'{val1} / {val2} = {object.divide(val1, val2)}')
        return 1
    else:
        return 0