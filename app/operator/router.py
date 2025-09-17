from fastapi import APIRouter, Depends
# from sqlalchemy import select
# from app.database import async_session_maker
# from app.operator.models import Employee
from app.operator.dao import EmployeeDAO
from app.operator.schemas import SEmployee
from app.operator.rb import RBEmployee

router = APIRouter(prefix='/employee', tags=['Работа с сотрудниками'])


# @router.get("/", summary="Получить всех сотрудников")
# async def get_all_employees():
#     async with async_session_maker() as session:
#         query = select(Employee)
#         result = await session.execute(query)
#         employee = result.scalars().all()
#         return employee

@router.get("/", summary="Получить всех работников", response_model=list[SEmployee])
async def get_all_employees(request_body: RBEmployee = Depends()) -> list[SEmployee]:
    return await EmployeeDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить одного работника по id")
async def get_employee_by_id(employee_id: int) -> SEmployee | dict:
    rez = await EmployeeDAO.find_full_data(employee_id)
    if rez is None:
        return {'message': f'Работник с ID {employee_id} не найден!'}
    return rez


