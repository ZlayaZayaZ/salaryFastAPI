from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Float
from datetime import datetime
from app.database import Base, int_pk
# from app.operator.models import Employee


# модель таблицы зарплаты
class Salary(Base):
    __tablename__ = "salaries"

    id: Mapped[int_pk]
    operator_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    calculation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    period_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)  # Начало расчетного периода
    period_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)  # Конец расчетного периода

    # Сумма всех параметров в коэффициентах
    total_score: Mapped[float] = mapped_column(Float, nullable=True)

    # Итоговая зарплата
    final_salary: Mapped[float] = mapped_column(Float, nullable=True)

    # Связи
    operator: Mapped["Employee"] = relationship("Employee", back_populates="salaries")

    def __str__(self):
        return (f"operator_id={self.operator_id}, "
                f"period={self.period_start.date()} - {self.period_end.date()}, ",
                f"coefficient={self.total_score})"
                f"salary={self.final_salary})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "operator_id": self.operator_id,
            "calculation_date": self.calculation_date,
            "period_start": self.period_start,
            "period_end": self.period_end,
            "total_score": self.total_score,
            "final_salary": self.final_salary,

            "operator": self.operator
        }

