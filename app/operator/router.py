from fastapi import APIRouter, Depends
from app.operator.dao import EmployeeDAO
from app.operator.schemas import SEmployee
from app.operator.rb import RBEmployee

router = APIRouter(prefix='/employee', tags=['Работа с сотрудниками'])


@router.get("/", summary="Получить всех работников", response_model=list[SEmployee])
async def get_all_employees(request_body: RBEmployee = Depends()) -> list[SEmployee]:
    return await EmployeeDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить одного работника по id")
async def get_employee_by_id(employee_id: int) -> SEmployee | dict:
    rez = await EmployeeDAO.find_full_data(employee_id)
    if rez is None:
        return {'message': f'Работник с ID={employee_id} не найден!'}
    return rez


