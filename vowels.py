all_vowels = 'aeiou'

def count_vowels(filename):
    output = dict.fromkeys(all_vowels, 0)

    for one_line in open(filename):
        for one_character in one_line:
            if one_character in all_vowels:
                output[one_character] += 1

    return output