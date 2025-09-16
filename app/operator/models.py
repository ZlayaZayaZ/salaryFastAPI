from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, DateTime, Integer, Enum, Float, Computed
from datetime import datetime
from enum import Enum as PyEnum
from app.database import Base, int_pk


# модель таблицы сотрудников
class Employee(Base):

    id: Mapped[int_pk]
    surname: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(50))
    patronymic: Mapped[str] = mapped_column(String(50))
    job_title: Mapped[str] = mapped_column(String(150))
    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        server_default='true'
    )
    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    # Связи
    work_shifts: Mapped[list["Work"]] = relationship(back_populates="operator")
    breaks: Mapped[list["Break"]] = relationship(back_populates="operator")
    statistics: Mapped[list["Statistic"]] = relationship(back_populates="operator")
    salaries: Mapped[list["Salary"]] = relationship(back_populates="operator")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"{self.surname!r} "
                f"{self.name!r} "
                f"{self.patronymic!r})")

    def __repr__(self):
        return str(self)


# модель таблицы рабочих смен
class Work(Base):

    id: Mapped[int_pk]
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    # Связи
    operator: Mapped["Employee"] = relationship(back_populates="works")
    statistics: Mapped[list["Statistic"]] = relationship(back_populates="works")


# модель таблицы перерывов сотрудников
class Break(Base):

    id: Mapped[int_pk]
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    # Связи
    operator: Mapped["Employee"] = relationship(back_populates="breaks")


# модель таблицы вариантов параметров оценки сотрудников
class StatisticParameter(PyEnum):
    # положительные параметры оценки
    FIRST = "reply to first message"    # ответ на первое сообщение
    FOLLOWUP = "reply follow up message"    # ответ на последующие сообщения
    POLITENESS = "politeness"   # вежливость
    COMPETENCE = "competence"   # компетентность
    # отрицательные параметры оценки
    SHORTCOMINGS = "shortcomings"    # недоработки
    LATENESS = "lateness"    # опоздания


# модель таблицы статистики сотрудников
class Statistic(Base):

    id: Mapped[int_pk]
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    parameter: Mapped[StatisticParameter] = mapped_column(
        Enum(StatisticParameter, name="statistic_parameter_enum"),
        nullable=False
    )
    value: Mapped[float] = mapped_column(Integer, nullable=False)
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    work_id: Mapped[int] = mapped_column(ForeignKey("works.id"), nullable=True)

    # Связи
    operator: Mapped["Employee"] = relationship(back_populates="statistics")
    work: Mapped["Work"] = relationship(back_populates="statistics")


# Перечисление для типа коэффициента
class CoefficientType(PyEnum):
    POSITIVE = "positive"  # Положительный коэффициент
    NEGATIVE = "negative"  # Негативный коэффициент


# модель таблицы коэффициентов
class Coefficient(Base):

    id: Mapped[int_pk]
    parameter: Mapped[StatisticParameter] = mapped_column(
        Enum(StatisticParameter, name="statistic_parameter_enum"),
        nullable=False
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


# модель таблицы зарплаты
class Salary(Base):
    __tablename__ = "salaries"

    id: Mapped[int_pk]
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    calculation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    period_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)  # Начало расчетного периода
    period_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)  # Конец расчетного периода

    # Параметры из StatisticParameter
    reply_first_message: Mapped[float] = mapped_column(Float, default=0.0)
    reply_follow_up_message: Mapped[float] = mapped_column(Float, default=0.0)
    politeness: Mapped[float] = mapped_column(Float, default=0.0)
    competence: Mapped[float] = mapped_column(Float, default=0.0)
    shortcomings: Mapped[float] = mapped_column(Float, default=0.0)
    lateness: Mapped[float] = mapped_column(Float, default=0.0)

    # Сумма всех параметров
    total_score: Mapped[float] = mapped_column(
        Float,
        Computed(
            "reply_first_message + reply_follow_up_message + politeness + competence + shortcomings + lateness",
            persisted=True
        )
    )

    # Итоговая зарплата
    final_salary: Mapped[float] = mapped_column(Float, nullable=False)

    # Связи
    operator: Mapped["Employee"] = relationship(back_populates="salaries")

    def __str__(self):
        return (f"operator_id={self.operator_id}, "
                f"period={self.period_start.date()} - {self.period_end.date()}, "
                f"salary={self.final_salary})")

    def __repr__(self):
        return str(self)

