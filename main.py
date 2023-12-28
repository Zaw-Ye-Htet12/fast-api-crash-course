from fastapi import FastAPI, Path, Query
from typing import Optional, List
from pydantic import BaseModel
from api import courses, sections, users

app = FastAPI(
    title="FastApi Crash Course",
    description="Study-case for learning crash course",
    version="0.0.1",
    contact={
        "name": "Simon",
        "email": "scottsimon4969@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
