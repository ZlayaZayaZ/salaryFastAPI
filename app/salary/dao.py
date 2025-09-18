from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.salary.models import Salary


class SalaryDAO (BaseDAO):
    model = Salary

    @classmethod
    async def find_full_data(cls, salary_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о работнике
            query_salary = select(cls.model).filter_by(id=salary_id)
            result_salary = await session.execute(query_salary)
            salary_info = result_salary.scalar_one_or_none()

            # Если работник не найден, возвращаем None
            if not salary_info:
                return None

            return salary_info

    @classmethod
    async def find_filter_data(cls, operator_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о зарплате конкретного работника
            query_salary = select(cls.model).filter_by(operator_id=operator_id)
            result_salary = await session.execute(query_salary)
            salary_info = result_salary.scalars.all()

            # Если информация не найдена, возвращаем None
            if not salary_info:
                return None

            return salary_info

