phonebook = {}
while True:
    name = input()
    if "-" not in name:
        break
    name = name.split("-")
    new_name = name[0]
    number = name[1]
    phonebook[new_name] = number

repeating = int(name)
for i in range(repeating):
    phone_name = input()
    if phone_name in phonebook.keys():
        print(f'{phone_name} -> {phonebook[phone_name]}')
    else:
        print(f"Contact {phone_name} does not exist.")