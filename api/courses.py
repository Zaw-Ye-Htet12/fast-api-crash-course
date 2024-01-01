import fastapi
from fastapi import Depends, HTTPException

from typing import List

from api.utils.course import get_course, get_courses, create_course
from db.db_setup import get_db
from pydantic_schemas.course import Course, CourseCreate
from sqlalchemy.orm import Session

router = fastapi.APIRouter()

@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    return get_courses(db=db)

@router.post("/courses", status_code=201, response_model=Course)
async def create_course_api(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)

@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=400, detail="Course Not Found")
    return db_course

@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}

@router.delete("/courses/{id}")
async def delete_course():
    return {"course": []}