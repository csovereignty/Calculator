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