letters = input().split(", ")
new_letter_dictionary = {}
for letter in letters:
    if letter not in new_letter_dictionary:
        new_letter_dictionary[letter] = {}
    new_letter_dictionary[letter] = ord(letter)

print(new_letter_dictionary)
