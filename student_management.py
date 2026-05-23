students = []

while True:

    print("\n=== Student Management System ===")

    print("1 Add student")
    print("2 Show students")
    print("3 Search student")
    print("4 Delete student")
    print("5 Exit")

    choice = input("Choose option: ")

    if choice == "1":

        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")

        student = {
            "name": name,
            "age": age,
            "grade": grade
        }

        students.append(student)

        print("Student added successfully")

    elif choice == "2":

        if len(students) == 0:
            print("No students found")

        else:
            for student in students:

                print("\nName :", student["name"])
                print("Age :", student["age"])
                print("Grade :", student["grade"])

    elif choice == "3":

        search_name = input("Enter student name to search: ")

        found = False

        for student in students:

            if student["name"] == search_name:

                print("\nStudent found")
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Grade :", student["grade"])

                found = True

        if found == False:
            print("Student not found")

    elif choice == "4":

        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:

            if student["name"] == delete_name:

                students.remove(student)

                print("Student deleted successfully")

                found = True
                break

        if found == False:
            print("Student not found")

    elif choice == "5":

        print("Program closed")
        break

    else:
        print("Invalid choice")
