students = []

def add_student():
   student_id = int(input("Enter ID: "))
   name = input("Enter Name: ")
   course = input("Enter Course: ")

   student = {
      "id": student_id,
      "name": name,
      "course": course
   }

   students.append(student)
   print("Student added successfully")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student)

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully")
            return

    print("Student not found")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
       add_student()
        
    elif choice == "2":
       view_students()
       
    elif choice == "3":
       delete_student()

    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
    	print("Invalid choice. Please try again.")
