# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    if name in students:
        print("Already registered.")
    else:
        students[name] = {'age': age,
                          'grade': grade,
                          'subjects': subjects}
        print(f"Student {name} added successfully to our platform.")


def update_student(name):
    if name in students:
        print(f"Updating the values for student {name}. If you want to keep the current value press ENTER!")
        age = input(f"Enter new age (current: {students[name]['age']}): ")
        grade = input(f"Enter new grade (current: {students[name]['grade']}): ")
        subjects = input(f"Enter new subjects (current: {', '.join(students[name]['subjects'])}): ")
        if age:
            students[name]['age'] = int(age)
        if grade:
            students[name]['grade'] = float(grade)
        if subjects:
            students[name]['subjects'] = subjects.split(',')
            # Here with the split method we split them as individual ones
        print(f"{name} updated successfully.")
    else:
        print(f"{name} was not found!")


def delete_student(name):
    if name in students:
        del students[name]
        print(f"Student {name} was deleted successfully!")
    else:
        print(f"Student {name} not found.")


def search_student(name):
    if name in students:
        student = students[name]
        print(f"Name: {name}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        print(f"Subjects: {', '.join(student['subjects'])}")


    else:
        print(f"Student {name} not found.")


def list_all_students():
    if students:
        for name, details in students.items():
            # Here we use name, details and students.items()
            # to list the items in the dictionary students,
            # name is the students name and details are all items listed in the dictionary
            print(f"Name: {name}, \
            Age: {details['age']}, \
            Grade: {details['grade']}, \
            Subjects: {', '.join(details['subjects'])}")
    else:
        print("Student was not found.")


def main():
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
