




























































for char in plaintext:
    if char.isalpha():
        #get the index of this letter in the alphabet
        plaintext_letter_index = alphabet.index(char)

        #get the index of the key letter
        key_index = alphabet.index(key[j])

        shifted_index = (plaintext_letter_index + key_index) % alphabet_length
        encrypted_text += alphabet[shifted_index]
        j += 1
    else:
        encrypted_text += char

print(f'Plaintext     : {plaintext}')
print(f'Encrypted text: {encrypted_text}')