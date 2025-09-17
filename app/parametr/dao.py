from app.dao.base import BaseDAO
from app.database import async_session_maker
from sqlalchemy.future import select
from app.parametr.models import Parameter
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload


class ParameterDAO (BaseDAO):
    model = Parameter

    @classmethod
    async def find_full_data(cls, parameter_id: int):
        async with async_session_maker() as session:
            # запрос для получения информации о параметре
            query_parameter = select(cls.model).filter_by(id=parameter_id)
            result_parameter = await session.execute(query_parameter)
            parameter_info = result_parameter.scalar_one_or_none()

            # Если параметр не найден, возвращаем None
            if not parameter_info:
                return None

            return parameter_info

