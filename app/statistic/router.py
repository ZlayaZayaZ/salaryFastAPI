from fastapi import APIRouter, Depends
from app.statistic.dao import StatisticDAO
from app.statistic.schemas import SStatistic
from app.statistic.rb import RBStatistic

router = APIRouter(prefix='/statistic', tags=['Статистика'])


@router.get("/", summary="Получить все записи статистики", response_model=list[SStatistic])
async def get_all_statistic(request_body: RBStatistic = Depends()) -> list[SStatistic]:
    return await StatisticDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить одну запись по id")
async def get_statistic_by_id(statistic_id: int) -> SStatistic | dict:
    rez = await StatisticDAO.find_full_data(statistic_id)
    if rez is None:
        return {'message': f'Запись с ID={statistic_id} не найдена!'}
    return rez


@router.get("/operator/{id}", summary="Получить статистику по одному работнику по его id")
async def get_operator_by_id(operator_id: int) -> SStatistic | dict:
    rez = await StatisticDAO.find_filter_data('operator_id', operator_id)
    if rez is None:
        return {'message': f'Статистика по работнику с ID={operator_id} не найдена'}
    return rez


@router.get("/work/{id}", summary="Получить статистику по смене")
async def get_work_by_id(work_id: int) -> SStatistic | dict:
    rez = await StatisticDAO.find_filter_data('work', work_id)
    if rez is None:
        return {'message': f'Статистика по смене с ID={work_id} не найдена!'}
    return rez


@router.get("/parameter/{id}", summary="Получить статистику по id параметра")
async def get_parameter_by_id(parameter_id: int) -> SStatistic | dict:
    rez = await StatisticDAO.find_filter_data(parameter_id)
    if rez is None:
        return {'message': f'Статистика по параметру с ID={parameter_id} не найдена!'}
    return rez



