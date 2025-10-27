from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    student_id: str
    name: str
    age: int
    grade: int
