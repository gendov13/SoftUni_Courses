all_shards = {'shards': 0, 'fragments': 0, 'motes': 0}
won_legendary_item = False
while not won_legendary_item:
    fragments = input().split()
    for index in range(0, len(fragments), 2):
        quantity = int(fragments[index])
        material = fragments[index + 1].lower()
        if material not in all_shards.keys():
            all_shards[material] = 0
        all_shards[material] += quantity
        if all_shards['shards'] >= 250:
            all_shards['shards'] -= 250
            print("Shadowmourne obtained!")
            won_legendary_item = True
        elif all_shards['fragments'] >= 250:
            all_shards['fragments'] -= 250
            print("Valanyr obtained!")
            won_legendary_item = True
        elif all_shards['motes'] >= 250:
            all_shards['motes'] -= 250
            print("Dragonmwrath obtained!")
            won_legendary_item = True
        if won_legendary_item:
            break

for material,quantity in all_shards.items():
    print(f"{material}: {quantity}")








