chars = [letter for letter in input() if letter != " "]
new_chars = {}
for char in chars:
    if char not in new_chars:
        new_chars[char] = 0
    new_chars[char] += 1
for key,value in new_chars.items():
    print(f"{key} -> {value}")