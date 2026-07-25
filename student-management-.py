students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        branch = input("Enter branch: ")

        student = {
            "name": name,
            "age": age,
            "branch": branch
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Branch:", student["branch"])
                print()

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for student in students:
            if student["name"] == search_name:
                print("Student Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Branch:", student["branch"])
                found = True

        if found == False:
            print("Student Not Found!")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        found = False

        for student in students:
            if student["name"] == delete_name:
                students.remove(student)
                print("Student Deleted!")
                found = True
                break

        if found == False:
            print("Student Not Found!")

    elif choice == "5":
        print("Program Ended!")
        break