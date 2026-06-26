from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students")
def create_student(
        student: schemas.StudentCreate,
        db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students/{student_id}")
def get_student(
        student_id: int,
        db: Session = Depends(get_db)):
    return crud.get_student(db)

    if not student:
        raise HTTPExpception(
            status_code=404,
            detail="Student not found"
        )
    
    return student

@app.put("/students/{student_id}")
def update_student(
        student_id: int,
        updated_student: schemas.StudentCreate,
        db: Session = Depends(get_db)):
    
    student = crud.update_student(
        db, 
        student_id,
        updated_student
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    
    return student

@app.delete("/students/{student_id}")
def delete_student(
        student_id: int,
        db: Session = Depends(get_db)):
    
    student = crud.delete_student(
        db, 
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    
    return {"message": "Student deleted successfully"}