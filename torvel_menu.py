import sys

def menu(*args):
    """
    Function that presents a menu to the user with the options passed as arguments.
    If the user's choice matches one of the options, it is returned.
    If not, the user is prompted again.
    """
    while True:
        print("\nPlease choose one of the following options:")
        for i, option in enumerate(args, start=1):
            print(f"{i}. {option}")

        user_choice = input("\nEnter your choice: ")

        if user_choice in args:
            return user_choice
        else:
            print(f"Invalid option '{user_choice}'. Please try again.")


if __name__ == "__main__":
    choices = sys.argv[1:]
    if choices:
        choice = menu(*choices)
        print(f"You chose '{choice}'.")
    else:
        print("No options provided. Please run the script with some options.")
