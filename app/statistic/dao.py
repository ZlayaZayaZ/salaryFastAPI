from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.statistic.models import Statistic
from app.parametr.models import Parameter
from app.operator.models import Employee
from app.work_time.models import Work


class StatisticDAO (BaseDAO):
    model = Statistic

    @classmethod
    async def find_full_data(cls, statistic_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о статистике
            query_statistic = select(cls.model).filter_by(id=statistic_id)
            result_statistic = await session.execute(query_statistic)
            statistic_info = result_statistic.scalar_one_or_none()

            # Если запись в таблице не найдена, возвращаем None
            if not statistic_info:
                return None

            # Второй запрос для получения информации о параметре
            query_parameter = select(Parameter).filter_by(id=statistic_info.parameter_id)
            result_parameter = await session.execute(query_parameter)
            parameter_info = result_parameter.scalar_one()

            statistic_data = statistic_info.to_dict()
            statistic_data['parameter'] = parameter_info.name

            # Третий запрос для получения информации о работнике
            query_operator = select(Employee).filter_by(id=statistic_info.operator_id)
            result_operator = await session.execute(query_operator)
            operator_info = result_operator.scalar_one()

            # statistic_data['operator'] = operator_info.name
            statistic_data['operator'] = f"{operator_info.surname} {operator_info.name}"

            # Четвертый запрос для получения информации о смене
            query_work = select(Work).filter_by(id=statistic_info.work_id)
            result_work = await session.execute(query_work)
            work_info = result_work.scalar_one()

            statistic_data['work'] = f"{work_info.start_date}-{work_info.end_date}"

            return statistic_data

    @classmethod
    async def find_filter_data(cls, param: str, value: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о статистике
            query_statistic = select(cls.model).filter_by(param=value)
            result_statistic = await session.execute(query_statistic)
            statistic_all_info = result_statistic.scalars.all()

            # Если запись в таблице не найдена, возвращаем None
            if not statistic_all_info:
                return None

            return statistic_all_info
