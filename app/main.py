from fastapi import FastAPI
from app.operator.router import router as router_employees


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


app.include_router(router_employees)
