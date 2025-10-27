# student_service.py - Business Logic (Service) Layer
from typing import List
from student import Student
from student_repo import StudentRepository

class StudentService:
    def __init__(self, repo: StudentRepository) -> None:
        self.repo = repo

    def add_student(self, student_id: str, name: str, age: int, grade: int) -> None:
        # validations as specified
        if int(age) <= 15:
            raise ValueError("Age must be greater than 15")
        if int(grade) <= 70:
            raise ValueError("Grade must be greater than 70")
        if not student_id.strip():
            raise ValueError("student_id cannot be empty")
        if not name.strip():
            raise ValueError("name cannot be empty")

        s = Student(student_id=student_id.strip(), name=name.strip(), age=int(age), grade=int(grade))
        self.repo.add_student(s)

    def get_students(self) -> List[Student]:
        return self.repo.get_students()

    def delete_student(self, student_id: str) -> bool:
        return self.repo.delete_student(student_id.strip())
