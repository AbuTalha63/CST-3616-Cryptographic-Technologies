# Hwk1: Monoalphabetic substitution: any letter by the median of the
# next 2 letters of the alphabet

# import module
import string

# create 2 string: uppercase and lowercase letters

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

# print the strings
print(f'Lowercase: {lowercase}')
print(f'Uppercase: {uppercase}')

'''Output
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''

# Create lists (arrays) for these 2 string

lst_lowercase = lowercase
lst_uppercase = uppercase

alphabet_size = len(lst_lowercase)

#create a dictionary for pairs of key:value

# what is the ordinal value of lowercase 'a' | ordinal aka the ASCII value

print(f'ordinal value of lowercase a: {ord(lst_lowercase[0])}')

# output: 97

# the indexes go from 0 to 25
# the map of lowercase is named LCAM
LCAM = {chr(i):i-97 for i in range (97,97+alphabet_size)}
print(f'LCAM: {LCAM}')

#output: LCAM: {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
# 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
# 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
# 'x': 23, 'y': 24, 'z': 25}

# now uppsercase ASCII values, known as UCAM
print('Decinal/ordinal value of A: ', ord('A'))
# Output: Decinal/ordinal value of A:  65

UCAM = {chr(i):(i-65) for i in range (65, 65+alphabet_size)}
print(f'UCAM: {UCAM}')
#Output: UCAM: {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
# 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
# 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
# 'Y': 24, 'Z': 25}

# ask the user for a plain text
plaintext = input('Enter a plaintext: ')
print(f'Plaintext: {plaintext}')
#output: Plaintext: hello

# ----------------- Encryption of Plaintext --------------------- #

for letter in plaintext:
    if letter.isupper():
        if letter in UCAM:
            LCAM[letter] = UCAM[letter]
            new_letter_index = math.ceil((letter_index + 2) / 2)

            #

