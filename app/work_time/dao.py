from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.work_time.models import Work, Break


class WorkDAO (BaseDAO):
    model = Work

    @classmethod
    async def find_full_data(cls, operator_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о рабочих сменах работника
            query_work = select(cls.model).filter_by(id=operator_id)
            result_work = await session.execute(query_work)
            work_info = result_work.scalar_one_or_none()

            # Если рабочие смены у работника не найдены, возвращаем None
            if not work_info:
                return None

            return work_info


class BreakDAO (BaseDAO):
    model = Break

    @classmethod
    async def find_full_data(cls, operator_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о перерывах работника
            query_break = select(cls.model).filter_by(id=operator_id)
            result_break = await session.execute(query_break)
            break_info = result_break.scalar_one_or_none()

            # Если работник не найден, возвращаем None
            if not break_info:
                return None

            return break_info
