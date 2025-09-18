from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer, Float
from app.database import Base, int_pk
from app.statistic.models import Statistic


# модель для таблицы параметров оценки
class Parameter(Base):

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    norm: Mapped[int] = mapped_column(Integer, nullable=False)
    base: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.25,
        comment="Вес коэффициента в границах от 0 до 1"
    )
    is_positive: Mapped[bool] = mapped_column(Boolean, default=True)  # Флаг положительного/отрицательного параметра

    # Связи
    statistics: Mapped[list["Statistic"]] = relationship("Statistic", back_populates="parameter")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"parameter={self.name}, "
                f"is_positive={self.is_positive})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "norm": self.norm,
            "base": self.base,
            "weight": self.weight,
            "is_positive": self.is_positive,

            "statistics": self.statistics,
        }

