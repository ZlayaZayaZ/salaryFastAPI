from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime
from app.database import Base, int_pk
from app.operator.models import Employee
from app.statistic.models import Statistic


# модель таблицы рабочих смен
class Work(Base):

    id: Mapped[int_pk]
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    # Связи
    operator: Mapped["Employee"] = relationship("Employee", back_populates="works")
    statistics: Mapped[list["Statistic"]] = relationship("Statistic", back_populates="works")


# модель таблицы перерывов сотрудников
class Break(Base):

    id: Mapped[int_pk]
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)

    # Связи
    operator: Mapped["Employee"] = relationship("Employee", back_populates="breaks")

