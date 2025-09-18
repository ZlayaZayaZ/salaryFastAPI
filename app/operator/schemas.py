from pydantic import BaseModel, Field, ConfigDict


class SEmployee(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    surname: str = Field(..., min_length=1, max_length=50, description="Фамилия")
    name: str = Field(..., min_length=1, max_length=50, description="Имя")
    patronymic: str = Field(..., min_length=1, max_length=50, description="Отчество")
    job_title: str = Field(..., min_length=1, max_length=150, description="Должность в фирме")
    status: bool = Field(True, description="работает/уволен")
    salary: int = Field(..., description="Зарплата")


class SEmployeeAdd(BaseModel):
    surname: str = Field(..., min_length=1, max_length=50, description="Фамилия")
    name: str = Field(..., min_length=1, max_length=50, description="Имя")
    patronymic: str = Field(..., min_length=1, max_length=50, description="Отчество")
    job_title: str = Field(..., min_length=1, max_length=150, description="Должность в фирме")
    status: bool = Field(True, description="работает/уволен")
    salary: int = Field(..., description="Зарплата")

