from fastapi import APIRouter
from querys import Querys
from logger import log_event

router = APIRouter()
querys = Querys()

@router.get("/query_1")
def query_1():
    log_event("INFO", "get query_1")
    return querys.query_1()

@router.get("/query_2")
def query_2():
    log_event("INFO", "get query_2")
    return querys.query_2()

@router.get("/query_3")
def query_3():
    log_event("INFO", "get query_3")
    return querys.query_3()

@router.get("/query_4")
def query_4():
    log_event("INFO", "get query_4")
    return querys.query_4()

@router.get("/query_5")
def query_5():
    log_event("INFO", "get query_5")
    return querys.query_5()

@router.get("/query_6")
def query_6():
    log_event("INFO", "get query_6")
    return querys.query_6()

@router.get("/query_7")
def query_7():
    log_event("INFO", "get query_7")
    return querys.query_7()
