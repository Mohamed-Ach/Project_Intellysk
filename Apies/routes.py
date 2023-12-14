from fastapi import APIRouter
from typing import List, Dict
import schema

router = APIRouter(
    prefix="/api/v1",
    tags=["students"]
)


@router.get("/students", response_model=List[Dict[str, str]])
async def get_etudiants():
    return schema.student_list

@router.get("/students/gender",response_model=Dict[str, int])
async def bar_gender():
    return schema.students_gender

@router.get("/students/internet_use",response_model=Dict[str, int])
async def using_internet():
    return schema.students_internet

@router.get("/students/absence",response_model=List[Dict[int, int]])
async def effects_absence():
    return schema.students_absence


@router.get("/students/cigarette_use",response_model=List[Dict[int, int]])
async def effects_cigarette():
    return schema.daily_cigarettes


@router.get("/students/romantics",response_model=Dict[str, int])
async def en_realtion():
    return schema.students_romantics