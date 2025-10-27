import sqlite3
from typing import List
from student import Student

class StudentRepository:
    def __init__(self, db_path: str = "students.db") -> None:
        self.db_path = db_path
        # Create connection on demand for simplicity
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def create_table(self) -> None:
        self.conn.execute()
        self.conn.commit()

    def add_student(self, student: Student) -> None:
        try:
            self.conn.execute(
                (student.student_id, student.name, student.age, student.grade),
            )
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Student with id '{student.student_id}' already exists") from e

    def get_students(self) -> List[Student]:
        cur = self.conn.execute("SELECT student_id, name, age, grade FROM students ORDER BY student_id")
        rows = cur.fetchall()
        return [Student(r["student_id"], r["name"], int(r["age"]), int(r["grade"])) for r in rows]

    def delete_student(self, student_id: str) -> bool:
        cur = self.conn.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        self.conn.commit()
        return cur.rowcount > 0

    def close(self) -> None:
        try:
            self.conn.close()
        except Exception:
            pass
