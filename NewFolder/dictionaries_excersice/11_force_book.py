forced_book = {}
command = input()
while command != 'Lumpawaroo':
    if "|" in command:
        force_side, force_user = command.split(" | ")
        forced_user_in_forced_side = False
        for list_of_force_users in forced_book.values():
            if force_user in list_of_force_users:
                forced_user_in_forced_side = True
                break
        if not forced_user_in_forced_side:
            if force_side not in forced_book.keys():
                forced_book[force_side] = []
            forced_book[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for list_of_force_users in forced_book.values():
            if force_user in list_of_force_users:
                list_of_force_users.remove(force_user)
                break
        if force_side not in forced_book.keys():
            forced_book[force_side] = []
        forced_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in forced_book.items():
    if force_users:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")
