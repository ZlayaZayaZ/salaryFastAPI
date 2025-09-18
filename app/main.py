from fastapi import FastAPI
from app.work_time.router import router_work, router_break
from app.parametr.router import router as router_parameter
from app.operator.router import router as router_employees
from app.statistic.router import router as router_statistic

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


app.include_router(router_employees)
app.include_router(router_parameter)
app.include_router(router_work)
app.include_router(router_break)
app.include_router(router_statistic)
