from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

students = [
    {"id": 1, "name": "Anu", "age": 20, "course": "Python"},
    {"id": 2, "name": "Rahul", "age": 21, "course": "Java"}
]

@app.get("/")
def home():
    return {"message": "Student API is running"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "Student not found"}

@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }