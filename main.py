from functions import *

calcfunctions.method()

running = True

while(running):
    option = None
    print_menu()
    option = int(input("Enter your selection: "))
    print(f'You have selected option #{option}')
    if option == 0:
        running = False
    else:
        option = option_select(option)  