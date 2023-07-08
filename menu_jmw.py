"""The menu module with only the menu function"""

import sys

def menu(*user_options):
    while user_selection := input(f'Please make a selection, your options are {user_options}')

        if user_selection in user_options:
            print("You've made a great selection.")
            return user_selection 
        else:
            print(f"The selection of {user_selection} was not in the available options of {user_options}.")
            print("Please try again.")


if __name__ == "__main__":
    menu(*sys.argv[1:])