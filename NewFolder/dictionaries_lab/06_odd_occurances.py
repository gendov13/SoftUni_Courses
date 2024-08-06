words = input().lower().split()
current_words = {}
for word in words:
    if word not in current_words:
        current_words[word] = 0
    current_words[word] += 1
odd_words = []
for key, value in current_words.items():
    if value % 2 == 1:
        odd_words.append(key)
print(" ".join(odd_words))


