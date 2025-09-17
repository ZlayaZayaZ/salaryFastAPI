from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer
from app.database import Base, int_pk
from app.work_time.models import Work, Break
from app.statistic.models import Statistic
from app.salary.models import Salary


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
    works: Mapped[list["Work"]] = relationship("Work", back_populates="operator")
    breaks: Mapped[list["Break"]] = relationship("Break", back_populates="operator")
    statistics: Mapped[list["Statistic"]] = relationship("Statistic", back_populates="operator")
    salaries: Mapped[list["Salary"]] = relationship("Salary", back_populates="operator")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"{self.surname!r} "
                f"{self.name!r} "
                f"{self.patronymic!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "surname": self.surname,
            "name": self.name,
            "patronymic": self.patronymic,
            "job_title": self.job_title,
            "status": self.status,
            "salary": self.salary,
            "works": self.works,
            "breaks": self.breaks,
            "statistics": self.statistics,
            "salaries": self.salaries
        }


