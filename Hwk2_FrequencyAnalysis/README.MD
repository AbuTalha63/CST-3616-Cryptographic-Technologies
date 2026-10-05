HW 2 - CST 3616 - Cryptographic Technologies

Every language has predictable letter frequencies. Frequency analysis is used in cryptanalysis (the art of breaking codes) to decrypt messages locked with classical substitution ciphers by counting how often specific letters or groups of letters appear. If a cipher preserves those frequencies (like Caesar or any monoalphabetic substitution), you can break it by comparing the ciphertext’s frequency distribution to the known distribution of English: E is the most common letter (~12–13%), T, A, O, I, N, S, R follow, and Z, Q, X, J are rare. These patterns persist in large enough texts.

Below is a ciphertext encrypted using a standard monoalphabetic substitution cipher. The original plaintext is in standard English (all punctuation and spaces have been removed to increase difficulty:

GBSVFNBSVFXBSPMBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJZWB

SZWBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVFJZWBSZWBSVFNBSVF

JZWBSVFNBSVFJZWBSVFNBSVFJZWBSZWBSVFNBSVFJZWBSVFNBSVF

JZWBSVFNBSVFJZWBSZWBSVFNBSVFJZWBSVFNBSVFJZWBSVFNBSVF

Write a Python script to calculate the percentage frequencies of all letters in the ciphertext. The script should show a table and a bar chart of the top 5 most frequent characters. Using your statistical data and knowledge of common English words, reconstruct the substitution key and decrypt the ciphertext. Print the final plaintext (with spaces and punctuation added back for readability).

Note: if W is the most frequent letter in the ciphertext and E is the most frequent letter in English text then you can guess that W is being replaced by E. Check for the shift in the index of both letters: W and E and apply this shift for the entire ciphertext to decrypt it.