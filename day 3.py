# Takes a secret word as input(without space).
# Then encodes the word using a custom cipher:
# Replace all vowels with +
# Reverse the entire string
# Then shift each letter 2 places ahead in the alphabet (wrap around if needed, e.g., y -> a , z-> b)
# Finally, print the resulting encoded word.

def encode_word(word):
    vowels = "aeiouAEIOU"

    new_word = ""
    for letter in word:
        if letter in vowels:
            new_word += "+"
        else:
            new_word += letter

    reversed_word = new_word[::-1]

    encoded = ""
    for letter in reversed_word:
        if letter.isalpha():
            if letter.islower():

                shifted = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
            else:

                shifted = chr((ord(letter) - ord('A') + 2) % 26 + ord('A'))
            encoded += shifted
        else:

            encoded += letter

    print(encoded)


secret_word = input("Enter the secret word (no spaces): ")
encode_word(secret_word)
