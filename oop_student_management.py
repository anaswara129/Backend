class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        student_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        student = Student(student_id, name, age)
        self.students.append(student)

        print("Student Added Successfully!")
       
       
    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()
            print("-" * 20)
    
    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted!")
                return

        print("Student Not Found!")
     
    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.delete_student()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid Choice")
     
manager = StudentManager()
manager.menu()                                  
