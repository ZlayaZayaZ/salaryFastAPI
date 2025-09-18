from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Integer
from datetime import datetime
from app.database import Base, int_pk
from app.operator.models import Employee
from app.work_time.models import Work
from app.parametr.models import Parameter


# модель таблицы статистики сотрудников
class Statistic(Base):

    id: Mapped[int_pk]
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    parameter_id: Mapped[int] = mapped_column(ForeignKey("parameters.id"), nullable=False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    work_id: Mapped[int] = mapped_column(ForeignKey("works.id"), nullable=True)

    # Связи
    parameter: Mapped["Parameter"] = relationship("Parameter", back_populates="statistics")
    operator: Mapped["Employee"] = relationship("Employee", back_populates="statistics")
    work: Mapped["Work"] = relationship("Work", back_populates="statistics")

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "parameter_id": self.parameter_id,
            "value": self.value,
            "operator_id": self.operator_id,
            "work_id": self.work_id,

            "parameter": self.parameter,
            "work": self.work,
            "operator": self.operator,
        }

