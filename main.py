from student_repo import StudentRepository
from student_service import StudentService

def print_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

def main():
    repo = StudentRepository()
    repo.create_table()
    service = StudentService(repo)

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
                student_id = input("Enter student id: ").strip()
                name = input("Enter name: ").strip()
                age = int(input("Enter age (>15): ").strip())
                grade = int(input("Enter grade (>70): ").strip())
                service.add_student(student_id, name, age, grade)
                print("Student added successfully.\n")
            except Exception as e:
                print(f"Error: {e}\n")
        elif choice == "2":
            students = service.get_students()
            if not students:
                print("No students found.\n")
            else:
                print(f"{'ID':<10} {'Name':<20} {'Age':>5} {'Grade':>7}")
                print("-" * 46)
                for s in students:
                    print(f"{s.student_id:<10} {s.name:<20} {s.age:>5} {s.grade:>7}")
                print()
        elif choice == "3":
            sid = input("Enter student id to delete: ").strip()
            removed = service.delete_student(sid)
            if removed:
                print("Student deleted.\n")
            else:
                print("Student id not found.\n")
        elif choice == "4":
            print("Goodbye!")
            try:
                repo.close()
            finally:
                break
        else:
            print("Invalid choice. Please select 1-4.\n")

if __name__ == "__main__":
    main()
