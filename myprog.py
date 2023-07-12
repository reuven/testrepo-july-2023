# This is a new program
# that will ask the user to enter the name of a file
# and will print the number of occurrences of each vowel
# in the named file.

# However, it won't do this counting itself. Rather, it'll
# call the count_vowels function in a separate module, called vowels.py

from vowels import count_vowels

filename = input('Enter a filename: ').strip()

print(count_vowels(filename))

import string
string.capwords