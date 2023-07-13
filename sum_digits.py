# here, I'm going to define a function that takes a string, finds
# all of the digits in the string, and returns their sum.  It ignores
# any non-digits in the string

import digit_funcs

user_string = input('Enter a string containing some digits: ').strip()
print(digit_funcs.sum_digits(user_string))

# attributes are names that come after dots (.)

# here, sum_digits is an attribute of digit_funcs,
# which is a global variable referring to a module

# in this file:
# globals: digit_funcs, user_string
# locals: none, because we don't define a function