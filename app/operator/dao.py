from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.operator.models import Employee


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

            return employee_info
