from fastapi import APIRouter, Depends
from app.work_time.dao import WorkDAO, BreakDAO
from app.work_time.schemas import SWork, SBreak, SWorkAdd, SBreakAdd
from app.work_time.rb import RBWork, RBBreak

router_work = APIRouter(prefix='/work', tags=['Рабочие смены'])
router_break = APIRouter(prefix='/break', tags=['Перерывы'])


@router_work.get("/", summary="Получить все смены", response_model=list[SWork])
async def get_all_works(request_body: RBWork = Depends()) -> list[SWork]:
    return await WorkDAO.find_all(**request_body.to_dict())


@router_work.get("/{operator_id}", summary="Получить смены одного работника по id работника")
async def get_works_by_operator_id(operator_id: int) -> SWork | dict:
    rez = await WorkDAO.find_full_data(operator_id)
    if rez is None:
        return {'message': f'Смены работника с ID={operator_id} не найдены!'}
    return rez


@router_work.post("/add/")
async def register_work(work: SWorkAdd) -> dict:
    check = await WorkDAO.add(**work.dict())
    if check:
        return {"message": "Смена успешно добавлена!", "work": work}
    else:
        return {"message": "Ошибка при добавлении смены!"}


@router_break.get("/", summary="Получить все перерывы", response_model=list[SBreak])
async def get_all_breaks(request_body: RBBreak = Depends()) -> list[SBreak]:
    return await BreakDAO.find_all(**request_body.to_dict())


@router_break.get("/{operator_id}", summary="Получить перерывы одного работника по id работника")
async def get_breaks_by_operator_id(operator_id: int) -> SBreak | dict:
    rez = await BreakDAO.find_full_data(operator_id)
    if rez is None:
        return {'message': f'Перерывы работника с ID={operator_id} не найдены!'}
    return rez


@router_break.post("/add/")
async def register_break(breaks: SBreakAdd) -> dict:
    check = await BreakDAO.add(**breaks.dict())
    if check:
        return {"message": "Перерыв успешно добавлен!", "break": breaks}
    else:
        return {"message": "Ошибка при добавлении перерыва!"}
