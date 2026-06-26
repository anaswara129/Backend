from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate

def create_student(db: Session, student: StudentCreate):
    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_student(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(
        Student.id == student_id
    ).first()

def update_student(
        db: Session,
        student_id: int,
        student: StudentCreate):
    existing = get_student(db, student_id)
    if existing:
        existing.name = student.name
        existing.age = student.age
        existing.course = student.course
        db.commit()
        db.refresh(existing)
    return existing

def delete_student(
        db: Session, 
        student_id: int):
    student = get_student(db, student_id)
    if student:
        db.delete(student)
        db.commit()
    return student