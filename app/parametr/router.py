from fastapi import APIRouter, Depends

from app.parametr.dao import ParameterDAO
from app.parametr.schemas import SParameter
from app.parametr.rb import RBParameter

router = APIRouter(prefix='/parameter', tags=['Работа с параметрами'])


@router.get("/", summary="Получить всех работников", response_model=list[SParameter])
async def get_all_parameters(request_body: RBParameter = Depends()) -> list[SParameter]:
    return await ParameterDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить одного работника по id")
async def get_employee_by_id(parameter_id: int) -> SParameter | dict:
    rez = await ParameterDAO.find_full_data(parameter_id)
    if rez is None:
        return {'message': f'Работник с ID {parameter_id} не найден!'}
    return rez

