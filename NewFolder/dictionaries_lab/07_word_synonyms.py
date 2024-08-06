number_of_repeats = int(input())
word_synonyms = {}
for number in range(0, number_of_repeats):
    word = input()
    synonym = input()
    if word not in word_synonyms:
        word_synonyms[word] = []
    word_synonyms[word].append(synonym)
for key, value in word_synonyms.items():
    print(f"{key} - {', '.join(value)}")


