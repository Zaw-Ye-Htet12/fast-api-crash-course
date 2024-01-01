import fastapi
from fastapi import Depends, HTTPException

from typing import List

from api.utils.users import get_user, get_user_by_email, get_users, create_user
from api.utils.course import get_user_courses
from db.db_setup import get_db
from pydantic_schemas.user import User, UserCreate
from pydantic_schemas.course import Course
from sqlalchemy.orm import Session

router = fastapi.APIRouter()


@router.get('/users', response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post('/users', status_code=201, response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user(db, user)

@router.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User Not Found")
    return db_user

@router.get('/users/{user_id}/courses', response_model=List[Course])
async def get_user_courses_api(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id, db=db)
    if not courses:
        raise HTTPException(status_code=404, detail=f"There's no course which is associated with user_id {user_id}")
    return courses