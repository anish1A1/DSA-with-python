# Write a program to read a character and check whether it is an alphabet, digit or special symbol.

import string

import string

def checkCharacter(charac):
    # Ensuring the input is converted to a string and grabing just the first character
    charac = str(charac)[0]
    
    if charac.isalpha():
        print(f"'{charac}' is an Alphabet")
    elif charac.isdigit():
        print(f"'{charac}' is a Digit")
    elif charac in string.punctuation:
        print(f"'{charac}' is a Special Character")
    else:
        print(f"'{charac}' is an unrecognized symbol")

# Test cases
checkCharacter(24)   # Output: '2' is a Digit
checkCharacter('a')   # Output: 'a' is an Alphabet
checkCharacter('$')   # Output: '$' is a Special Character
