from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class SSalary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    operator_id: int = Field(..., description="id оператора")
    calculation_date: datetime = Field(..., description="дата расчетов")
    period_start: datetime = Field(..., min_length=1, max_length=50, description="дата начал расчета")
    period_end: datetime = Field(..., min_length=1, max_length=150, description="дата окончания расчета")
    total_score: float = Field(..., description="сумма получившихся коэффициентов")
    final_salary: float = Field(..., description="итоговая сумма зарплаты")


class SSalaryAdd(BaseModel):

    operator_id: int = Field(..., description="id оператора")
    # calculation_date: datetime = Field(..., description="дата расчетов") - должна проставляться автоматически
    period_start: datetime = Field(..., min_length=1, max_length=50, description="дата начал расчета")
    period_end: datetime = Field(..., min_length=1, max_length=150, description="дата окончания расчета")
    # total_score: float = Field(..., description="сумма получившихся коэффициентов") - должен рассчитываться
    #                                               автоматически по данным таблиц статистики и параметров
    # final_salary: float = Field(..., description="итоговая сумма зарплаты") - должен получаться перемножением
    #                                               значения зарплаты в таблицу Employee и значения total_score

