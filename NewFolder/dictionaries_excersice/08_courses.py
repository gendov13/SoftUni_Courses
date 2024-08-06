command = input()
register = {}
while command != "end":
    course_name, student = command.split(' : ')
    if course_name not in register:
        register[course_name] = []
    register[course_name].append(student)
    command = input()

for key,values in register.items():
    print(f"{key}: {len(values)}")
    for value in values:
        print(f"-- {value}")


