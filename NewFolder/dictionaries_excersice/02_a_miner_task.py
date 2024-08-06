collected_items = {}
while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command  not in collected_items.keys():
        collected_items[command] = 0
    collected_items[command] += quantity
for key, value in collected_items.items():
    print(f"{key} -> {value}