# Frequency Analysis

ciphertext = (
    'GBSVFNBSVFXBSPMBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJZWB'
    'SZWBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJZWBSZWBSVFNBSVF'
    'JZWBSVFNBSVFJZWBSVFNBSVFJZWBSZWBSVFNBSVFJZWBSVFNBSVF'
    'JZWBSVFNBSVFJZWBSZWBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVF'
)
# if you place 2 or more string next to each other in python inside parethsesis
# python automatically glues them toghether into a single string

print(f'ciphertext: {ciphertext}')

# output: ciphertext: GBSVFNBSVFXBSPMBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJ
# ZWBSZWBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJZWBSZWBSVFNBSVFJZWBSVFNBSVFJZ
# WBSVFNBSVFJZWBSZWBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJZWBSZWBSVFNBSVFJZW
# BSVFNBSVFJZWBSVFNBSVF

print(f'ciphertext type: {type(ciphertext)}')

# lets use the counter function (from the lib) to count the number of times
# each letter appears in the cipher text

from collections import Counter
ciphertext_letter_count = Counter(ciphertext)

# Note: Counter function automatically sorts by highest frequency

print(f'ciphertext letter count: {ciphertext_letter_count}')
# output: ciphertext letter count: Counter({'B': 37, 'S': 37, 'V': 32, 'F': 32, 'Z': 18,
# 'W': 18, 'N': 16, 'J': 14, 'G': 1, 'X': 1, 'P': 1, 'M': 1})

# the top letter in appearance
print(f'the most frequent letter is: {ciphertext_letter_count.most_common(1)[0][0]}')

# now lets make a bar chart to show this

categories = list(ciphertext_letter_count.keys())

import matplotlib.pyplot as plt

# add labels as title
plt.xlabel('Ciphertext')
plt.ylabel('Frequency')

# display the chart
plt.show()

# now we calculate the letters' frequencies
ciphertext_length = len(ciphertext)
print(f'ciphertext length: {ciphertext_length}')
# Ouput: ciphertext length: 208

for letter in ciphertext_letter_count.keys():
    percentage = (ciphertext_letter_count[letter] / ciphertext_length) * 100
    print(f'{letter}: {percentage}%')


'''
For decryption shift backwards
our table of letters substitution becomes
B(37)/S(37) -> E
B -> E shift of 23
S -> E shift of 14
V(32)/F(32) -> T shift of 2

'''