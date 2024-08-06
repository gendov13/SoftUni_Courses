statistic_dic = {}

while True:
    command = input()
    if command == "statistics":
        break
    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key in statistic_dic:
        statistic_dic[key] += value
    else:
        statistic_dic[key] = value

print(f'Products in stock:')
for key,value in statistic_dic.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(statistic_dic)}")
print(f"Total Quantity: {sum(statistic_dic.values())}")
