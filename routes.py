from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import predict as _model
import schema


router = APIRouter(
    prefix="/api/v1",
    tags=["students"]
)


# ** Initializing The Data:
student_list = schema.read_csv("csv/students.csv")
prediction_list = _model.predict_all_students()
students_list = schema.merge_data_model(student_list, prediction_list)


@router.get("/students/all", response_model=List[Dict[str, str | int | float]])
async def get_students():
    return students_list


@router.post("/students/single", response_model=Dict[str, Any])
async def get_students(apogee: int, student_data: Dict[str, Any]):
    if apogee is None:
        raise HTTPException(
            status_code=400, detail="Apogee number is required")

    return {"Numero Apogee": apogee, "Expected Mark": _model.predict_single_student(apogee, student_data)}


@router.get("/students/gender", response_model=Dict[str, int])
async def bar_gender():
    return schema.get_students_gender(students_list)


@router.get("/students/internet_use", response_model=Dict[str, int])
async def using_internet():
    return schema.get_students_internet(students_list)


@router.get("/students/absence", response_model=List[Dict[int, int]])
async def effects_absence():
    return schema.get_students_absence(students_list)


@router.get("/students/cigarette_use", response_model=List[Dict[int, int]])
async def effects_cigarette():
    return schema.get_daily_cigarettes(students_list)


@router.get("/students/romantics", response_model=Dict[str, int])
async def in_relationship():
    return schema.get_students_romantics(students_list)
