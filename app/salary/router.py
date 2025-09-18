from fastapi import APIRouter, Depends
from app.salary.dao import SalaryDAO
from app.salary.schemas import SSalary
from app.salary.rb import RBSalary

router = APIRouter(prefix='/salary', tags=['Зарплата сотрудников'])


@router.get("/", summary="Получить данные всех зарплат", response_model=list[SSalary])
async def get_all_employees(request_body: RBSalary = Depends()) -> list[SSalary]:
    return await SalaryDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить данные по зарплате одного работника по id")
async def get_employee_by_id(salary_id: int) -> SSalary | dict:
    rez = await SalaryDAO.find_full_data(salary_id)
    if rez is None:
        return {'message': f'Данные о зарплате с ID={salary_id} не найдены!'}
    return rez


@router.get("/operator/{id}", summary="Получить данные по зарплате одного работника")
async def get_operator_by_id(operator_id: int) -> SSalary | dict:
    rez = await SalaryDAO.find_filter_data(operator_id)
    if rez is None:
        return {'message': f'Данные о зарплате по работнику с ID={operator_id} не найдены!'}
    return rez
