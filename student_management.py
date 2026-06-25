students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        course = input("Enter Course: ")

        student = {
            "name": name,
            "roll": roll,
            "course": course
        }

        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Records Found!")
        else:
            for s in students:
                print("\nName :", s["name"])
                print("Roll :", s["roll"])
                print("Course :", s["course"])

    elif choice == "3":
        search_name = input("Enter Student Name to Search: ")

        found = False

        for s in students:
            if s["name"] == search_name:
                print("\nStudent Found")
                print("Name :", s["name"])
                print("Roll :", s["roll"])
                print("Course :", s["course"])
                found = True

        if not found:
            print("Student Not Found!")

    elif choice == "4":
        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for s in students:
            if s["name"] == delete_name:
                students.remove(s)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")