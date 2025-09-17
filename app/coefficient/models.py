from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Enum, Float
from app.database import Base, int_pk
from enum import Enum as PyEnum
from app.statistic.models import StatisticParameter


# Перечисление для типа коэффициента
class CoefficientType(PyEnum):
    POSITIVE = "positive"  # Положительный коэффициент
    NEGATIVE = "negative"  # Негативный коэффициент


# модель таблицы коэффициентов
class Coefficient(Base):

    id: Mapped[int_pk]
    parameter: Mapped[StatisticParameter] = mapped_column(
        Enum(StatisticParameter, name="statistic_parameter_enum"),
        nullable=False,
        unique=True
    )
    norm: Mapped[int] = mapped_column(Integer, nullable=False)
    base: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.25,
        comment="Вес коэффициента в границах от 0 до 1"
    )
    coefficient_type: Mapped[CoefficientType] = mapped_column(
        Enum(CoefficientType, name="coefficient_type_enum"),
        nullable=False,
        comment="Тип коэффициента: положительный или негативный"
    )

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"parameter={self.parameter.value}, "
                f"type={self.coefficient_type.value})")

    def __repr__(self):
        return str(self)

