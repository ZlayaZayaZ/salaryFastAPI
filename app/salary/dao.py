from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.salary.models import Salary
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload


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

            # # Второй запрос для получения информации о специальности
            # query_major = select(Major).filter_by(id=student_info.major_id)
            # result_major = await session.execute(query_major)
            # major_info = result_major.scalar_one()
            #
            # student_data = student_info.to_dict()
            # student_data['major'] = major_info.major_name
            #
            # return student_data
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

