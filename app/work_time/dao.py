from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.work_time.models import Work, Break
from app.operator.models import Employee


class WorkDAO (BaseDAO):
    model = Work

    @classmethod
    async def find_full_data(cls, operator_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о рабочих сменах работника
            query_work = select(cls.model).filter_by(operator_id=operator_id)
            result_work = await session.execute(query_work)
            work_info = result_work.scalars.all()

            # Если рабочие смены у работника не найдены, возвращаем None
            if not work_info:
                return None

            # Второй запрос для получения информации о работнике
            query_operator = select(Employee).filter_by(id=work_info.operator_id)
            result_operator = await session.execute(query_operator)
            operator_info = result_operator.scalar_one()

            work_data = work_info.to_dict()
            # statistic_data['operator'] = operator_info.name
            work_data['operator'] = f"{operator_info.surname} {operator_info.name}"

            return work_data


class BreakDAO (BaseDAO):
    model = Break

    @classmethod
    async def find_full_data(cls, operator_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о перерывах работника
            query_break = select(cls.model).filter_by(operator_id=operator_id)
            result_break = await session.execute(query_break)
            break_info = result_break.scalars.all()

            # Если работник не найден, возвращаем None
            if not break_info:
                return None

            # Второй запрос для получения информации о работнике
            query_operator = select(Employee).filter_by(id=break_info.operator_id)
            result_operator = await session.execute(query_operator)
            operator_info = result_operator.scalar_one()

            break_data = break_info.to_dict()
            # statistic_data['operator'] = operator_info.name
            break_data['operator'] = f"{operator_info.surname} {operator_info.name}"

            return break_data
