user_points_dictionary = {}
course_dictionary = {}
while True:
    command = input().split("-")
    if len(command) == 1:
        break
    elif len(command) == 2:
        username = command[0]
        del user_points_dictionary[username]
    elif len(command) == 3:
        name, language, points = command[0], command[1], int(command[2])
        if name not in user_points_dictionary:
            user_points_dictionary[name] = 0
        if user_points_dictionary[name] < points:
            user_points_dictionary[name] = points
        if language not in course_dictionary:
            course_dictionary[language] = 0
        course_dictionary[language] += 1
print(f"Results:")
for username, points in user_points_dictionary.items():
    print(f"{username} | {points}")
print(f"Submissions:")
for language, submissions_count in course_dictionary.items():
    print(f"{language} - {submissions_count}")

