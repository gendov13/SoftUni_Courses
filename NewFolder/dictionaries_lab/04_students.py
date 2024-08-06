all_students = {}
while True:
    students = input()
    if ":" not in students:
        break
    info = students.split(":")
    name = info[0]
    ID = info[1]
    course = info[2]
    if course not in all_students:
        all_students[course] = {}
    all_students[course][name] = ID
current_course = students.split("_")
for current_key in all_students.keys():
    if current_course[0] in current_key:
        for name, ID in all_students[current_key].items():
            print(f"{name} - {ID}")


