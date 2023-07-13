# here, I'm going to define a function that takes a string, finds
# all of the digits in the string, and returns their sum.  It ignores
# any non-digits in the string

def sum_digits(s):
    total = 0

    for one_character in s:
        if one_character.isdigit():
            total += int(one_character)

    return total

# in this file, sum_digits is a function we've
# defined -- and it is a global variable IN THIS FILE

# in this file:
# globals: sum_digits
# locals: s, total, and one_character

# now, let's add something interactive to this module
# this interactive stuff should only run if we 
# run the module file directly, as a program, *not*
# if it is imported

# if a module file contains both definitions
# (that will be loaded) and actual code that should
# be run (when the module is treated as a program),
# we can distinguish between those two types of running
# with the magic incantation checking __name__ == '__main__'.

# __name__ is a global variable that is always defined.
# It normally contains the string '__main__'.  But when
# we import a module, the imported module sees the value
# as its name (e.g., 'digit_funcs').  That lets us 
# distinguish bewteen importing the module (when 
# the __name__ == '__main__' stuff won't run) and
# running the module as a program (when it will).

# if your module only contains 100% definitions,
# you DO NOT NEED THIS SECTION.  

print(f'Thanks for running me; {__name__=}')

if __name__ == '__main__':
    print('Hello from digit_funcs!')
    print(sum_digits('123abcd'))
