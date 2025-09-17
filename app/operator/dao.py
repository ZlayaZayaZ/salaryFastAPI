from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.operator.models import Employee
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload


class EmployeeDAO (BaseDAO):
    model = Employee

    @classmethod
    async def find_full_data(cls, employee_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о работнике
            query_employee = select(cls.model).filter_by(id=employee_id)
            result_employee = await session.execute(query_employee)
            employee_info = result_employee.scalar_one_or_none()

            # Если работник не найден, возвращаем None
            if not employee_info:
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
            return employee_info
