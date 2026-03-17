from fastapi import APIRouter
from querys import Querys
from logger import log_event

router = APIRouter()
querys = Querys()

@router.get("/employees/engineering/high-salary")
def engineering_high_salary_employees():
    log_event("INFO", "API Request: GET /employees/engineering/high-salary")
    return querys.query_1()

@router.get("/employees/by-age-and-role")
def employees_by_age_and_role(age: int, role: str):
    log_event("INFO", f"API Request: GET /employees/by-age-and-role | Parameters: age={age}, role={role}")
    return querys.query_2(age, role)

@router.get("/employees/top-seniority")
def top_seniority_employees_excluding_hr():
    log_event("INFO", "API Request: GET /employees/top-seniority")
    return querys.query_3()