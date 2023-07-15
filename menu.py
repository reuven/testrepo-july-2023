def menu(*args):  
    while True:
        user_choice = input("Enter a selection from the menu: ")
        if user_choice not in args:
            continue
        print(f'Your choice is {user_choice}')
        break

