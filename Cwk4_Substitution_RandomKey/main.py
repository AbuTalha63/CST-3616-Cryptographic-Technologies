# Single substitution - random key

# import packages
import string
import random

# create a string that contains all characters: letters, digits, punctuations, and space bar
allchars = string.ascii_letters + string.digits + string.punctuation + " "

print(f'All characters : {allchars}')
#output: All characters : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# turn the string into a list (array) of characters

allchars = list(allchars)
print(f'All characters in array: {allchars}')
#output: All characters in array : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
# 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
# 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
# '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
# '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

# key is randomly created
# lets make a copy of allchars and call it key

key = allchars.copy()

# now we shuffle the key
random.shuffle(key)
print(f'Key:                     {key}')
#output: Key : ['c', 'C', '7', '8', 'X', 'U', '#', "'", 'P', '`', ')', 'D', 'N', 'Q', 'w', 'q', '^', 's', ' ', '!', 'i',
# ',', 'z', 'k', '{', 'R', '[', '<', '2', 'r', 'Y', 'I', 'h', 'l', '|', 'p', '}', '9', 'L', 'e', ':', ']', '_', '4',
# '1', '&', '5', '3', 'O', 'u', 'j', 'A', 'b', '/', 'K', 'T', 'B', 'J', 'G', 'a', '"', 'S', '-', '=', '~', 't', '.',
# 'v', '?', 'E', ';', 'V', '*', 'o', '6', '(', '\\', 'Z', '0', 'y', '+', 'n', 'W', '@', 'd', 'H', 'g', '%', 'm', 'f',
# 'F', '$', 'M', '>', 'x']

# get some plain text form the user
plaintext = input("Enter in your message: ")
# print(f'Plaintext : {plaintext}')

'''Output
Enter in your message: Hello!
Plaintext : Hello!
'''

ciphertext = ''

# The encryption process consists of replacing every letter in the plain text with the corresponding character

for letter in plaintext:
    index = allchars.index(letter)
    ciphertext += key[index]

print(f'Plaintext:  {plaintext} \nCiphertext :{ciphertext}')

