from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from app.database import Base, int_pk
from app.statistic.models import Statistic


# модель для таблицы параметров оценки
class Parameter(Base):

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_positive: Mapped[bool] = mapped_column(Boolean, default=True)  # Флаг положительного/отрицательного параметра

    # Связь со статистикой
    statistics: Mapped[list["Statistic"]] = relationship("Statistic", back_populates="parameter")
