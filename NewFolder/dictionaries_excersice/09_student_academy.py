numbers = int(input())
students_academy = {}
for number in range(numbers):
    students_name = input()
    grade = float(input())
    if students_name not in students_academy:
        students_academy[students_name] = []
    students_academy[students_name].append(grade)

for students_name, grade in students_academy.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{students_name} -> {average_grade:.2f}")
